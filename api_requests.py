import requests, json

#import initial data set json
json_read = open('may_hours.json')
json_data = json.load(json_read)
json_read.close()



# predict demand from a data set
url = "http://localhost:5000/predict/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(json_data), headers=headers)
print r.text
