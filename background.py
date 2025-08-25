# this is the flask server that runs in the background
from flask import Flask
from flask import render_template
from jnius import autoclass, cast

#PythonService = autoclass("org.kivy.android.PythonService")
#PythonService.mService.setAutoRestartService(True) 


from kvdroid.tools.package import all_main_activities
from kvdroid.tools.package import package_info

app = Flask(__name__)

@app.route("/")
def hellothere():
	return render_template("generalkenobi.html")

if __name__ == "__main__":
    app.run(port=5003,debug=False,)
    
