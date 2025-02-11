# this is the flask server that runs in the background
from flask import Flask
from flask import render_template

PythonService = autoclass("org.kivy.android.PythonService")
PythonService.mService.setAutoRestartService(True) 

app = Flask(__name__)

@app.route("/")
def hellothere():
	return render_template("generalkenobi.html")

if __name__ == "__main__":
    app.run(debug=True)
    
