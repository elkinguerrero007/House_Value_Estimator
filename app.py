#!/usr/bin/python3
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import joblib
from keras.models import Sequential
from keras.layers import Dense

app = Flask(__name__)


# Cargar datos
data = pd.read_csv('/home/elkin/flask2/house_data.csv')

# Codificar la columna 'ubicacion' utilizando OneHotEncoder
one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit(data[['ubicacion']])
joblib.dump(one_hot_encoder, '/home/elkin/flask2/one_hot_encoder.joblib')
data_encoded = pd.DataFrame(one_hot_encoder.transform(data[['ubicacion']]).toarray())
data = data.join(data_encoded)
data = data.drop(['ubicacion'], axis=1)

# Dividir datos en entrenamiento y prueba
train_data = data.sample(frac=0.8, random_state=0)
test_data = data.drop(train_data.index)

