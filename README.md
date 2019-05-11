# google-play
Scrapes data from Google Play Store
# Usage
### Installation
`pip install play-store`
### Simple Example
```python
import play_store

app = App('com.android.chrome')

# Get the app name
print(app.name)

# Get the app category
print(app.category)

# Is the app free
print(app.free)

# Get the name of the app developer
print(app.developer_name)
```
#### Attributes of App
* url - the play store url for the app
* name
* package_name
* description
* category
* logo
* price
* free - if the app is free or not
* developer_name
* developer_email
* developer_website
* rating
* reviews
* images
* similar - list of apps related to the app
### Search for apps
#### search(query)
```python
print(play_store.search('google chrome'))

# Ouput
['com.google.android.videos', 'com.deerslab.dinoTREX', 'com.wChromeplus_8575770',
'im.dnn.dinochrome', 'com.cloudmosa.puffinFree', 'webexplorer.amazing.speed',
'com.chromereadervoice', 'com.chrome.dev', 'com.oinkandstuff.chromewebstoredeveloperdashboard',
'org.mozilla.firefox', 'com.opera.browser', 'org.easyweb.browser',
'com.linuxjet.apps.ChromeUA','com.hsv.freeadblockerbrowser', 'nu.tommie.inbrowser',
'com.ekm.chromevr','net.the4thdimension.firefoxchromemanifestcheatsheet',
'com.google.android.apps.docs','com.codeweavers.cxoffice', 'com.opera.mini.native',
'net.the4thdimension.chromehtml5supported', 'com.google.android.apps.enterprise.cpanel',
'com.google.android.apps.subscriptions.red','com.chrome.canary',
'net.the4thdimension.chromecheatsheet', 'com.google.android.apps.chromecast.app','com.android.chrome',
'com.kiwibrowser.browser', 'com.funkeys.chrome','com.google.android.apps.googleassistant',
'com.google.android.apps.photos', 'com.transsion.phoenix', 'com.google.android.apps.mapslite',
'com.google.chromeremotedesktop', 'com.chrome.beta','com.sec.android.app.sbrowser',
'com.amaan.phonetochromepro', 'mobi.mgeek.TunnyBrowser','com.fevdev.nakedbrowser',
'com.amaan.phonetochrome', 'com.smajenterprise.incognitoaway','com.google.android.webview',
'de.alexotron.tabs', 'com.google.android.keep','io.kodular.duamalik86334.smartbrowser',
'net.xisberto.phonetodesktop', 'ua.kyiv.heneraliuk.crosupdates',
'com.google.android.googlequicksearchbox', 'com.myboyfriendisageek.airbrowser',
'com.google.android.apps.tachyon']
```
### Get apps from the same developer
#### developer(dev, amount)
```python
# Return 24 apps made by Google LLC
print(play_store.developer('Google LLC', 24))

# Output
['com.google.android.contacts', 'com.google.android.apps.maps', 'com.google.android.play.games',
'com.google.android.calculator', 'com.google.android.youtube', 'com.google.android.apps.docs',
'com.google.android.apps.messaging', 'com.google.android.apps.docs.editors.sheets',
'com.google.android.apps.translate', 'com.android.chrome', 'com.google.android.deskclock',
'com.google.android.talk', 'com.google.android.apps.photos', 'com.google.android.music',
'com.google.android.gm', 'com.google.android.apps.docs.editors.docs',
'com.google.android.calendar', 'com.google.android.keep',
'com.google.android.googlequicksearchbox', 'com.google.android.apps.tachyon']
```
### Get app leaderboard
#### leaderboard(identifier, category, start, amount) 
```python
# Get the leaderboard for topselling free apps
print(play_store.leaderboard(play_store.TOPSELLING_FREE))

# Output
['com.serejadexxx.ballsRotate', 'io.voodoo.crowdcity', 'com.azurgames.stackball',
'com.hulu.plus', 'com.mgc.runnergame', 'com.crazylabs.amaze.game',
'com.pandora.android', 'com.squareup.cash', 'com.snapchat.android',
'com.clean.road', 'com.spotify.music', 'com.whatsapp', 'com.housepaint.game',
'com.colorup.game', 'com.facebook.orca', 'com.facebook.katana',
'com.instagram.android', 'com.particlenews.newsbreak',
'com.zhiliaoapp.musically', 'com.google.android.apps.youtube.music',
'com.popcore.foldingblocks', 'com.amanotes.beathopper', 'com.netflix.mediaclient',
'com.geishatokyo.trafficrun']
```
## Constants
* TOPSELLING_FREE
* TOPSELLING_PAID
## Categories
`art_and_design` `auto_and_vehicles` `books_and_reference`
`brain` `business` `comics` `communication` `education`
`entertainment` `finance` `game` `health_and_fitness`
`house_and_home` `libraries_and_demo` `lifestyle`
`media_and_video` `medical` `music_and_audio`
`news_and_magazines` `personalization` `photography`
`productivity` `shopping` `social` `sports` `tools`
`transportation` `travel_and_local` `weather`
