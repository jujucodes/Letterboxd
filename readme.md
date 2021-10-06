HYPERPARAMETER TABLE

| Model        | Features           | Training Set Model Score  | Testing Set Model Score | RMSE | Data Types |
| ------------- |:-------------:| -----:| ---: | ---: | ---: | 
Linear Regression | likes | model score: 0.0389 | model score: 0.0388 | rmse:0.4675 | int
Linear Regression | views | model score: 0.0279 | model score: 0.0272 | rmse: 0.4703 | int
Linear Regression | running time | model score: 0.0093 | model score: 0.0133 | rmse: 0.4737 | int
Linear Regression | likes and views | model score: 0.0409 | model score: 0.0414 | rmse: 0.4669 | int 
Linear Regression | likes, views and running time | model score: 0.0539 | model score: 0.0595 | rmse: 0.4625 | int
Linear Regression | likes, views, running time, five star | model score: 0.05848 | model score: 0.0578 | rmse: 0.4629 | int
Linear Regression | likes, views, running time, year | model score: 0.0683 | model score: 0.0646 | rmse: 0.4612 | int and float
Linear Regression | genres | model score: 0.1149 | model score: 0.1145 | rmse: 0.4487 | int
Linear Regression | genres, views, likes, running time and year | model score: 0.1656 | model score: 0.1608 | rmse: 0.4369 | int and float
Linear Regression | genres, all stars, year, running time, views, likes | model score: 0.2479 | model score: 0.2181 | rmse: 0.4217 | int and float
Lasso Regression | views, likes, running time, year, genres | model score: 0.06822 | model score: 0.0648 | rmse: 0.4612 | int and float
Lasso Regression | genres, all stars, year, running time, views, likes | model score: 0.1591 | model score: 0.1289 | rmse: 0.4450 | int and float
Ridge Regression | genres, all stars, year, running time, views, likes | model score: 0.1656 | model score: 0.1608 | rmse: 0.4369 | int and float
Gradient Boosting Regressor | genres, all stars, year, running time, views, likes | model score: 0.9757 | model score: 0.9738 | rmse: 0.0772 | int and float
Elastic Net | genres, all stars, year, running time, views, likes | model score: 0.1572 | model score: 0.1273 |  rmse: 0.4455 | int and float
Kneighbors Regressor | genres, all stars, year, running time, views, likes | model score: 0.9722 | model score: 0.9562 | rmse: 0.0998 | int and float
Decision Tree Regressor | genres, all stars, year, running time, views, likes | model score: 1.0 | model score: 0.9707 | rmse: 0.0816 | int and float

experiments:

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
    
