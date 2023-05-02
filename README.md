# Machine Learning Model for Housing Price Prediction

## Authors:
- [Elkin Guerrero](https://github.com/elkinguerrero007)
- [Juan Sebastian Posada](https://github.com/Juansepo13/Juansepo13)

![Home](House_Value_Estimator/home.png)



This project is a machine learning model that predicts the value of a house based on its area, number of bathrooms, and number of bedrooms. The model was trained on a dataset of historical houses and was implemented using TensorFlow and Keras on a Ubuntu backend. In addition, a REST API was provided using Flask to interact with the model and make predictions.

## Installation

To use the model, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Make sure you have Python 3 and the necessary dependencies installed, which are specified in the requirements.txt file. To install the dependencies, you can use the following command in the terminal:

pip install -r requirements.txt

3. Run the Flask API using the following command in the terminal:

python app.py


4. The API will run on http://localhost:5000. You can interact with it through a REST client.


## Usage

To make a housing price prediction, send a POST request to the following URL: http://localhost:5000/predict, with the following parameters in JSON format:


{
  "area": <area value>,
  "bathrooms": <number of bathrooms>,
  "bedrooms": <number of bedrooms>
}


The server will return a JSON response with the estimated price of the house:

## Dataset

The model was trained on a dataset of historical houses which can be found in the "house_data.csv" file. This file contains information about the sale price, area, number of bathrooms, and number of bedrooms of the houses.


## Limitations

It is important to note that this model has limitations and should not be used as the sole source of information for making real estate investment decisions. Additionally, the model was trained on a historical dataset and cannot predict the effects of external factors, such as economic changes or natural disasters, on the price of a house.

## Future Improvements

Although this model provides a good estimate of the price of a house based on its features, there are several improvements that could be made in the future, such as the inclusion of more features, the use of regularization techniques to avoid overfitting, and the implementation of a more user-friendly interface

## Contributors
- [Elkin Guerrero](https://github.com/elkinguerrero007): implemented the TensorFlow and Keras models, created the Flask API, and wrote the README.md file.
- [Juan Sebastian Posada](https://github.com/Juansepo13/Juansepo13): collected and preprocessed the housing dataset, performed exploratory data analysis, and assisted in the model tuning and realize front-end whith Html,Css and JavaScript. 
