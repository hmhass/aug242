import requests, pprint, datetime

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhRS0QiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkxMDQxNzA4LCJpYXQiOjE2NTk1MDU3MDh9.NzxJB3FZxmWDyJx44pvUZOCkqME50heLRhYWD19z1go"
token2 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSRFQiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBycHJvIHJudXQgcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkzNDg4MDQxLCJpYXQiOjE2NjE5NTIwNDF9.uk4UyLwyQeLjnoE6jxKPNCxfkzs0mFTq_09cfuyV74U"
acturl = "https://api.fitbit.com/1/user/-/activities/date/2022-08-02.json"
header = {'Accept' : 'application/json', 'Authorization' : 'Bearer {}'.format(token2)}
hearturl = "https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json"

#summ = resp["summary"]
#print("You walked {} steps today.".format(summ["steps"]))

def get_heart():
    resp = requests.get(hearturl, headers=header).json()
    heart = resp['activities-heart-intraday']['dataset'][-1]
    hearttime = heart["time"]
    
    
    heartr8 = heart["value"]

    return(heart)

def time_diffy():
    #now = datetime.now().strftime("%H:%M:%S")
    test = "13:26:00"
    early = "12:24:00"
    timedt = datetime.datetime.strptime(test, "%H:%M:%S")
    timeea = datetime.datetime.strptime(early, "%H:%M:%S")
    #c = timedt - timeea
    #mins = c.total_seconds() / 60
    print(timedt)
    print(timeea)
    return(timedt-timeea)

    
poop = get_heart()
print(poop)
