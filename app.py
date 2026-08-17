from flask import Flask, render_template
from gh import gh

app = Flask(__name__)

@app.route("/")
def index():
    return str[gh["sensors"]["light_lux"]]

if __name__ == '__main__':
    app.run(debug=True)