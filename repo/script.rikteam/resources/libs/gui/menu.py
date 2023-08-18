################################################################################
#      Copyright (C) 2019 drinfernoo                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

import glob
import os
import re

try:  # Python 3
    from urllib.parse import quote_plus
    from urllib.request import urlretrieve
except ImportError:  # Python 2
    from urllib import quote_plus
    from urllib import urlretrieve

from resources.libs.common import directory
from resources.libs.common.config import CONFIG


###########################
#      Menu Items         #
###########################

def check_for_fm():
    if not xbmc.getCondVisibility('System.HasAddon(script.kodi.android.update)'):
        from resources.libs.gui import addon_menu
        addon_menu.install_from_kodi('script.kodi.android.update')
    
    try:
        updater = xbmcaddon.Addon('script.kodi.android.update')
    except RuntimeError as e:
        return False
        
    fm = int(updater.getSetting('File_Manager'))
    apps = xbmcvfs.listdir('androidapp://sources/apps/')[1]
    
    if fm == 0 and 'com.android.documentsui' not in apps:
        dialog = xbmcgui.Dialog()
        choose = dialog.yesno(CONFIG.ADDONTITLE, 'Parece que su dispositivo no tiene un administrador de archivos predeterminado. ¿Le gustaría configurar uno ahora?')
        if not choose:
            dialog.ok(CONFIG.ADDONTITLE, 'If an APK downloads, but doesn\'t open for installation, try changing your file manager in {}\'s "Install Settings".'.format(CONFIG.ADDONTITLE))
        else:
            from resources.libs import install
            install.choose_file_manager()
            
    return True


def apk_menu(url=None):
    from resources.libs.common import logging
    from resources.libs.common import tools

    if check_for_fm():
        directory.add_dir('Official Kodi APK\'s', {'mode': 'kodiapk'}, icon=CONFIG.ICONAPK, themeit=CONFIG.THEME1)
        directory.add_separator()

    response = tools.open_url(CONFIG.APKFILE)
    url_response = tools.open_url(url)

    if response:
        TEMPAPKFILE = tools.clean_text(url_response.text if url else response.text)

        if TEMPAPKFILE:
            match = re.compile('name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"').findall(TEMPAPKFILE)
            if len(match) > 0:
                x = 0
                for aname, section, url, icon, fanart, adult, description in match:
                    if not CONFIG.SHOWADULT == 'true' and adult.lower() == 'yes':
                        continue
                    if section.lower() == 'yes':
                        x += 1
                        directory.add_dir("[B]{0}[/B]".format(aname), {'mode': 'apk', 'name': aname, 'url': url}, description=description, icon=icon, fanart=fanart, themeit=CONFIG.THEME3)
                    else:
                        x += 1
                        directory.add_file(aname, {'mode': 'apkinstall', 'name': aname, 'url': url}, description=description, icon=icon, fanart=fanart, themeit=CONFIG.THEME2)
                    if x == 0:
                        directory.add_file("No addons added to this menu yet!", themeit=CONFIG.THEME2)
            else:
                logging.log("[APK Menu] ERROR: Invalid Format.", level=xbmc.LOGERROR)
        else:
            logging.log("[APK Menu] ERROR: URL for apk list not working.", level=xbmc.LOGERROR)
            directory.add_file('Url for txt file not valid', themeit=CONFIG.THEME3)
            directory.add_file('{0}'.format(CONFIG.APKFILE), themeit=CONFIG.THEME3)
    else:
        logging.log("[APK Menu] No APK list added.")


def youtube_menu(url=None):
    from resources.libs.common import logging
    from resources.libs.common import tools

    response = tools.open_url(CONFIG.YOUTUBEFILE)
    url_response = tools.open_url(url)

    if response:
        TEMPYOUTUBEFILE = url_response.text if url else response.text

        if TEMPYOUTUBEFILE:
            link = TEMPYOUTUBEFILE.replace('\n', '').replace('\r', '').replace('\t', '')
            match = re.compile('name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
            if len(match) > 0:
                for name, section, url, icon, fanart, description in match:
                    if section.lower() == "yes":
                        directory.add_dir("[B]{0}[/B]".format(name), {'mode': 'youtube', 'name': name, 'url': url}, description=description, icon=icon, fanart=fanart, themeit=CONFIG.THEME3)
                    else:
                        directory.add_file(name, {'mode': 'viewVideo', 'url': url}, description=description, icon=icon, fanart=fanart, themeit=CONFIG.THEME2)
            else:
                logging.log("[YouTube Menu] ERROR: Invalid Format.")
        else:
            logging.log("[YouTube Menu] ERROR: URL for YouTube list not working.")
            directory.add_file('Url for txt file not valid', themeit=CONFIG.THEME3)
            directory.add_file('{0}'.format(CONFIG.YOUTUBEFILE), themeit=CONFIG.THEME3)
    else:
        logging.log("[YouTube Menu] No YouTube list added.")

#########################################NET TOOLS#############################################


def net_tools():
    directory.add_dir('Speed Test', {'mode': 'speedtest'}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME1)
    if CONFIG.HIDESPACERS == 'No':
        directory.add_separator()
    directory.add_dir('View IP Address & MAC Address', {'mode': 'viewIP'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)


def view_ip():
    from resources.libs import speedtest

    mac, inter_ip, ip, city, state, country, isp = speedtest.net_info()
    directory.add_file('[COLOR {0}]MAC:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, mac), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Internal IP: [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, inter_ip), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]External IP:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, ip), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]City:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, city), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]State:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, state), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Country:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, country), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]ISP:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, isp), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)


def speed_test():
    from datetime import date

    directory.add_file('Iniciando Test de Velocidad', {'mode': 'runspeedtest'}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)
    if os.path.exists(CONFIG.SPEEDTEST):
        speedimg = glob.glob(os.path.join(CONFIG.SPEEDTEST, '*.png'))
        speedimg.sort(key=lambda f: os.path.getmtime(f), reverse=True)
        if len(speedimg) > 0:
            directory.add_file('Clear Results', {'mode': 'clearspeedtest'}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)
            directory.add_separator('Previous Runs', icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)
            for item in speedimg:
                created = date.fromtimestamp(os.path.getmtime(item)).strftime('%m/%d/%Y %H:%M:%S')
                img = item.replace(os.path.join(CONFIG.SPEEDTEST, ''), '')
                directory.add_file('[B]{0}[/B]: [I]Ran {1}[/I]'.format(img, created), {'mode': 'viewspeedtest', 'name': img}, icon=CONFIG.ICONSPEED, themeit=CONFIG.THEME3)


def clear_speed_test():
    from resources.libs.common import tools

    speedimg = glob.glob(os.path.join(CONFIG.SPEEDTEST, '*.png'))
    for file in speedimg:
        tools.remove_file(file)


def view_speed_test(img=None):
    from resources.libs.gui import window

    img = os.path.join(CONFIG.SPEEDTEST, img)
    window.show_speed_test(img)


def run_speed_test():
    from resources.libs.common import logging
    from resources.libs import speedtest

    try:
        found = speedtest.speedtest()
        if not os.path.exists(CONFIG.SPEEDTEST):
            os.makedirs(CONFIG.SPEEDTEST)
        urlsplits = found[0].split('/')
        dest = os.path.join(CONFIG.SPEEDTEST, urlsplits[-1])
        urlretrieve(found[0], dest)
        view_speed_test(urlsplits[-1])
    except Exception as e:
        logging.log("[Speed Test] Error Test de Velocidad: {0}".format(e), level=xbmc.LOGDEBUG)
        pass


def system_info():
    from resources.libs.common import logging
    from resources.libs.common import tools
    from resources.libs import speedtest

    infoLabel = ['System.FriendlyName', 'System.BuildVersion', 'System.CpuUsage', 'System.ScreenMode',
                 'Network.IPAddress', 'Network.MacAddress', 'System.Uptime', 'System.TotalUptime', 'System.FreeSpace',
                 'System.UsedSpace', 'System.TotalSpace', 'System.Memory(free)', 'System.Memory(used)',
                 'System.Memory(total)']
    data = []
    x = 0
    for info in infoLabel:
        temp = tools.get_info_label(info)
        y = 0
        while temp == "Busy" and y < 10:
            temp = tools.get_info_label(info)
            y += 1
            logging.log("{0} sleep {1}".format(info, str(y)))
            xbmc.sleep(200)
        data.append(temp)
        x += 1
    storage_free = data[8] if 'Una' in data[8] else tools.convert_size(int(float(data[8][:-8])) * 1024 * 1024)
    storage_used = data[9] if 'Una' in data[9] else tools.convert_size(int(float(data[9][:-8])) * 1024 * 1024)
    storage_total = data[10] if 'Una' in data[10] else tools.convert_size(int(float(data[10][:-8])) * 1024 * 1024)
    ram_free = tools.convert_size(int(float(data[11][:-2])) * 1024 * 1024)
    ram_used = tools.convert_size(int(float(data[12][:-2])) * 1024 * 1024)
    ram_total = tools.convert_size(int(float(data[13][:-2])) * 1024 * 1024)

    picture = []
    music = []
    video = []
    programs = []
    repos = []
    scripts = []
    skins = []

    fold = glob.glob(os.path.join(CONFIG.ADDONS, '*/'))
    for folder in sorted(fold, key = lambda x: x):
        foldername = os.path.split(folder[:-1])[1]
        if foldername == 'packages': continue
        xml = os.path.join(folder, 'addon.xml')
        if os.path.exists(xml):
            prov = re.compile("<provides>(.+?)</provides>").findall(tools.read_from_file(xml))
            if len(prov) == 0:
                if foldername.startswith('skin'):
                    skins.append(foldername)
                elif foldername.startswith('repo'):
                    repos.append(foldername)
                else:
                    scripts.append(foldername)
            elif not (prov[0]).find('executable') == -1:
                programs.append(foldername)
            elif not (prov[0]).find('video') == -1:
                video.append(foldername)
            elif not (prov[0]).find('audio') == -1:
                music.append(foldername)
            elif not (prov[0]).find('image') == -1:
                picture.append(foldername)

    directory.add_file('[B]Media Center Info:[/B]', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Name:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[0]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
    directory.add_file('[COLOR {0}]Version:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[1]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
    directory.add_file('[COLOR {0}]Platform:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, tools.platform().title()), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
    directory.add_file('[COLOR {0}]CPU Usage:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[2]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)
    directory.add_file('[COLOR {0}]Screen Mode:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[3]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME3)

    directory.add_file('[B]Uptime:[/B]', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Current Uptime:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[6]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Total Uptime:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, data[7]), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)

    directory.add_file('[B]Local Storage:[/B]', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Used Storage:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, storage_used), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Free Storage:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, storage_free), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Total Storage:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, storage_total), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)

    directory.add_file('[B]Ram Usage:[/B]', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Used Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, ram_free), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Free Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, ram_used), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Total Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, ram_total), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)

    mac, inter_ip, ip, city, state, country, isp = speedtest.net_info()
    directory.add_file('[B]Network:[/B]', icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Mac:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, mac), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Internal IP: [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, inter_ip), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]External IP:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, ip), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]City:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, city), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]State:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, state), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Country:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, country), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]ISP:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, isp), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)

    totalcount = len(picture) + len(music) + len(video) + len(programs) + len(scripts) + len(skins) + len(repos)
    directory.add_file('[B]Addons([COLOR {0}]{1}[/COLOR]):[/B]'.format(CONFIG.COLOR1, totalcount), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Video Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(video))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Program Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(programs))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Music Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(music))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Picture Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(picture))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Repositories:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(repos))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Skins:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(skins))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)
    directory.add_file('[COLOR {0}]Scripts/Modules:[/COLOR] [COLOR {1}]{2}[/COLOR]'.format(CONFIG.COLOR1, CONFIG.COLOR2, str(len(scripts))), icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME2)

def backups_menu():
        directory.add_file('Copia de Seguridad de la Videoteca', {'mode': 'backup', 'action': 'gui'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME1)
        directory.add_file('Restaurar Copia de Seguridad de la Videoteca', {'mode': 'restore', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)
        directory.add_file('Copia de Seguridad del Skin', {'mode': 'backup', 'action': 'theme'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME1)
        directory.add_file('Restaurar Cpoia de Seguridad del Skin', {'mode': 'restore', 'action': 'gui'}, icon=CONFIG.ICONMAINT, themeit=CONFIG.THEME1)


def save_menu():
    on = '[COLOR springgreen]ON[/COLOR]'
    off = '[COLOR red]OFF[/COLOR]'

    trakt = 'true' if CONFIG.KEEPTRAKT == 'true' else 'false'
    alfa = 'true' if CONFIG.KEEPalfa == 'true' else 'false'
    login = 'true' if CONFIG.KEEPLOGIN == 'true' else 'false'
    sources = 'true' if CONFIG.KEEPSOURCES == 'true' else 'false'
    myvideos = 'true' if CONFIG.KEEPMYVIDEOS == 'true' else 'false'
    advanced = 'true' if CONFIG.KEEPADVANCED == 'true' else 'false'
    profiles = 'true' if CONFIG.KEEPPROFILES == 'true' else 'false'
    playercore = 'true' if CONFIG.KEEPPLAYERCORE == 'true' else 'false'
    guisettings = 'true' if CONFIG.KEEPGUISETTINGS == 'true' else 'false'
    favourites = 'true' if CONFIG.KEEPFAVS == 'true' else 'false'
    repos = 'true' if CONFIG.KEEPREPOS == 'true' else 'false'
    super = 'true' if CONFIG.KEEPSUPER == 'true' else 'false'
    whitelist = 'true' if CONFIG.KEEPWHITELIST == 'true' else 'false'

    directory.add_file('Proteger Datos de Trakt.tv: {0}'.format(trakt.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keeptrakt'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Datos del Addon Alfa: {0}'.format(alfa.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepalfa'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Fuentes \'Sources.xml\': {0}'.format(sources.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepsources'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Videoteca de la aplicación: {0}'.format(myvideos.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepmyvideos'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Perfiles: {0}'.format(profiles.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepprofiles'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Reproductores \'playercorefactory.xml\': {0}'.format(playercore.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepplayercore'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Configuración de Kodi \'guisettings.xml\': {0}'.format(guisettings.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepguiseettings'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Buffer \'Advancedsettings.xml\': {0}'.format(advanced.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepadvanced'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)
    directory.add_file('Proteger Favoritos: {0}'.format(favourites.replace('true', on).replace('false', off)), {'mode': 'togglesetting', 'name': 'keepfavourites'}, icon=CONFIG.ICONSAVE, themeit=CONFIG.THEME1)


def trakt_menu():
    from resources.libs import traktit

    keep_trakt = '[COLOR springgreen]ON[/COLOR]' if CONFIG.KEEPTRAKT == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(CONFIG.TRAKTSAVE) if not CONFIG.TRAKTSAVE == '' else 'Trakt hasn\'t been saved yet.'
    directory.add_file('Guardar Datos de Trakt.tv: {0}'.format(keep_trakt), {'mode': 'togglesetting', 'name': 'keeptrakt'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    if CONFIG.KEEPTRAKT == 'true':
        directory.add_file('Último Guardado: {0}'.format(str(last)), icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    directory.add_separator(icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)

    for trakt in traktit.ORDER:
        if xbmc.getCondVisibility('System.HasAddon({0})'.format(traktit.TRAKTID[trakt]['plugin'])):
            name = traktit.TRAKTID[trakt]['name']
            path = traktit.TRAKTID[trakt]['path']
            saved = traktit.TRAKTID[trakt]['saved']
            file = traktit.TRAKTID[trakt]['file']
            user = CONFIG.get_setting(saved)
            auser = traktit.trakt_user(trakt)
            icon = traktit.TRAKTID[trakt]['icon'] if os.path.exists(path) else CONFIG.ICONTRAKT
            fanart = traktit.TRAKTID[trakt]['fanart'] if os.path.exists(path) else CONFIG.ADDON_FANART
            menu = create_addon_data_menu('Trakt', trakt)
            menu2 = create_save_data_menu('Trakt', trakt)
            menu.append((CONFIG.THEME2.format('{0} Settings'.format(name)), 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=trakt)'.format(CONFIG.ADDON_ID, trakt)))

            directory.add_file('[+]-> {0}'.format(name), icon=icon, fanart=fanart, themeit=CONFIG.THEME3)
            if not os.path.exists(path):
                directory.add_file('[COLOR red]Datos de Traktv: No Instalado[/COLOR]', icon=icon, fanart=fanart, menu=menu)
            elif not auser:
                directory.add_file('[COLOR red]Datos de Trakt.tv: No Registrado[/COLOR]', {'mode': 'authtrakt', 'name': trakt}, icon=icon, fanart=fanart, menu=menu)
            else:
                directory.add_file('[COLOR springgreen]Datos de Trakt.tv: {0}[/COLOR]'.format(auser), {'mode': 'authtrakt', 'name': trakt}, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file):
                    directory.add_file('[COLOR red]Guardar Datos: Archivo Guardado encontrado(Importar Datos)[/COLOR]', {'mode': 'importtrakt', 'name': trakt}, icon=icon, fanart=fanart, menu=menu2)
                else:
                    directory.add_file('[COLOR red]Datos Guardados: No Guardados[/COLOR]', {'mode': 'savetrakt', 'name': trakt}, icon=icon, fanart=fanart, menu=menu2)
            else:
                directory.add_file('[COLOR springgreen]Datos Guardados: {0}[/COLOR]'.format(user), icon=icon, fanart=fanart, menu=menu2)

    directory.add_separator()
    directory.add_file('Guardar todos los Datos', {'mode': 'savetrakt', 'name': 'all'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    directory.add_file('Recuperar todos los Datos', {'mode': 'restoretrakt', 'name': 'all'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    directory.add_file('Importar Datos', {'mode': 'importtrakt', 'name': 'all'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    directory.add_file('Borrar todos los Datos', {'mode': 'addontrakt', 'name': 'all'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)
    directory.add_file('Borrar todos los Datos guardados', {'mode': 'cleartrakt', 'name': 'all'}, icon=CONFIG.ICONTRAKT, themeit=CONFIG.THEME3)


def alfa_menu():
    from resources.libs import alfait

    keep_alfa = '[COLOR springgreen]ON[/COLOR]' if CONFIG.KEEPalfa == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(CONFIG.alfaSAVE) if not CONFIG.alfaSAVE == '' else 'Alfa authorizations haven\'t been saved yet.'
    directory.add_file('Datos de Alfa Guardados: {0}'.format(keep_alfa), {'mode': 'togglesetting', 'name': 'keepalfa'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    if CONFIG.KEEPalfa == 'true':
        directory.add_file('Último Guardado: {0}'.format(str(last)), icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    directory.add_separator(icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)

    for alfa in alfait.ORDER:
        if xbmc.getCondVisibility('System.HasAddon({0})'.format(alfait.alfaID[alfa]['plugin'])):
            name = alfait.alfaID[alfa]['name']
            path = alfait.alfaID[alfa]['path']
            saved = alfait.alfaID[alfa]['saved']
            file = alfait.alfaID[alfa]['file']
            user = CONFIG.get_setting(saved)
            auser = alfait.alfa_user(alfa)
            icon = alfait.alfaID[alfa]['icon'] if os.path.exists(path) else CONFIG.ICONalfa
            fanart = alfait.alfaID[alfa]['fanart'] if os.path.exists(path) else CONFIG.ADDON_FANART
            menu = create_addon_data_menu('alfa', alfa)
            menu2 = create_save_data_menu('alfa', alfa)
            menu.append((CONFIG.THEME2.format('{0} Settings'.format(name)), 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=alfa)'.format(CONFIG.ADDON_ID, alfa)))

            directory.add_file('[+]-> {0}'.format(name), icon=icon, fanart=fanart, themeit=CONFIG.THEME3)
            if not os.path.exists(path):
                directory.add_file('[COLOR red]Datos de Alfa: No Instalado[/COLOR]', icon=icon, fanart=fanart, menu=menu)
            elif not auser:
                directory.add_file('[COLOR red]Datos de Alfa: No Registrado[/COLOR]', {'mode': 'authalfa', 'name': alfa}, icon=icon, fanart=fanart, menu=menu)
            else:
                directory.add_file('[COLOR springgreen]Datos de Alfa: {0}[/COLOR]'.format(auser), {'mode': 'authalfa', 'name': alfa}, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file):
                    directory.add_file('[COLOR red]Guardar Datos: Archivo Guardado encontrado (Importar Datos)[/COLOR]', {'mode': 'importalfa', 'name': alfa}, icon=icon, fanart=fanart, menu=menu2)
                else:
                    directory.add_file('[COLOR red]Datos Guardados: No Guardados[/COLOR]', {'mode': 'savealfa', 'name': alfa}, icon=icon, fanart=fanart, menu=menu2)
            else:
                directory.add_file('[COLOR springgreen]Datos Guardados: {0}[/COLOR]'.format(user), icon=icon, fanart=fanart, menu=menu2)

    directory.add_separator(themeit=CONFIG.THEME3)
    directory.add_file('Guardar todos los Datos', {'mode': 'savealfa', 'name': 'all'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    directory.add_file('Recuperar todos los Datos Guardados', {'mode': 'restorealfa', 'name': 'all'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    directory.add_file('Importar Datos', {'mode': 'importalfa', 'name': 'all'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    directory.add_file('Borrar todos los Datos de Alfa', {'mode': 'addonalfa', 'name': 'all'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)
    directory.add_file('Borrar todos los Datos Guardados', {'mode': 'clearalfa', 'name': 'all'}, icon=CONFIG.ICONalfa, themeit=CONFIG.THEME3)


def login_menu():
    from resources.libs import loginit

    keep_login = '[COLOR springgreen]ON[/COLOR]' if CONFIG.KEEPLOGIN == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(CONFIG.LOGINSAVE) if not CONFIG.LOGINSAVE == '' else 'Login data hasn\'t been saved yet.'
    directory.add_file('[I]Several of these addons are PAID services.[/I]', icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_file('Save API Keys: {0}'.format(keep_login), {'mode': 'togglesetting', 'name': 'keeplogin'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    if CONFIG.KEEPLOGIN == 'true':
        directory.add_file('Last Save: {0}'.format(str(last)), icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_separator(icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)

    for login in loginit.ORDER:
        if xbmc.getCondVisibility('System.HasAddon({0})'.format(loginit.LOGINID[login]['plugin'])):
            name = loginit.LOGINID[login]['name']
            path = loginit.LOGINID[login]['path']
            saved = loginit.LOGINID[login]['saved']
            file = loginit.LOGINID[login]['file']
            user = CONFIG.get_setting(saved)
            auser = loginit.login_user(login)
            icon = loginit.LOGINID[login]['icon'] if os.path.exists(path) else CONFIG.ICONLOGIN
            fanart = loginit.LOGINID[login]['fanart'] if os.path.exists(path) else CONFIG.ADDON_FANART
            menu = create_addon_data_menu('Login', login)
            menu2 = create_save_data_menu('Login', login)
            menu.append((CONFIG.THEME2.format('{0} Settings'.format(name)), 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=login)'.format(CONFIG.ADDON_ID, login)))

            directory.add_file('[+]-> {0}'.format(name), icon=icon, fanart=fanart, themeit=CONFIG.THEME3)
            if not os.path.exists(path):
                directory.add_file('[COLOR red]Addon Data: Not Installed[/COLOR]', icon=icon, fanart=fanart, menu=menu)
            elif not auser:
                directory.add_file('[COLOR red]Addon Data: Not Registered[/COLOR]', {'mode': 'authlogin', 'name': login}, icon=icon, fanart=fanart, menu=menu)
            else:
                directory.add_file('[COLOR springgreen]Addon Data: {0}[/COLOR]'.format(auser), {'mode': 'authlogin', 'name': login}, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file):
                    directory.add_file('[COLOR red]Saved Data: Save File Found (Import Data)[/COLOR]', {'mode': 'importlogin', 'name': login}, icon=icon, fanart=fanart, menu=menu2)
                else:
                    directory.add_file('[COLOR red]Saved Data: Not Saved[/COLOR]', {'mode': 'savelogin', 'name': login}, icon=icon, fanart=fanart, menu=menu2)
            else:
                directory.add_file('[COLOR springgreen]Saved Data: {0}[/COLOR]'.format(user), icon=icon, fanart=fanart, menu=menu2)

    directory.add_separator(themeit=CONFIG.THEME3)
    directory.add_file('Save All Login Info', {'mode': 'savelogin', 'name': 'all'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_file('Recover All Saved Login Info', {'mode': 'restorelogin', 'name': 'all'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_file('Import Login Info', {'mode': 'importlogin', 'name': 'all'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_file('Clear All Addon Login Info', {'mode': 'addonlogin', 'name': 'all'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)
    directory.add_file('Clear All Saved Login Info', {'mode': 'clearlogin', 'name': 'all'}, icon=CONFIG.ICONLOGIN, themeit=CONFIG.THEME3)


def enable_addons():
    from resources.libs.common import tools
    
    from xml.etree import ElementTree

    directory.add_file("[I][B][COLOR red]!!Aviso: deshabilitar algunos complementos puede causar problemas!![/COLOR][/B][/I]", icon=CONFIG.ICONMAINT)
    fold = glob.glob(os.path.join(CONFIG.ADDONS, '*/'))
    addonnames = []
    addonids = []
    for folder in sorted(fold, key=lambda x: x):
        foldername = os.path.split(folder[:-1])[1]
        if foldername in CONFIG.EXCLUDES:
            continue
        elif foldername in CONFIG.DEFAULTPLUGINS:
            continue
        elif foldername == 'packages':
            continue
        xml = os.path.join(folder, 'addon.xml')
        if os.path.exists(xml):
            root = ElementTree.parse(xml).getroot()
            addonid = root.get('id')
            addonname = root.get('name')
           
            try:
                addonnames.append(tools.get_addon_info(addonid, 'name'))
                addonids.append(addonid)
            except:                
                pass
                
            if xbmc.getCondVisibility('System.HasAddon({0})'.format(addonid)):
                state = "[COLOR springgreen][Enabled][/COLOR]"
                goto = "false"
            else:
                state = "[COLOR red][Disabled][/COLOR]"
                goto = "true"
                
            icon = os.path.join(folder, 'icon.png') if os.path.exists(os.path.join(folder, 'icon.png')) else CONFIG.ADDON_ICON
            fanart = os.path.join(folder, 'fanart.jpg') if os.path.exists(os.path.join(folder, 'fanart.jpg')) else CONFIG.ADDON_FANART
            directory.add_file("{0} {1}".format(state, addonname), {'mode': 'toggleaddon', 'name': addonid, 'url': goto}, icon=icon, fanart=fanart)
    if len(addonnames) == 0:
        directory.add_file("No Addons Found to Enable or Disable.", icon=CONFIG.ICONMAINT)


def remove_addon_data_menu():
    if os.path.exists(CONFIG.ADDON_DATA):
        directory.add_file('[COLOR red][B]Eliminar[/B][/COLOR] los Datos de todos los addons [Addon_Data]', {'mode': 'removedata', 'name': 'all'}, themeit=CONFIG.THEME1)
        directory.add_file('[COLOR red][B]Eliminar[/B][/COLOR] Datos del {0}'.format(CONFIG.ADDONTITLE), {'mode': 'resetaddon'}, themeit=CONFIG.THEME1)
        fold = glob.glob(os.path.join(CONFIG.ADDON_DATA, '*/'))
        for folder in sorted(fold, key = lambda x: x):
            foldername = folder.replace(CONFIG.ADDON_DATA, '').replace('\\', '').replace('/', '')
            icon = os.path.join(folder.replace(CONFIG.ADDON_DATA, CONFIG.ADDONS), 'icon.png')
            fanart = os.path.join(folder.replace(CONFIG.ADDON_DATA, CONFIG.ADDONS), 'fanart.png')
            folderdisplay = foldername
            replace = {'audio.': '[COLOR orange][AUDIO] [/COLOR]', 'metadata.': '[COLOR cyan][METADATA] [/COLOR]',
                       'module.': '[COLOR orange][MODULE] [/COLOR]', 'plugin.': '[COLOR blue][PLUGIN] [/COLOR]',
                       'program.': '[COLOR orange][PROGRAM] [/COLOR]', 'repository.': '[COLOR gold][REPO] [/COLOR]',
                       'script.': '[COLOR springgreen][SCRIPT] [/COLOR]',
                       'service.': '[COLOR springgreen][SERVICE] [/COLOR]', 'skin.': '[COLOR dodgerblue][SKIN] [/COLOR]',
                       'video.': '[COLOR orange][VIDEO] [/COLOR]', 'weather.': '[COLOR yellow][WEATHER] [/COLOR]'}
            for rep in replace:
                folderdisplay = folderdisplay.replace(rep, replace[rep])
            if foldername in CONFIG.EXCLUDES:
                folderdisplay = '[COLOR springgreen][B][Protegido][/B][/COLOR] {0}'.format(folderdisplay)
            else:
                folderdisplay = '[COLOR red][B]Eliminar[/B][/COLOR] {0}'.format(folderdisplay)
            directory.add_file(' {0}'.format(folderdisplay), {'mode': 'removedata', 'name': foldername}, icon=icon, fanart=fanart, themeit=CONFIG.THEME2)
    else:
        directory.add_file('Carpeta Addon_Data no encontrada.', themeit=CONFIG.THEME3)


def change_freq():
    from resources.libs.common import logging

    dialog = xbmcgui.Dialog()

    change = dialog.select("[COLOR {0}]¿Con qué frecuencia listaría la limpieza automática al iniciar??[/COLOR]".format(CONFIG.COLOR2), CONFIG.CLEANFREQ)
    if not change == -1:
        CONFIG.set_setting('autocleanfreq', str(change))
        logging.log_notify('[COLOR {0}]Limpieza automática[/COLOR]'.format(CONFIG.COLOR1),
                           '[COLOR {0}]Frecuencia ahora {1}[/COLOR]'.format(CONFIG.COLOR2, CONFIG.CLEANFREQ[change]))


def developer():
    directory.add_file('Create QR Code', {'mode': 'createqr'}, themeit=CONFIG.THEME1)
    directory.add_file('Test Notifications', {'mode': 'testnotify'}, themeit=CONFIG.THEME1)
    directory.add_file('Test Update', {'mode': 'testupdate'}, themeit=CONFIG.THEME1)
    directory.add_file('Test Build Prompt', {'mode': 'testbuildprompt'}, themeit=CONFIG.THEME1)
    directory.add_file('Test Save Data Settings', {'mode': 'testsavedata'}, themeit=CONFIG.THEME1)
    directory.add_file('Test Binary Detection', {'mode': 'binarycheck'}, themeit=CONFIG.THEME1)


###########################
#      Misc Functions     #
###########################


def create_addon_data_menu(add='', name=''):
    menu_items = []

    add2 = quote_plus(add.lower().replace(' ', ''))
    add3 = add.replace('alfa', 'Real alfa')
    name2 = quote_plus(name.lower().replace(' ', ''))
    name = name.replace('url', 'URL Resolver')
    menu_items.append((CONFIG.THEME2.format(name.title()), ' '))
    menu_items.append((CONFIG.THEME3.format('Save {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=save{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Restore {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=restore{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Clear {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=clear{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))

    menu_items.append((CONFIG.THEME2.format('{0} Settings'.format(CONFIG.ADDONTITLE)), 'RunPlugin(plugin://{0}/?mode=settings)'.format(CONFIG.ADDON_ID)))

    return menu_items


def create_save_data_menu(add='', name=''):
    menu_items = []

    add2 = quote_plus(add.lower().replace(' ', ''))
    add3 = add.replace('alfa', 'Real alfa')
    name2 = quote_plus(name.lower().replace(' ', ''))
    name = name.replace('url', 'URL Resolver')
    menu_items.append((CONFIG.THEME2.format(name.title()), ' '))
    menu_items.append((CONFIG.THEME3.format('Register {0}'.format(add3)), 'RunPlugin(plugin://{0}/?mode=auth{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Save {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=save{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Restore {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=restore{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Import {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=import{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))
    menu_items.append((CONFIG.THEME3.format('Clear Addon {0} Data'.format(add3)), 'RunPlugin(plugin://{0}/?mode=addon{1}&name={2})'.format(CONFIG.ADDON_ID, add2, name2)))

    menu_items.append((CONFIG.THEME2.format('{0} Settings'.format(CONFIG.ADDONTITLE)), 'RunPlugin(plugin://{0}/?mode=settings)'.format(CONFIG.ADDON_ID)))

    return menu_items
