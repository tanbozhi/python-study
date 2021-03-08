# coding=utf-8

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index/index.html")

@app.route("/log")
def login():
    return render_template("index/login.html")

@app.route("/reg")
def register():
    return render_template("index/register.html")