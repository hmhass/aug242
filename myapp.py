from testapp import *
from flask import Flask
app = Flask(__name__)
@app.route("/banana/meep", methods=["GET"])
def mymethod ():
    ret = get_heart()
    return ret

@app.route("/poopy", methods=["GET"])
def mymethod2 ():
    return "Test"


if __name__ == '__main__':
    app.run(debug=True)