from flask import Flask, render_template
from gh import gh

app = Flask(__name__)

@app.route("/")
def index():
    print(gh)
    return render_template("index.html", gh=gh)

if __name__ == '__main__':
    app.run(debug=True)