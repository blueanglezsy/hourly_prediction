#!flask/bin/python
from flask import Flask, jsonify, request

import parse_and_count
import sklearner
import json, datetime, time
from dateutil import parser
import numpy as np
import csv

app = Flask(__name__)

#import initial data set json
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

#GET entire database if you want
@app.route('/hourly/api/', methods = ['GET'])
def get_timestamps():
    return jsonify( { 'Data Evaluated': json_data } )

#POST new data to learn
@app.route('/learn/', methods = ['POST'])
def create_timestamps():
    if not request.json:
        abort(400)
    timestamp = request.json
    json_data.append(timestamp)
    return jsonify( { 'posted': timestamp } ), 201

#POST input to learn from and return 
@app.route('/predict/', methods = ['POST'])
def predict_timestamps():
    if not request.json:
        abort(400)
    datetime_parsed = parse_and_count.parseJson(request.json)
    data_to_predict = parse_and_count.formatData(datetime_parsed)
    predictionFormatted = sklearner.vectorizeCategories(data_to_predict)
    answer_array = learningModel.forecast(datetime_parsed, predictionFormatted)
    return  jsonify( {'data': answer_array} ), 201




if __name__ == '__main__':
    app.run(debug = True)

