from flask import Flask, jsonify
import requests, json, datetime
app = Flask(__name__)
@app.route("/banana/meep", methods=["GET"])
def mymethod ():
    token2 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"
    header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token2)}
    hearturl = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json"
    resp = requests.get(hearturl, headers=header).json()
    heart = resp['activities-heart-intraday']['dataset'][-1]
    hearttime = heart["time"]
    now = datetime.datetime.now()
    
    newht = datetime.datetime.strptime(hearttime, "%H:%M:%S")
    diffy = now - newht
    
    diffmins = math.floor(diffy.seconds / 60)
    
    
    heartrate = heart["value"]
    ret = {'heart-rate':heartrate, 'time offset':diffmins}

    return jsonify(ret)

@app.route("/poopy", methods=["GET"])
def mymethod2 ():
    return "Test"


if __name__ == '__main__':
    app.run(debug=True)