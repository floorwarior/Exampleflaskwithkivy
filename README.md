# Exampleflaskwithkivy

Don't change in buildozer.spec:
## Risky to change:
- api 27
- webview -> custom tabs
- This is the version that tries custom tabs instead of webview.
- werkzueg and flask version, this might break the code.

## How to use?
1. change the package name to your own package in the main.py file as well as in buildozer.spec
2. change the name of the service in main.py as well as in background.spec
3. drop your server code in backgroud.py
4. edit or replace the [AndroidManifest.tmpl.xml](.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/app/templates)
```
android:networkSecurityConfig="@xml/network_security_config" 
``` 
5. copy the network_security_config.xml into -> [res/xml](.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/app/src/main/res/xml) (make the xml folder first if it does not exists)
6. add these dependecies to gradle:
```
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.2 ,androidx.browser:browser:1.4.0

```



## How does it work?
- we start a background process that runs the flask server
- kivy opens a customtab to show the server page for this to work **you need to enable**
    - androidx 
    - android.api needs to be higher then 27 which is the last one supporting clearTextTraffic
    ------------------------------

## Tips:
some systems might kill your background/foreground process for example on Huawei phones you need to first allow the notification that shows your foreground, for the app. in the application settings.
then you also have to set in the launch manager manual instead of auto, so that the resource manager does not kill your app and its process






