# this is the flask server that runs in the background
from flask import Flask
from flask import render_template
#from jnius import autoclass, cast

#PythonService = autoclass("org.kivy.android.PythonService")
#PythonService.mService.setAutoRestartService(True) #if you want to make your server restart when there is more resources available


#from kvdroid.tools.package import all_main_activities
#from kvdroid.tools.package import package_info

app = Flask(__name__)

@app.route("/")
def hellothere():
	return render_template("generalkenobi.html")

    
app.run(port=5000,host="localhost")
