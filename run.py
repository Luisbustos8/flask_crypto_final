from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import sqlite3


@app.route("/")
def index():

    data_base = "./data/movimientos.db"

    try:   
        conn = sqlite3.connect(data_base)
        cur = conn.cursor()

        query = "SELECT * FROM movimientos;"
        movimientos = cur.execute(query).fetchall()
        print(movimientos)

        if movimientos[0] == None:
            return "No hay movimientos"
        else:
            conn.close()
            return render_template("index.html", movimientos=movimientos)
            
    except:
        return render_template("index.html")
   


@app.route("/purchase")
def purchase():
    return "Aquí ira la compra de cryptos"
