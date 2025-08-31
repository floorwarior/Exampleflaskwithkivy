# Exampleflaskwithkivy

Don't change in buildozer.spec:
## Risky to change:
- api 27
- webview -> custom tabs
- Your can try to make custom tabs work instead of webview, but this requires androidx to be enabled and every single build where i tried that, fails with some kind of java.heap error, i tried increasing the size of the heap but it did not work and i kind of gave up on that
- werkzueg and flask version this might break the code.

## How to use?
1. change the package name to your own package in the main.py file as well as in buildozer.spec
2. change the name of the service in main.py as well as in background.spec
2. drop your server code in backgroud.py

## How does it work?
- we start a background process that runs the flask server
- kivy opens a webview to show the server page ( you can experiement with androidx and try to use custom tabs: from kvdroid.tools.webkit import launch_url, since webview is missing some features of a normal browser for example TTS will not work)
## Tips:
some systems might kill your background/foreground process for example on Huawei phones you need to first allow the notification that shows your foreground, for the app. in the application settings.
then you also have to set in the launch manager manual instead of auto, so that the resource manager does not kill your app and its process






