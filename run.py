from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import sqlite3


@app.route("/")
def index():

    data_base = "./data/movimientos.db"

 
    conn = sqlite3.connect("data_base")
    cur = conn.cursor()

    query = 'CREATE TABLE IF NOT EXISTS "movimientos"("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "date" TEXT, "time" TEXT, "from_currency" INTEGER, "from_quantity" REAL, "to_currency" INTEGER, "to_quantity" REAL, "unit_price" REAL, FOREIGN KEY("from_currency") REFERENCES "cryptos"("symbol"), FOREIGN KEY("to_currency") REFERENCES "cryptos"("symbol"));'
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
            
   


@app.route("/purchase")
def purchase():
    return "Aquí ira la compra de cryptos"
