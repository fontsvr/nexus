# -*- coding: utf-8 -*-
#------------------------------------------------------------
# mitelechopo - XBMC Add-on by Torete
# Version 0.2.5 (15.05.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
import os
import sys
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools
import requests
import six
import xbmcvfs
addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]RikTeam_[COLOR aqua]fonts[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.RikTeam_fonts")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')

def run():
 
    plugintools.set_view(plugintools.LIST)
 
    # Get params
    params = plugintools.get_params()
 
    if params.get("action") is None:
        main_list(params)
    else:
       action = params.get("action")
       url = params.get("url")
       exec(action+"(params)")
    plugintools.close_item_list()
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


   
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------

 

def main_list(params):

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR violet] RikTeam[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://res.cloudinary.com/dsmvomgrd/image/upload/v1684519184/build/fonts_fanart.jpghttps://imgur.com/a/kmDBgGd",  folder = False )   

    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]A C T U A L I Z A D O R [COLOR yellow]   D E [COLOR aqua]  F U E N T E S[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://res.cloudinary.com/dsmvomgrd/image/upload/v1684519183/build/fonts_icon.png", fanart = "https://res.cloudinary.com/dsmvomgrd/image/upload/v1684519184/build/fonts_fanart.jpg",  folder = False ) 

 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] RikTeam[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://res.cloudinary.com/dsmvomgrd/image/upload/v1684519183/build/fonts_icon.png", fanart = "https://res.cloudinary.com/dsmvomgrd/image/upload/v1684519184/build/fonts_fanart.jpg",  folder = False )   


    if six.PY2:
        translatePath = xbmc.translatePath
    elif six.PY3:
        translatePath = xbmcvfs.translatePath


    site = "https://pastebin.com/raw/kY3W2iRB"
    try:
        r = requests.get(site,timeout=3)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        #print ("OOps: Something Else",err)
        di='\n[COLOR red]Servidor caído[/COLOR]\n'+ str(err)
        xbmcgui.Dialog().notification("[COLOR yellow]info[/COLOR]", di, xbmcgui.NOTIFICATION_INFO, 15000, False)
        #xbmcgui.Dialog().textviewer("[COLOR yellow]info[/COLOR]", di)
        r = requests.get("https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/sources/sources.xml")
    except requests.exceptions.HTTPError as errh:
        di='\n[COLOR red]Http Error:[/COLOR]\n'+ str(errh)
        xbmcgui.Dialog().textviewer("[COLOR yellow]info[/COLOR]", di)
    except requests.exceptions.ConnectionError as errc:
        di='\n[COLOR red]Error Connecting:[/COLOR]\n'+ str(errc)
        xbmcgui.Dialog().textviewer("[COLOR yellow]info[/COLOR]", di)
    except requests.exceptions.Timeout as errt:
        di='\n[COLOR red]Timeout Error:[/COLOR]\n'+ str(errt)
        xbmcgui.Dialog().textviewer("[COLOR yellow]info[/COLOR]", di)
    

    t = r.text
    sources = xbmcvfs.translatePath('special://profile/sources.xml')    
    respuesta = xbmcgui.Dialog().yesno("[COLOR violet]"+"RikTeam"+"[/COLOR]", "[COLOR yellow]"+"Script "+"[COLOR violet]"+" RikTeam. "+"[COLOR yellow]"+"Pulsa Ok para borrar tus fuentes y añadir las pricipales"+" fuentes actualizadas."+"[COLOR lightpink]"+" Reiniciar Kodi para que coja los cambios."+"[/COLOR]", "No","Si")
   

    if respuesta:       
        if not os.path.isfile(sources):
            file = open(sources, 'w+')
            source_data = file.read()
            #file.truncate(0)
            file.seek(0)
            for linea in t:
                file.write(linea)
            file.seek(0)    
            file.close()
            xbmcgui.Dialog().notification('[COLOR violet]'+'RikTeam'+'[/COLOR]', '[COLOR lightgreen]'+'COPIA DE FUENTES REALIZADA EXITOSAMENTE.'+'[/COLOR]', xbmcgui.NOTIFICATION_INFO, 5000)
            
        else:
            file = open(sources,'w+')
            file.seek(0)
            file.truncate(0)
            for linea in t:
                file.write(linea)
            file.seek(0)    
            file.close()
            xbmcgui.Dialog().notification('[COLOR gold]RikTeam[/COLOR]', '[COLOR green]COPIA DE FUENTES REALIZADA EXITOSAMENTE.[/COLOR]', xbmcgui.NOTIFICATION_INFO, 5000)
            
    else:
        xbmcgui.Dialog().notification('Info', 'CANCELADA LA COPIA DE FUENTES.', xbmcgui.NOTIFICATION_ERROR, 4000) 
    exit(0)            
run()
