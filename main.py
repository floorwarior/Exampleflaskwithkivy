from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout



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
        elif platform == "windows" or platform == "linux":
            class Fire_fox():

                def open():
                    import webbrowser
                    webbrowser.open("http://localhost:5000/")

            self.view = Fire_fox()
       
        # adding the start screen



    def on_start(self):
        Clock.schedule_once(lambda x: self.view.open(),4)
        """        import threading
                from background import app, startapp
                threading.Thread(target=startapp).start()
"""

    def build(self):
        if platform == 'android':
            from jnius import autoclass
            service = autoclass('org.test.app.ServiceFlaskserver')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            argument = ''
            service.start(mActivity, argument)


    

        return self.screen

if __name__ == "__main__":
    

    #flask_thread = threading.Thread(target=background.startapp, daemon=True)
    #flask_thread.start()

    FloorMobileApp().run()
