<h2> <align="center">Machine learning API Deployment using Properties data from ImmoEliza</h1>
<p align="center"><img src="https://immoelissa.be/wp-content/uploads/2021/11/4372580_30803501-1024x682.jpg" width="500" height="400"></p>


## Host organization:
* <a href="https://github.com/becodeorg"><strong>BeCode</strong></a>(Ghent campus)
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200">
  
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

At the end of this challenge, you should :

- Be able to deploy a machine learning model.
- Be able to create a Flask API that can handle a machine learning model.
- Deploy an API to Heroku.

## The Mission

The real estate company "ImmoEliza" is really happy about your data collection using web scrapping. Whenever a new property comes on the market, the question of how it should be priced naturally arises.

Now, the company asks you to create a machine learning model to predict prices on Belgium's real estate sales. "ImmoEliza" has hired you to build a tool that enables the company to predict property prices using linear regression.  

Take the dataset that was previously **scraped** and preprocess the data to be used with machine learning. 

In addition, they would like you to create an API to let their web-developers create a website around it.

Ideally, your API would ask a user to provide with information about a property (features) and return the estimated price using your model.

## Description
Python scripts to scrape from www.immoweb.be for houses and apartments in the market for sale. 
It uses threading and it can be run many times. Ideal is; for a standard pc with 16 GB memory and i7 cpu,  20 threads while scraping properties and 100 urls for each thread.
It takes around 50 minutes for scraping 2000 properties.

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
Gradient-Boosting-Regression model, Flask and  heroku were used for modelling, development and deployment respectively. 

After testing most regression model, Gradient-Boosting-regression seems to have the highest accurary of prediction considered the 3 feature used.  
To cleaning the data; All the NaN, duplicate, text data were handle to my best knowledge.
Exploratory data analaysis and Correlation was perform to have an insight about the datasets. 
For this version, all categorical variables were dropped.

The data was seperated into dependent variable (Price) and independent variable, which are mostly numerical variable(Area, Numbers of Room, and Garden surface).
To train the model, the data was splitted into trained(70%) and test data(30%).

The Flask App was developed based on GET and POST request method. 

The App was deployed to heroku using GitHub.

At the end, an App that can predict the price of house bases on three feature; $Area$, $Numbers of Rooms$ and $Gardens surface$ was developed and deployed.

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
