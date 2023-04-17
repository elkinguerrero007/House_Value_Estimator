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

