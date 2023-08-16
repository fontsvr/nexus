import os, xbmc, xbmcaddon

#########################################################
### Global Variables ####################################
#########################################################
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR orchid][B]RIKTEAM WIZARD[/B][/COLOR]'
BUILDERNAME    = '[COLOR white][B]RikTeam[/B][/COLOR]'
EXCLUDES       = [ADDON_ID, 'repository.fontsvr', 'script.module.kodi-six', 'script.module.six']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it. https://raw.githubusercontent.com/posadka/builds/main/builds/builds.txt
# https://raw.githubusercontent.com/fontsvr/fontsvr.github.io/master/wizard_nexus/builds_nexus.txt (20 builds)
# https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/builds_nexus.txt (19/20.x builds)
# https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/builds_all.txt
BUILDFILE      = 'https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/builds_all.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'https://' to ignore https://raw.githubusercontent.com/posadka/builds/main/builds/builds.txt
APKFILE        = 'https://raw.githubusercontent.com/fontsvr/fontsvr.github.io/master/wizard_nexus/apks/apks.txt'
# Text File with Youtube Videos urls.  Leave as 'https://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'https://'
# Text File for addon installer.  Leave as 'https://' to ignore
ADDONFILE      = 'https://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'orchid'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']*[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'RIKTEAM\n\nrikteam/me'
#Images used for the contact window.  https:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'qricon.png')
CONTACTFANART  = 'https://'
#########################################################

#########################################################
### Auto Update                   #######################
###        For Those With No Repo #######################
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'no'
# Url to wizard version
WIZARDFILE     = 'https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/builds_all.txt'
###################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = 'repository.fontsvr'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/addons/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL = 'https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/addons/zips/'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'No'
# Url to notification file
# https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/VR/Notify.txt
NOTIFICATION = 'https://raw.githubusercontent.com/fontsvr/repo-fontsVR/main/wizardfiles/VR/Notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR azure][B]RikTeam[/B][/COLOR] [COLOR white][B]Wizard [COLOR orchid]NEXUS[/B][/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE = 'https://res.cloudinary.com/dsmvomgrd/image/upload/v1683640913/build/banner.png'
# Font for Notification Window #13
FONTSETTINGS = 'Font14'
# Background for Notification Window
BACKGROUND = 'https://res.cloudinary.com/dsmvomgrd/image/upload/v1683640927/build/fandrart.png'
#########################################################