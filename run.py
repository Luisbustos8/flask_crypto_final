import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

import sqlite3
import _config

data_base = "./data/movimientos.db"
@app.route("/")
def index():
    conn = sqlite3.connect("data_base")
    cur = conn.cursor()

    query = 'CREATE TABLE IF NOT EXISTS "movimientos"("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "date" TEXT, "time" TEXT, "from_currency" INTEGER, "from_quantity" REAL, "to_currency" INTEGER, "to_quantity" REAL, "precio_unitario" REAL, FOREIGN KEY("from_currency") REFERENCES "cryptos"("symbol"), FOREIGN KEY("to_currency") REFERENCES "cryptos"("symbol"));'
    cur.execute(query)

    todomovimiento = ("SELECT * FROM movimientos")
    movimiento = cur.execute(todomovimiento).fetchall()

    if len (movimiento) == 0:
        return render_template("indexnomove.html")
    else:
        query = ("SELECT * FROM movimientos")
        movimientos = cur.execute(movimiento).fetchall()
        conn.close()
        return render_template("index.html", movimientos=movimientos)
            

@app.route("/purchase", methods= ["GET", "POST"])
def purchase():


    
    conn = sqlite3.connect("data_base")



    return render_template("purchase.html")

@app.route("/calculate", methods=["GET"])
def calculate():
    API = "1dbb05ab-4813-4123-8201-8cd33cad7d7e"
    params = request.args
    url_convert = "https://sandbox-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}".format(params.get("form_quantity"), params.get("from_currency"), params.get("to_currency"), API)
    req = requests.get(url_convert)
    if req.status_code == 401:
        return jsonify()
    return req.text

    

    

@app.route("/status")
def status():
    return "Aquí irá el stado de tus inversiones"
