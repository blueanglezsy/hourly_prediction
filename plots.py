import numpy as np
import matplotlib.pyplot as plt
import json
from dateutil import parser
from collections import Counter
import datetime, time
import csv

json_read =  open('uber_demand_prediction_challenge.json')
data = json.load(json_read)

datetime_parsed = []
for i in data:
	 datetime_parsed.append(parser.parse(i[:13]))

hourstamps_csv = csv.writer(open('hourstamps.csv', 'wb'), delimiter=',') 
hourstamps_csv.writerow(['hour_stamp'])

"""
for i in datetime_parsed:
	hourstamps_csv.writerow([i,])

print datetime_parsed[0].weekday(), type(datetime_parsed[0].weekday())
print datetime_parsed[0].hour, type(datetime_parsed[0].hour)
print str(datetime_parsed[0])
"""
counted_data_by_hour = Counter(datetime_parsed)

print type(counted_data_by_hour)
print counted_data_by_hour

for i in set(datetime_parsed):
    print '%s : %d' % (i, counted_data_by_hour[i])

"""
def count_unique(keys):
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return uniq_keys, np.bincount(bins)

print count_unique(datetime_parsed)

plt.plot(count_unique(datetime_parsed))


list_of_lists = []
string_times = []
for i in data:
	string_times.append(datetime.time(i))
	splitted = i.split("T")
	list_of_lists.append([splitted[0], int(splitted[1][:2])])
"""
