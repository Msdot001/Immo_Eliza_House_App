# import necessary libararies
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics


def train(X_train, y_train):
    #Fitting the  Regression model
    model = GradientBoostingRegressor(random_state=0)
    model.fit(X_train, y_train)
    return model


def predict(model,X_test):
    """This function aim at using the model trained to make prediction on the test data """
    Price_predicted = model.predict(X_test)
    return Price_predicted 

def model_evaluation(model,x,y,Price_predicted,y_test):
    meanAbErr = metrics.mean_absolute_error(y_test, Price_predicted)
    meanSqErr = metrics.mean_squared_error(y_test, Price_predicted)
    rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, Price_predicted))

    print('R squared: {:.2f}'.format(model.score(x,y)*100))
    print('Mean Absolute Error:', meanAbErr)
    print('Mean Square Error:', meanSqErr)
    print('Root Mean Square Error:', rootMeanSqErr)


def save_model(model):
    """loading model to API"""
    return pickle.dump(model,open('model.pkl','wb'))

cleandata_path = r"../Data/cleandata.csv"
data = pd.read_csv(cleandata_path)
# Splitting the data into dependent and independent variable
x = data[['Area', 'Number_of_Rooms','Garden surface']]      
y = data['Price']

# Splitting the data trained and test 
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
y_test = y_test.values.ravel()
y_train = y_train.values.ravel()

model = train(X_train, y_train)
y_pred = predict(model,X_test)







