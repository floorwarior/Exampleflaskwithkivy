# Exampleflaskwithkivy

Don't change in buildozer.spec:
## Risky to change:
- api 27
- webview -> custom tabs
- Your can try to make (custom tabs)[https://github.com/floorwarior/Exampleflaskwithkivy/tree/customtab-version] work instead of webview
- werkzueg and flask version, this might break the code. 

## How to use?
1. change the package name to your own package in the main.py file as well as in buildozer.spec
2. change the name of the service in main.py as well as in background.spec
2. drop your server code in backgroud.py

## How does it work?
- we start a background process that runs the flask server
- kivy opens a webview to show the server page ( to have all the browser functionality check out (customtabs)[https://github.com/floorwarior/Exampleflaskwithkivy/tree/customtab-version] since webview is missing some features of a normal browser, for example TTS will not work)

## Tips:
some systems might kill your background/foreground process for example on Huawei phones you need to first allow the notification that shows your foreground, for the app. in the application settings.
then you also have to set in the launch manager manual instead of auto, so that the resource manager does not kill your app and its process






