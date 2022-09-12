from flask import Flask
import requests, datetime, math
app = Flask(__name__)

@app.route("/banana/meep", methods=["GET"])
def mymethod ():
    return "Ok"

@app.route("/poopy", methods=["GET"])
def mymethod2 ():
    return "Test"


if __name__ == '__main__':
    app.run(debug=True)