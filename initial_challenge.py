import parse_and_count
import sklearner
import json, datetime, time
from dateutil import parser
import numpy as np
import csv

#import json
json_read =  open('uber_demand_prediction_challenge.json')
json_data = json.load(json_read)
json_read.close()

#parse data and set up for GLM regressor
datetime_parsed = parse_and_count.parseJson(json_data)
final_matrix = parse_and_count.formatData(datetime_parsed)
vectorizedData = sklearner.vectorizeCategories(final_matrix)

#Create model and learn from initial json data set
learningModel = sklearner.PredictionModel()
vectorizedData = sklearner.vectorizeCategories(final_matrix)
learningModel.learn(vectorizedData)

#load up dates to predict
json_read = open('may_hours.json')
json_data = json.load(json_read)
json_read.close()

#parse data and set up for GLM predictor
datetime_parsed = parse_and_count.parseJson(json_data)
data_to_predict = parse_and_count.formatData(datetime_parsed)
predictionFormatted = sklearner.vectorizeCategories(data_to_predict)
answer_array = learningModel.forecast(datetime_parsed, predictionFormatted)


#export_predictions
output_csv = csv.writer(open('output.csv', 'wb'), delimiter=',') 
output_csv.writerow(['hour', 'demand_prediction'])

for i in answer_array:
	output_csv.writerow(i)
