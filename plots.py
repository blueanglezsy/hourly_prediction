import numpy as np
import matplotlib.pyplot as plt
import json

json_read =  open('uber_demand_prediction_challenge.json')
data = json.load(json_read)

print type(data[1])