# Exampleflaskwithkivy

***This instruction does not work yet correctly***

Don't change in buildozer.spec:
## Risky to change:
- api 31
- werkzueg and flask version, this might break the code.

## How to use?
1. change the package name to your own package in the main.py file as well as in buildozer.spec
2. change the name of the service in main.py as well as in background.spec
3. drop your server code in backgroud.py
4. add these dependecies to gradle:
```
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.2 ,androidx.browser:browser:1.4.0

```
5. enable adroidx in buildozer.spec



## How does it work?
- we start a background process that runs the flask server
- kivy opens a customtab to show the server page


## Tips:
some systems might kill your background/foreground process for example on Huawei phones you need to first allow the notification that shows your foreground, for the app. in the application settings.
then you also have to set in the launch manager manual instead of auto, so that the resource manager does not kill your app and its process






