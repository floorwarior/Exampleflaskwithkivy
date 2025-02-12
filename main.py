from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout


## references:
##
##
## https://github.com/TirrouOussama/kivyserviceforeground/
##
##


from kivy.uix.label import Label



from kivy.utils import platform
#import webbrowser


#import multiprocessing
#import background

from kivy.clock import Clock

class FloorMobileApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Screen()
        self.rel = RelativeLayout()
        self.l = Label(text="Loading . . ")


        self.screen.add_widget(self.rel)
        self.rel.add_widget(self.l)


        if platform == "android":
            from webviewforflaskapp import WebView
            self.view = WebView(
                url="http://localhost:5000/",
                enable_javascript=True,
                enable_downloads=False,
                enable_zoom=False
            )



    def on_start(self):
        # this might or might not be a good aproach
        
        Clock.schedule_once(lambda x: self.view.open(),5) # 4 seconds seems to be not enough sometimes for the server to stand up



    def get_permit(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions 

            def callback(permissions, results):
                granted_permissions = [perm for perm, res in zip(permissions, results) if res]
                denied_permissions = [perm for perm, res in zip(permissions, results) if not res]

                if denied_permissions:
                    print('Denied permissions:', denied_permissions)

                elif granted_permissions:
                    print('Got all permissions')
                else:
                    print('No permissions were granted or denied')

            requested_permissions = [
                Permission.INTERNET,
                Permission.FOREGROUND_SERVICE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.SYSTEM_ALERT_WINDOW
            ]
            request_permissions(requested_permissions, callback)



    

    def build(self):
        if platform == 'android':
            self.get_permit()
            from jnius import autoclass
            from android import mActivity
            context = mActivity.getApplicationContext()
            SERVICE_NAME = "org.test.app.ServiceFlaskserver" #this must always contain Service as leading part of the service sencond part need to be Capitial!            
            self.service_target = autoclass(SERVICE_NAME)
            self.service_target.start(mActivity,"icon","This is title","this is message","") # the service now runs as foreground and it will be alive as long as the user doesnt kill the app or dismisses the notification

        return self.screen

if __name__ == "__main__":
    

    #flask_thread = threading.Thread(target=background.startapp, daemon=True)
    #flask_thread.start()

    FloorMobileApp().run()
