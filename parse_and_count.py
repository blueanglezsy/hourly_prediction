
import json, datetime, time
from dateutil import parser
from collections import Counter
import numpy as np
from sklearn import linear_model
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer
import csv

#import json
json_read =  open('uber_demand_prediction_challenge.json')
json_data = json.load(json_read)
json_read.close()

#parse json into a list of datetime objects while stripping away elements after hour
datetime_parsed = []
for i in json_data:
	 datetime_parsed.append(parser.parse(i[:13]))

#create a dictionary of datetime:frequency and then load into final matrix

counted_data_by_hour = dict(Counter(datetime_parsed))



final_matrix = []
for i in sorted(counted_data_by_hour.keys()):
	final_matrix.append({'weekday':str(i.weekday()), 
						'hour':str(i.hour), 
						'rides':counted_data_by_hour[i],
						'weeknumber':i.isocalendar()[1]})


vec = DictVectorizer()
data = vec.fit_transform(final_matrix).toarray()

print final_matrix[0]
print data[0]


#X = data[:, -24]
X = np.delete(data, 24, 1)  # features
y = data[:, 24]   # target

print final_matrix[0]
print data[0]
print "x0= ", X[0], "y0= ", y[0]
print type(data)


#clf = tree.DecisionTreeRegressor()
clf = linear_model.LinearRegression()
clf.fit(X, y)

output_csv = csv.writer(open('output.csv', 'wb'), delimiter=',') 
output_csv.writerow(['hour', 'actual', 'predictions'])

for i in range(0,len(y)):
	output_csv.writerow([sorted(counted_data_by_hour.keys())[i], 
		y[i], 
		clf.predict(X[i]) if clf.predict(X[i]) >= 0 else 0 ])




