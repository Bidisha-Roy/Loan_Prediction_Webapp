# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:31:24 2022

@author: user
"""

import numpy as np
import pickle
# loading the saved model
loaded_model = pickle.load(open('D:/loan_stream/trained_model.sav', 'rb'))

input_data = (1, 0 ,0 ,1  ,0  , 6000,0.0 ,141.0 ,360.0 ,1.0 ,2)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not eligibale for loan')
else:
  print('The person is eligable for loan')