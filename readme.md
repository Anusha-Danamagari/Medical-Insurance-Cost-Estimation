Medical Insurance Cost Estimation



Goal: Estimating the  medical insurance cost of person by age, sex, bmi, smoking,etc.



Task:

* Collecting the dataset from the Kaggle (https://www.kaggle.com/datasets/mirichoi0218/insurance)
* Loading the dataset
* Data cleaning(like removing null values, checking the column names and data types, etc.)

&nbsp;Exploratory Data Analysis\[EDA]:

* Univariate analysis: Which means examining the distribution or frequency of individual variables(one at a time)
* Creating a histogram to show a numerical variable
* Next, Bivariate analysis which means analyzing the relationship between two variables for example, how charges are related to smoker, bmi, or age.
* Then correlation analysis using a heatmap, which helps to understand how numerical variables are related each other.



After the analysis of the data we are building the model with the Random Forest Regressor.



1. Preparing the features and target
2. We are splitting the data int test data and train data.
3. Initializing and training the model by using random forest regressor.
4. Making the predictions(predicting the target values usin the features from the test set.
5. Evaluating the model by mean absolute error(mae), mean squared error(mse),rmse(root mean squared error) and r2 (R-squared)

mae- average of absolute differences between predicted and actual values.

mse-average of squared differences between predicted and actual values.

rsme- square root of mse , gives error in original units.

r2-tells how well the model explains the variability in the target.

6\. Finaly, executing the results.

Results:

Random Forest Regressor Performance:

MAE:  2550.67

MSE:  20955694.24

RMSE: 4577.74

R²:   0.87



After the model building we are doing model interpretation .

&nbsp;The model interpretation is the process of understanding how and why a machine learning model makes its predictions.



In this project, model interpretation helps understand which features (like age, bmi, smoker) are driving insurance charges.





And Finally we are importing python library(joblib) which is used in python to save and load machine learning models efficiently.

We will save the file because to reuse it later, deploy it in a web page or API and share the models.











&nbsp;

