HYPERPARAMETER TABLE

put in an excel spreadsheet for now, test and training set accuracy (choose the metric)

paste in proposal intro

directors and ratings
    - directors as features and ratings as target variable, 6000 features not helpful for model
    - dimensionality problem, good on directors its seen but not ones it hasn't, too many features
    - feature variable is director, float variable is avg_rating
    - linear regression model

year and ratings
    - year as a feature, ratings as target variable
    - some correlation, model score of 0.068
    - year and avg_ratings are both floats
    - linear regression model
    
genre and ratings
    - genre is a feature, ratings is a target variable
    - fairly accurate with a standard error of ~0.445
    - genre is a feature variable, avg_rating is a float
    - linear regression model

    

PROCESS

data cleaning - dealing with NaN and corruption of data

data wrangling - combining dataframes into one table

feature engineering - creating a new feature (get_dummies for new genres)

modelling - keep modelling features along the way

conclude with interesting predictive results 