from flask import Flask, render_template
from gh import gh

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", gh=gh)

@app.route("/Crops")
def Crops():
    return render_template("Crops.html", gh=gh)

@app.route("/Sensors")
def Sensors():
    return render_template("Sensors.html", gh=gh)

@app.route("/Onion")
def Onion():
    return render_template("Onion.html", gh=gh)

@app.route("/Tomato")
def Tomato():
    return render_template("Tomato.html", gh=gh)

@app.route("/Potato")
def Potato():
    return render_template("Potato.html", gh=gh)

@app.route("/Lettuce")
def Lettuce():
    return render_template("Lettuce.html", gh=gh)

if __name__ == '__main__':
    app.run(debug=True)