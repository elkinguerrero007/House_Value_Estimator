#!/usr/bin/python3
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
import joblib

# Cargar datos
data = pd.read_csv('/home/elkin/flask2/house_data.csv')

# Codificar la columna 'ubicacion' utilizando OneHotEncoder
one_hot_encoder = OneHotEncoder()
data_encoded = pd.DataFrame(one_hot_encoder.fit_transform(data[['ubicacion']]).
