import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
from datetime import datetime
import sqlite3
import _config


data_base = "./data/movimientos.db"
@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("data_base")
    cur = conn.cursor()

    query = 'CREATE TABLE IF NOT EXISTS "movimientos"("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "date" TEXT, "time" TEXT, "from_currency" INTEGER, "form_quantity" REAL, "to_currency" INTEGER, "to_quantity" REAL, "precio_unitario" REAL, FOREIGN KEY("from_currency") REFERENCES "cryptos"("symbol"), FOREIGN KEY("to_currency") REFERENCES "cryptos"("symbol"));'
    cur.execute(query)

    todos_movimientos = ("SELECT * FROM movimientos")
    movimientos = cur.execute(todos_movimientos).fetchall()

    if len (movimientos) == 0:
        return render_template("indexnomove.html")
    else:
        query = ("SELECT * FROM movimientos")
        movimientos = cur.execute(query).fetchall()
        conn.close()
        return render_template("index.html", movimientos=movimientos)


@app.route("/purchase", methods= ["GET", "POST"])
def purchase():
    now = datetime.now()
    time = str(now.time())
    time = time[0:8]

    if request.method == "GET":
        return render_template("purchase.html", form=forms)

    else:
        form_data = request.form

        conn = sqlite3.connect("data_base")
        cur = conn.cursor()
        query = "INSERT INTO MOVIMIENTOS (date, time, from_currency, form_quantity, to_currency, to_quantity, unit_price) VALUES (?,?,?,?,?,?,?)";
        data = (str(now.date()), time, request.form.get("from_currency"), request.form.get("form_quantity"), request.form.get("to_currency"), request.form.get("unit_price"))

        cur.execute(query, data)
        conn.commit()
        con.close()

        return redirect(url_for('index'))




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
    return render_template("status.html")
