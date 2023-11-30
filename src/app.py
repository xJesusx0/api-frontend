from flask import * 
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/datos")
def datos():
    url = "https://xjesusx0.github.io/datos.json"

    datosJson = requests.get(url).json()
    print(datosJson)
    return render_template("datos.html",datos = datosJson)


app.run(debug = True,port=8000)