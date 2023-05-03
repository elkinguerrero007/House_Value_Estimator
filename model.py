from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import joblib

# Cargar los datos
boston = load_boston()
X = boston.data
y = boston.target

# Crear el modelo
model = LinearRegression()
model.fit(X, y)

# Guardar el modelo
joblib.dump(model, 'model.joblib')
