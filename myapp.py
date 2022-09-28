from pymongo import MongoClient
from flask import Flask, request, json
import requests, datetime, math
app = Flask(__name__)

@app.route("/heartrate/last", methods=["GET"])
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
    ret = {'heart-rate':heartrate, 'time offset':diffmins-240}
    return ret

@app.route("/steps/last", methods=["GET"])
def mymethod2 ():
    token2 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"
    header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token2)}
    stepurl = "https://api.fitbit.com/1/user/-/activities/date/today.json"
    acturl = "https://api.fitbit.com/1/user/-/activities/calories/date/today/1d/15min.json"
    stepresp = requests.get(stepurl, headers=header).json()
    actresp = requests.get(acturl, headers=header).json()
    steps = stepresp["summary"]["steps"]
    distance = stepresp["summary"]["distances"][0]["distance"]
    time = actresp["activities-calories-intraday"]["dataset"][-1]["time"]
    now = datetime.datetime.now()
    newt = datetime.datetime.strptime(time, "%H:%M:%S")
    diffy = now - newt
    diffmins = math.floor(diffy.seconds / 60)
    ret = {'step-count':steps,'distance':distance, 'time offset':diffmins-240}
    return ret

@app.route("/sleep/<date>")
def sleep(date):
    token2 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"
    token3 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"
    header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token3)}
    sleepurl = "https://api.fitbit.com/1.2/user/-/sleep/date/" + date + ".json"
    sleepresp = requests.get(sleepurl, headers=header).json()

    if sleepresp["sleep"] == []:
        return("No sleep record for this date")
    else:
        deep = sleepresp["summary"]["stages"]["deep"]
        light = sleepresp["summary"]["stages"]["light"]
        rem = sleepresp["summary"]["stages"]["rem"]
        wake = sleepresp["summary"]["stages"]["wake"]
        ret = {'deep': deep, 'light': light, 'rem': rem, 'wake': wake}
        return ret

@app.route("/activity/<date>")
def act(date):
    token2 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"
    token3 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"
    header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token2)}
    acturl = "https://api.fitbit.com/1/user/-/activities/date/" + date + ".json"
    actresp = requests.get(acturl, headers=header).json()

    very = str(actresp["summary"]["veryActiveMinutes"])
    light = str(actresp["summary"]["lightlyActiveMinutes"])
    sed = str(actresp["summary"]["sedentaryMinutes"])

    ret = {'very-active': very, 'lightly-active': light, 'sedentary': sed}
    return ret

@app.route("/sensors/env", methods=["GET"])
def mymethod3 ():
    client = MongoClient("mongodb+srv://hmhassell:poopybutt@cluster0.ocm571a.mongodb.net/?retryWrites=true&w=majority")
    db = client["myenvdb"]
    rowy = db.environmental.find().limit(1)
    temp = rowy[0].get("temp")
    hum = rowy[0].get("humidity")
    time = rowy[0].get("timestamp")
    ret = {"temp": temp, "humidity": hum, "timestamp":time}
    return ret
    
@app.route("/sensors/pose", methods=["GET"])
def mymethod4 ():
    client = MongoClient("mongodb+srv://hmhassell:poopybutt@cluster0.ocm571a.mongodb.net/?retryWrites=true&w=majority")
    db = client["myenvdb"]
    rowy = db.pose.find().limit(1)
    pres = rowy[0].get("presence")
    pose = rowy[0].get("pose")
    time = rowy[0].get("timestamp")
    ret = {"presence": pres, "pose": pose, "timestamp":time}
    return ret

@app.route('/post/pose', methods=['POST'])
def mymethod5 ():
    data = request.data
    input = json.loads(data)
    client = MongoClient("mongodb+srv://hmhassell:poopybutt@cluster0.ocm571a.mongodb.net/?retryWrites=true&w=majority")
    db = client["myenvdb"]
    db.pose.insert_one(input)
    ret = {"success":"yes"}
    return ret

@app.route('/post/env', methods=['POST'])
def mymethod6 ():
    data = request.data
    input = json.loads(data)
    client = MongoClient("mongodb+srv://hmhassell:poopybutt@cluster0.ocm571a.mongodb.net/?retryWrites=true&w=majority")
    db = client["myenvdb"]
    db.environmental.insert_one(input)
    ret = {"success":"yes"}
    return ret

    


if __name__ == '__main__':
    app.run(debug=True)