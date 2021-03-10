# coding=utf-8

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",newslist=newslists)


newslists=[
    {"title":"热点狙击","intro":"总书记的教育观"},
    {"title":"热点狙击","intro":"张伯礼说明年开春有望摘口罩"},
    {"title":"热点狙击","intro":"最高检点名辣笔小球"},
    {"title":"热点狙击","intro":"建议遗弃宠物纳入征信记录"},
    {"title":"热点狙击","intro":"东风快递的工作餐"}
]

@app.route("/log")
def login():
    return render_template("login.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.context_processor
def username():
    username="小博"
    return {"username":username}