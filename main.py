from flask import Flask
import os
print(os.getcwd())

app = Flask(__name__)

@app.route("/")
def main():
    f = open("about.html", "r")
    return f.read()

@app.route("/data")
def data():
    k = open("data.html", "r")
    return k.read()

app.run()
