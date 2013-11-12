
import json, datetime, time
from dateutil import parser
from collections import Counter
import numpy as np




#parse json into a list of datetime objects while stripping away elements after hour
def parseJson(json_data):
	datetime_parsed = []
	for i in json_data:
		datetime_parsed.append(parser.parse(i[:13]))
	return(datetime_parsed)

#create a dictionary of datetime:frequency and then load into final matrix
def formatData(datetime_parsed):
	final_matrix = []
	counted_data_by_hour = dict(Counter(datetime_parsed))
	for i in sorted(counted_data_by_hour.keys()):
		final_matrix.append({'weekday':str(i.weekday()), 
							'hour':str(i.hour), 
							'rides':counted_data_by_hour[i],
							'weeknumber':i.isocalendar()[1]})
	return final_matrix


