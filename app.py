#!/usr/bin/python3
# Importar librerias
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

# Cargar datos
data = pd.read_csv('/home/elkin/house_data/house_data.csv')

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
model.add(Dense(1, input_dim=4, activation='linear'))

# Compilar modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenar modelo
model.fit(train_features, train_labels, epochs=50, batch_size=10)

# Evaluar modelo
test_loss = model.evaluate(test_features, test_labels)
print(f"El error cuadrático medio en el conjunto de prueba es de: {test_loss}")

# Hacer predicciones
new_data = np.array([[2000, 3, 2, 1]]) # Ejemplo de nueva casa
prediction = model.predict(new_data)
print(f"La casa de ejemplo tiene un valor estimado de: {prediction}")
