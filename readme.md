HYPERPARAMETER TABLE

| Model        | Features           | Training Set Model Score  | Testing Set Model Score | RMSE | Data Types |
| ------------- |:-------------:| -----:| ---: | ---: | ---: | 
Linear Regression | likes | 0.0389 | 0.0388 | 0.4675 | int
Linear Regression | views | 0.0279 | 0.0272 | 0.4703 | int
Linear Regression | running time | 0.0093 | 0.0133 | 0.4737 | int
Linear Regression | likes and views | 0.0409 | 0.0414 | 0.4669 | int 
Linear Regression | likes, views and running time | 0.0539 | 0.0595 | 0.4625 | int
Linear Regression | likes, views, running time, five star | 0.05848 | 0.0578 | 0.4629 | int
Linear Regression | likes, views, running time, year | 0.0683 | 0.0646 | 0.4612 | int and float
Linear Regression | genres | 0.1149 | 0.1145 | 0.4487 | int
Linear Regression | genres, views, likes, running time and year | 0.1656 | 0.1608 | 0.4369 | int and float
Linear Regression | genres, all stars, year, running time, views, likes | 0.2479 | 0.2181 | 0.4217 | int and float
Lasso Regression | views, likes, running time, year, genres | 0.06822 | 0.0648 | 0.4612 | int and float
Lasso Regression | genres, all stars, year, running time, views, likes | 0.1591 | 0.1289 | 0.4450 | int and float
Ridge Regression | genres, all stars, year, running time, views, likes | 0.1656 | 0.1608 | 0.4369 | int and float
Gradient Boosting Regressor | genres, all stars, year, running time, views, likes | 0.9757 | 0.9738 | 0.0772 | int and float
Elastic Net | genres, all stars, year, running time, views, likes | 0.1572 | 0.1273 | 0.4455 | int and float
KNeighbors Regressor | genres, all stars, year, running time, views, likes | 0.9722 | 0.9562 | 0.0998 | int and float
Decision Tree Regressor | genres, all stars, year, running time, views, likes | 1.0 | 0.9707 | 0.0816 | int and float


CONCLUSIONS

>Gradient Boosting Regressor, KNeighbors Regressor and Decision Tree Regressor provide the most accurate predictions on unseen data. Gradient Boosting gives the lowest RMSE (0.0772) and the highest model accuracy score on the testing set (0.9738), with Decision Tree as a close second. 


Past experiments:

directors and ratings
    - linear regression model
    - directors as features and ratings as target variable, 6000 features not helpful for model
    - dimensionality problem, good on directors its seen but not ones it hasn't, too many features


year and ratings
    - linear regression model
    - year as a feature, ratings as target variable
    - little correlation, model score of 0.068

    
    
