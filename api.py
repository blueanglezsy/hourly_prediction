#!flask/bin/python
from flask import Flask, jsonify, request

import parse_and_count
import sklearner
import json, datetime, time
from dateutil import parser
import numpy as np


app = Flask(__name__)

#import initial data set json
json_read =  open('uber_demand_prediction_challenge.json')
json_data = json.load(json_read)
json_read.close()

final_matrix = []
learningModel = sklearner.PredictionModel()

def addToDb(json_format_data):
    datetime_parsed = parse_and_count.parseJson(json_format_data)
    output_matrix = parse_and_count.formatData(datetime_parsed)
    return (output_matrix)

def learn(input_matrix):
    #learn from initial json data set
    vectorizedData = sklearner.vectorizeCategories(input_matrix)
    learningModel.learn(vectorizedData)


#GET entire database if you want
@app.route('/all_data/', methods = ['GET'])
def get_timestamps():
    return jsonify( { 'Data Evaluated': final_matrix } )

#POST new data to learn
@app.route('/learn/', methods = ['POST'])
def create_timestamps():
    if not request.json:
        abort(400)
    timestamps = request.json
    input_matrix = addToDb(timestamps) 
    for i in input_matrix:
        final_matrix.append(i)
    learn(final_matrix)
    return jsonify( { 'posted': timestamps } ), 201

#POST input to learn from and return 
@app.route('/predict/', methods = ['POST'])
def predict_timestamps():
    if not request.json:
        abort(400)
    timestamps = request.json
    datetime_parsed = parse_and_count.parseJson(timestamps)
    data_to_predict = parse_and_count.formatData(datetime_parsed)
    predictionFormatted = sklearner.vectorizeCategories(data_to_predict)
    answer_array = learningModel.forecast(datetime_parsed, predictionFormatted)
    return  jsonify( {'date': answer_array[:], 'rides':answer_array[:]} ), 201


if __name__ == '__main__':
    app.run(debug = True)

