<h1 align="center">Machine Learning Model for Housing Price Prediction</h1>

## Authors:
- [Elkin Guerrero](https://github.com/elkinguerrero007)
- [Juan Sebastian Posada](https://github.com/Juansepo13/Juansepo13)

## Abstract
* This project is a machine learning model that predicts the value of a house based on its area, number of bathrooms, and number of bedrooms. The model was trained on a dataset of historical houses and was implemented using TensorFlow and Keras on a Ubuntu backend. In addition, a REST API was provided using Flask to interact with the model and make predictions.


## Description
* This software is a web application that uses Flask as a framework to run templates and allows users to get a quote for a house based on 4 parameters: square meters, number of bedrooms, number of bathrooms, and geographic location (north, south, east, or west).
* The application presents the user with a form where they can enter the aforementioned parameters, and upon clicking a quote button, the application calculates an estimated price for the house. The quote page also displays additional information about the houses, such as photographs and descriptions of the area.
* This application is useful for individuals looking to buy or sell a house and wanting to have an idea of the selling price of a property. By using the parameters entered by the user, the application can generate an accurate quote that helps make informed decisions about the real estate market.

### Overview

* The app.py file is a code file that contains a web application created with Flask. This application has a trained machine learning model that predicts the price of a house based on its features such as area, number of bedrooms, bathrooms, and location.
* The file loads the data, encodes the location using OneHotEncoder, splits the data into training and testing, creates and trains the model, and saves it to a file. It also contains a function to make predictions based on data entered in a web form.
* Additionally, the file contains several URL routes that render different web pages in the application, such as the home page, a blog page, a contact page, a frequently asked questions page, and the privacy and terms and conditions policies.
* Overall, this file is the backbone of the web application and is responsible for handling all user requests and responses, as well as performing house price predictions using the machine learning model.

## Dataset
* The model was trained on a dataset of historical houses which can be found in the "house_data.csv" file. This file contains information about the sale price, area, number of bathrooms, and number of bedrooms of the houses.

## Limitations
* It is important to note that this model has limitations and should not be used as the sole source of information for making real estate investment decisions. Additionally, the model was trained on a historical dataset and cannot predict the effects of external factors, such as economic changes or natural disasters, on the price of a house.

## Future Improvements
* Although this model provides a good estimate of the price of a house based on its features, there are several improvements that could be made in the future, such as the inclusion of more features, the use of regularization techniques to avoid overfitting, and the implementation of a more user-friendly interface

## Requirements
* To use this application, the user needs to have a web browser installed and access to the internet.

| Librery          | Version |
|------------------|--------|
| Flask            | 2.2.2  |
| joblib           | 1.1.1  |
| keras            | 2.11.0 |
| numpy            | 1.24.2 |
| pandas           | 1.3.3  |
| scikit-learn     | 1.2.2  |
| tensorflow       | 2.11.0 |


## Installation
* To install the application, it is recommended to follow these steps:
### Download the files from the GitHub repository.
* Download the files from the [Github repository](https://github.com/elkinguerrero007/flask2/tree/juansepo)
* Install the project dependencies using the command ```pip install -r requirements.txt.```
* Run the application using the command ```flask run```
* Access the quote page in a web browser by entering the address ```http://localhost:5000/cotizar.```

### Usage

* #### To use the application, the user should follow these steps:
* Access the quote page in a web browser by entering the address ```http://127.0.0.1:5000/```
* Enter the house parameters in the quote form.
* Click the quote button. ```Predict Price```
* The application will display the estimated price of the house and other relevant information.

### Contribution
* If you wish to contribute to the project, you can follow these steps:
* ```Fork``` the repository on GitHub.
* Create a ```new branch``` for your changes.
* Make the necessary changes.
* Submit a ```pull request``` from your branch to the ```main branch``` of the repository.
* Wait for your changes to be reviewed and approved by the project collaborators.

- [Elkin Guerrero](https://github.com/elkinguerrero007): implemented the TensorFlow and Keras models, created the Flask API, and wrote the README.md file.
- [Juan Sebastian Posada](https://github.com/Juansepo13/Juansepo13): collected and preprocessed the housing dataset, performed exploratory data analysis, and assisted in the model tuning and realize front-end whith Html,Css and JavaScript. 