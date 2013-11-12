import numpy as np
from sklearn import linear_model
from sklearn.feature_extraction import DictVectorizer


def vectorizeCategories(final_matrix):
	vec = DictVectorizer()
	return (vec.fit_transform(final_matrix).toarray())


class PredictionModel(object):
	def __init__(self):
		self.clf = linear_model.LinearRegression()

	def learn(self, vectorizedData):
		self.X = np.delete(vectorizedData, 24, 1)  # features
		self.y = vectorizedData[:, 24]   # target
		self.clf.fit(self.X, self.y)

	def forecast(self, dateTimeArray, vectorizedArray):
		output_array = []
		prediction_vector = self.clf.predict(np.delete(vectorizedArray, 24,1))
		for i in range(0,len(dateTimeArray)):
			output_array.append(
				[dateTimeArray[i], 
				prediction_vector[i] if prediction_vector[i] >= 0 else 0.0])
		return(output_array)