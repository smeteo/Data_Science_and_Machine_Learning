# Credit Card Transaction Fraud Dection Capstone Project - Supervised Classification

The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where it has 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

|Feature | Description|
|---|---|
|Time: |This feature contains the seconds elapsed between each transaction and the first transaction in the dataset.|
|Amount:| This feature is the transaction Amount, can be used for example-dependant cost-senstive learning.|
|Class: |This feature is the target variable and it takes value 1 in case of fraud and 0 otherwise.|


#### 1. Exploratory Data Analysis & Data Cleaning  
Import Modules, Load Data & Data Review  
Exploratory Data Analysis  

<img src='Class_Dist.PNG'>  

<img src='Corr_Class.PNG'>  

Data Cleaning  
#### 2. Data Preprocessing  
Scaling  
Train - Test Split  
#### 3. Model Building  
Logistic Regression without SMOTE  

<img src='Class_Rep.PNG'>  

Apply SMOTE  
Logistic Regression with SMOTE  
Random Forest Classifier with SMOTE  

<img src='Confusion.PNG'>  

<img src='Pre_Rec.PNG'>  

<img src='RF_Feature.PNG'>  

Neural Network  

<img src='NN.PNG'>  

Comparison of Models

<img src='Comparison.PNG'>  

####  4. Model Deployement   

Save and Export the Model as .pkl   
Save and Export Variables as .pkl   