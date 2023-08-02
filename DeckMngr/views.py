from flask import render_template, request
from DeckMngr import app


@app.route("/")
def index():
    return "index!"


@app.route("/test1")
def test1():
    send_dict = {
        "send_data1": "send1です。",
        "send_data2": "send2です。",
    }
    return render_template("DeckMngr/test1.html", send_dict=send_dict)
