import requests, json

#import initial data set json
json_read = open('uber_demand_prediction_challenge.json')
json_data = json.load(json_read)
json_read.close()

#Learn
url = "http://localhost:5000/learn/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(json_data), headers=headers)



#Load json you want to be predicted
json2_read = open('may_hours.json')
json2_data = json.load(json2_read)
json2_read.close()

#Predict demand from a data set
url = "http://localhost:5000/predict/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(json2_data), headers=headers)
print r.json()
