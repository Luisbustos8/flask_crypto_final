from my_app import app
from flask import render_template


@app.route("/")
def index():
    return "Aquí irán mis movimientos"