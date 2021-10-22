HYPERPARAMETER TABLE

| Model        | Features           | Training Set Model Score  | Testing Set Model Score | RMSE | Data Types |
| ------------- |:-------------:| -----:| ---: | ---: | ---: | 
Linear Regression | likes | 0.0389 | 0.0388 | 0.4675 | int
Linear Regression | views | 0.0279 | 0.0272 | 0.4703 | int
Linear Regression | running time | 0.0093 | 0.0133 | 0.4737 | int
Linear Regression | animation | 0.0693 | 0.0693 | 0.4691 | int 
Linear Regression | animation, thriller, horror, scifi, war | 0.1149 | 0.1145 | 0.4487 | int
Linear Regression | year, running time, animation, thriller, horror, scifi, war | 0.1236 | 0.1175 | 0.4479 | int and float
Lasso Regression | year, running time, animation, thriller, horror, scifi, war | 0.0232 | 0.0183 | 0.4725 | int and float
Ridge Regression | year, running time, animation, thriller, horror, scifi, war | 0.1236 | 0.1175 | 0.4479 | int and float
Elastic Net Regression | year, running time, animation, thriller, horror, scifi, war | 0.0222 | 0.0183 | 0.4725 | int and float
Decision Tree Regression | year, running time, animation, thriller, horror, scifi, war | 0.6386 | -0.0172 | 0.4809 | int and float
KNeighbors Regression | year, running time, animation, thriller, horror, scifi, war | 0.4259 | 0.1976 | 0.4272 | int and float
Gradient Boosting Regression | year, running time, animation, thriller, horror, scifi, war | 0.3129 | 0.3025 | 0.3982 | int and float
Linear Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.1249 | 0.1186 | 0.3979 | int and float
Lasso Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.0302 | 0.0242 | 0.4711 | int and float
Ridge Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.1249 | 0.1186 | 0.4477 | int and float
Elastic Net Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.0223 | 0.0183 | 0.4725 | int and float
Decision Tree Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.9520 | -0.3295 | 0.5499 | int and float
KNeighbors Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.4791 | 0.2082 | 0.4243 | int and float
Gradient Boosting Regression | title length, year, running time, animation, thriller, horror, scifi, war | 0.3166 | 0.3037 | 0.3979 | int and float


CONCLUSIONS

>Gradient Boosting Regression, KNeighbors Regression and Linear Regression provide the most accurate predictions on unseen data. Gradient Boosting gives the lowest RMSE (0.3979) and the highest model accuracy score on the testing set (0.3166). 





    
    
