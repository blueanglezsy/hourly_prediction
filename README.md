hourly_prediction
=================

Uber Challenge

Required Packages:
numpy
scipy
scikit-learn
Flask


Module Description:

sklearner.py = Defines the ML learning model, and uses the scikit-learn methods to vectorize categorical data to be processed, and also models and predicts future data.

parse_and_count.py = Houses functions to parse json, recognize date-time, and count frequency


For an example of using the modules directly, see initial_challenge.py. This learns & models from the initial data set, ‘uber_demand_prediction_challenge.json’ and then utilizes the ‘forecast’ function of the sklearner.py module. The output is then easily written to a csv, under ‘#export_predictions’.

api.py = A VERY simple Flask app that utilizes the above modules for three specific HTTP functions:

/all_data/
GET all data that is in the database ready to be learned by the model. 

/learn/
POST a simple json collection of timestamps to be learned into the model. Keep in mind the model starts with no data so use this request to initially set up the model.

/predict/
POST a simple json collection of timestamps to get the predicted amount of rides during the hour of the timestamp.


api_requests.py = An implementation of initial_challenge.py that uses the running api to pass in data to learn and then data to predict. Utilizes ‘requests’ module but the same can be done directly in cURL
