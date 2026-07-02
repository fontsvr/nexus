# default.py - element_launcher minimal i robust
import sys, urllib.parse
import xbmc, xbmcgui

def log(s, lvl=xbmc.LOGINFO):
    xbmc.log("elementum_launcher: %s" % s, lvl)

def get_params():
    params = {}
    # 1) plugin invocation: query string a sys.argv[2] (ex: "uri=magnet:...&title=...")
    if len(sys.argv) > 2 and sys.argv[2]:
        qs = sys.argv[2]
        try:
            params.update({k: v[0] for k, v in urllib.parse.parse_qs(qs).items()})
        except Exception as e:
            log("parse_qs error: %s" % str(e), xbmc.LOGWARNING)

    # 2) ExecuteAddon passes args com "key=val" en sys.argv[1:]
    for a in sys.argv[1:]:
        if '=' in a:
            k, v = a.split('=', 1)
            params[k] = v

    # 3) fallback: if someone passed a raw URI as first arg
    if not params and len(sys.argv) > 1:
        maybe = sys.argv[1].strip()
        if maybe:
            if maybe.startswith("plugin://") or maybe.startswith("magnet:") or maybe.startswith("http"):
                params['uri'] = maybe

    return params

def _extract_inner_magnet_from_plugin(uri_val):
    """If uri_val is plugin://...play?uri=magnet:..., return inner magnet (unquoted)."""
    try:
        parsed = urllib.parse.urlparse(uri_val)
        if parsed.query:
            q = urllib.parse.parse_qs(parsed.query)
            inner = q.get('uri') or q.get('url') or q.get('id')
            if inner:
                return urllib.parse.unquote_plus(inner[0])
    except Exception as e:
        log("extract_inner_magnet error: %s" % str(e), xbmc.LOGWARNING)
    return None

def _extract_dn_from_magnet(magnet):
    """If magnet contains dn=..., return decoded filename."""
    try:
        if not magnet:
            return None
        # magnet may be already percent-encoded or plain; parse its query part
        parsed = urllib.parse.urlparse(magnet)
        # if magnet was percent-encoded inside plugin URI, parsed.query will be empty;
        # fallback: split at '?' manually
        query = parsed.query
        if not query and '?' in magnet:
            query = magnet.split('?', 1)[1]
        qd = urllib.parse.parse_qs(query)
        dn = qd.get('dn')
        if dn:
            return urllib.parse.unquote_plus(dn[0])
    except Exception as e:
        log("title_from_magnet error: %s" % str(e), xbmc.LOGWARNING)
    return None

def main():
    log("started")
    params = get_params()
    uri = params.get('uri') or params.get('magnet')
    title = params.get('title', '').strip()
    log("title dels params.get: %s" % title)
    # si no tenim title explícit, intentem extreure'l del magnet (dn) o del plugin URI intern
    extracted_title = None
    inner_magnet = None
    if uri:
        if uri.startswith("plugin://"):
            inner_magnet = _extract_inner_magnet_from_plugin(uri)
            if inner_magnet:
                log("detected nested magnet inside plugin URI")
                extracted_title = _extract_dn_from_magnet(inner_magnet)
        elif uri.startswith("magnet:"):
            extracted_title = _extract_dn_from_magnet(uri)

    # Prioritat: param title > dn from magnet > fallback
    if not title:
        if extracted_title:
            title = extracted_title
            log("title set from magnet dn: %s" % title)
        else:
            title = "Stream"


    if not uri:
        # mostra teclat per enganxar manualment
        kb = xbmc.Keyboard('', 'Paste plugin URI or magnet (plugin://... or magnet:...)')
        kb.doModal()
        if kb.isConfirmed():
            uri = kb.getText().strip()

    if not uri:
        log("no URI received", xbmc.LOGWARNING)
        xbmcgui.Dialog().notification("Elementum Launcher", "No URI received", xbmcgui.NOTIFICATION_WARNING)
        return

    log("received uri: %s" % uri)

    # si hem rebut magnet -> construir plugin URI per Elementum
    if uri.startswith("magnet:"):
        plugin_uri = "plugin://plugin.video.elementum/play?uri=" + uri
        log("BRANCH: uri is magnet -> constructed plugin_uri: %s" % plugin_uri)
    elif uri.startswith("plugin://"):
        plugin_uri = uri
        log("BRANCH 2: uri is plugin:// and has no nested magnet")
    else:
        # si és una URL directa (.m3u8/.mp4) la reproduïm tal qual
        plugin_uri = uri

    log("will play -> %s" % plugin_uri)
    li = xbmcgui.ListItem(label=title)
    try:
        vtag = li.getVideoInfoTag()              # retorna InfoTagVideo
        vtag.setTitle(title)
    except Exception as e:
        # fallback curt per compatibilitat amb versions antigues
        '''try:
            li.setInfo('video', {'title': title})
        except Exception:
            xbmc.log("elementum_launcher: fallback setInfo failed: %s" % str(e), xbmc.LOGWARNING)
        '''
        # fallback mínim si la versió kodi no suporta getVideoInfoTag
        xbmc.log("elementum_launcher: getVideoInfoTag fallback: %s" % str(e), xbmc.LOGWARNING)
        # NO fem li.setInfo(...) si vols evitar la advertència
    try:
        # Preferim Player().play perquè gestiona millor fonts i plugins
        p = xbmc.Player()
        started = p.play(plugin_uri,li)
        log("Player.play returned: %s" % str(started))
        log("Using title: %s" % title)
        xbmcgui.Dialog().notification("Elementum Launcher", "Launching playback", xbmcgui.NOTIFICATION_INFO)
    except Exception as e:
        log("error playing: %s" % str(e), xbmc.LOGERROR)
        # prova RunPlugin com fallback
        try:
            xbmc.executebuiltin('RunPlugin(%s)' % plugin_uri)
            xbmcgui.Dialog().notification("Elementum Launcher", "Launching via RunPlugin", xbmcgui.NOTIFICATION_INFO)
        except Exception as e2:
            log("fallback RunPlugin failed: %s" % str(e2), xbmc.LOGERROR)
            xbmcgui.Dialog().notification("Elementum Launcher", "Error launching playback", xbmcgui.NOTIFICATION_ERROR)

if __name__ == '__main__':
    main()
