<h2> <align="center">Machine learning API Deployment using Properties data from ImmoEliza</h1>
<p align="center"><img src="https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"></p>


## Host organization:
* <a href="https://github.com/becodeorg"><strong>BeCode</strong></a>(Ghent campus)
<p align="center"><img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></p>
  
## Project Pipeline:
* <a><strong>Pipeline for Deploying Machine Learning</strong></a>
<p align="center"><img src="https://miro.medium.com/max/1400/0*BxqrsN_OjKUk6nr8.png" alt="Logo" width="600" height="300"></p>

# Project Overview

- Repository: `Machine-learning-API-Deployment`
- Type of Challenge: `Learning`
- Duration: `6 days`
- Deadline: `05/06/2022 12:30 PM`
- Presentation: `05/06/2022 1:30 PM`
- Team challenge : 'Solo project'
- Developer : [`Moshood Owolabi`](https://www.linkedin.com/in/moshood-owolabi)
- Level: `Junior Developer`
- Organization: `Becode  AI Bootcamp`


## Learning objectives

This challenge is designed to help you learn how to deploy a machine learning model using Flask API and Heroku. By the end of this challenge, you should be able to deploy a machine learning model, create a Flask API that can handle the model, and deploy the API to Heroku.

- Understand how to deploy a machine learning model.
- Learn how to create a Flask API that can handle a machine learning model.
- Deploy an API to Heroku.

## The Mission

The real estate company "ImmoEliza" is really happy about your data collection using web scrapping. Whenever a new property comes on the market, the question of how it should be priced naturally arises.

Now, the company asks you to create a machine learning model to predict prices on Belgium's real estate sales. "ImmoEliza" has hired you to build a tool that enables the company to predict property prices using linear regression.  

Take the dataset that was previously **scraped** and preprocess the data to be used with machine learning. 

In addition, they would like you to create an API to let their web-developers create a website around it.

Ideally, your API would ask a user to provide with information about a property (features) and return the estimated price using your model.

## Description
The purpose of this report is to document the development of a Python web scraping project that was completed as a solo project. The project involved creating a script to scrape data from www.immoweb.be for houses and apartments that are on the market for sale.

### Methodology:
The project was completed using Python, and threading was implemented to enable the script to gather data quickly and efficiently. The recommended setup for the script was to use 20 threads on a standard PC with 16 GB memory and an i7 CPU. The script was designed to handle up to 100 URLs for each thread, which allowed it to gather data on up to 2000 properties in approximately 50 minutes.

### Input

The input of current API is:


```json
{
  "data": {
    "area": int,
    "rooms-number": int,
    "garden-area": int,
  }
}


Subsequent version would include additional input such as:
{
  "data": {
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "zip-code": int,
    "garden": bool,
    "garden-area": int,
    "equipped-kitchen": bool,
    "full-address": str,
    "swimming-pool": bool,
    "furnished": bool,
    "open-fire": bool,
    "terrace": bool,
    "terrace-area": int,
    "facades-number": int,
    "building-state": 
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
  }
}
```


## Repo Architecture 

```
│   README.md                     : This file
│   Data                          : contains 2 csv file
│   Preprocessing                 : conatins cleaning_data.py. 
|   Model                         : contains prediction.py.
|   template                      : contains index.html.
|   static                        : contains style.css.
|   app.py                        : Script used to create a Flask App.
|   requirements.txt              : Libraries needed to runs this App.
│___   
|    Data
|   | data2.csv                   : csv file containing the data from immoweb.
|   | cleandata.csv               : csv file containing the data after preprocessing.
|___  
|   Preprocessing      
│   │ cleaning_data.py            : Script to preprocess the data receive to predict a new price
│___   
|   Model
│   │ prediction.py               : Script used to predict a new house's price.          
│___  
|    template
│   | index.html                  : Script used to get users input for the prediction.
|___
|   static
│   │ style.css                   : Script used for styling the App webpage.          
```

## Details
This report outlines my solo project on developing and deploying a Gradient-Boosting-Regression model using Flask and Heroku. After testing various regression models, Gradient-Boosting-Regression was found to have the highest accuracy of prediction, considering the three features used in the model.

To ensure the data was cleaned and handled accurately, NaN, duplicate, and text data were removed. Exploratory data analysis and correlation analysis were performed to gain insight into the dataset. For this version, categorical variables were dropped.

The data was separated into the dependent variable (Price) and independent variables (Area, Number of Rooms, and Garden Surface). To train the model, the data was split into 70% training and 30% test data.

The Flask app was developed using GET and POST request methods. The app allows users to predict the price of a house based on three features.

The app was deployed to Heroku using GitHub, and is now accessible to users.

Overall, this project demonstrates my ability to develop and deploy a machine learning model using Flask and Heroku. The resulting app provides a valuable tool for predicting the price of a house, based on key features.

## Used Language and Libraries:
Python libraries:
* Numpy
* Pandas 
* Scikit-learn
* Flask
* Gunicorn

GitHub

Heroku

## Installation & Usage
For Installation and Usage of this project, follow the steps below:

- Clone the repository to your local machine.
- Navigate to the Preprocessing directory in your terminal.
- Run the cleaning_data.py script to clean the data. A new CSV file will be generated.
- Navigate to the Model directory.
- Run the prediction.py script with the URL of the new CSV file generated in step 3. This will generate the model.pkl file.
- Navigate back to the root directory of the project.
- Run the app.py script to start the Flask app.
- Once the app is running, copy the URL generated and paste it into the browser of your choice to access the app.

These steps will ensure that the data is cleaned and the model is trained before the app is launched. Once the app is running, users can input data and receive a predicted price for a house based on key features.


To run execute below commands

      clone the repository.
      cd Preprocessing. 
      Run cleaning_data.py : "New csv file will be generated"
      cd.. and cd  Model
      Run prediction.py with url of the new csv file generated
      "model.pkl" will be generated.
      cd..
      Run app.py
      copy the html generate to browser of your choice. 
