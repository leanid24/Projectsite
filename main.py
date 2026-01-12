from pydoc import render_doc

from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template("test.html")

@app.route('/news')
def news():
  return render_template("news.html")

@app.route('/culture')
def culture():
  return render_template("culture.html")

@app.route('/sports')
def sports():
  return render_template("sports.html")

@app.route('/olympiads')
def olympiads():
  return render_template("olympiads.html")

app.run(debug = True)