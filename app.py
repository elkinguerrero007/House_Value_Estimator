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

# Separar las características de las etiquetas
train_features = train_data.drop(['price'], axis=1)
train_labels = train_data['price']
test_features = test_data.drop(['price'], axis=1)
test_labels = test_data['price']

# Crear modelo
model = Sequential()
model.add(Dense(1, input_dim=7, activation='linear'))


# Compilar modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenar modelo
model.fit(train_features, train_labels, epochs=18000, batch_size=5)

# Guardar modelo entrenado
joblib.dump(model, '/home/elkin/flask2/model.joblib')


# Cargar objeto OneHotEncoder
one_hot_encoder = joblib.load('/home/elkin/flask2/one_hot_encoder.joblib')
# Cargar modelo entrenado
model = joblib.load('/home/elkin/flask2/model.joblib')

# Función para hacer predicciones
def make_prediction(area, num_habitaciones, num_banos, ubicacion):
    # Codificar la ubicación
    encoded_location = one_hot_encoder.transform([[ubicacion]]).toarray()
    # Crear arreglo con los datos ingresados en el formulario y la ubicación codificada
    data = np.array([[area, num_habitaciones, num_banos] + encoded_location[0].tolist()])
    # Hacer predicción
    prediction = model.predict(data)
    return prediction[0][0]
