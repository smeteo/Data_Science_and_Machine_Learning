# RFM Customer Segmentation and Cohort Analysis Capstone Project

[Online Retail dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail) from the University of Colombia UCI Machine Learning Repository used for Exploratory Data Analysis, Customer Segmentation, RFM Analysis, K-Means Clustering and Cohort Analysis.  
This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.


Feature Information:

InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.
StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
Description: Product (item) name. Nominal.
Quantity: The quantities of each product (item) per transaction. Numeric.
InvoiceDate: Invoice Date and time. Numeric, the day and time when each transaction was generated.
UnitPrice: Unit price. Numeric, Product price per unit in sterling.
CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
Country: Country name. Nominal, the name of the country where each customer resides


### Project Structure  
Data Cleaning & Exploratory Data Analysis  
RFM Analysis  
Customer Segmentation  
Applying K-Means Clustering  
Create Cohort and Conduct Cohort Analysis  


## Project Steps in Detail
### 1. Data Cleaning & Exploratory Data Analysis  
Import Modules, Load Data & Data Review  
Follow the Steps Below  

i. Take a look at relationships between InvoiceNo, Quantity and UnitPrice columns.  

ii. What does the letter "C" in the invoiceno column mean?  

iii. Handling Missing Values  

iv. Clean the Data from the Noise and Missing Values  

v. Explore the Orders  

<img src='Country.PNG'>

vi. Explore Customers by Country  

vii. Explore the UK Market  


### 2. RFM Analysis  
Follow the steps below  

i. Import Libraries  

ii. Review "df_uk" DataFrame (the df_uk what you create at the end of the Task 1)  

iii. Calculate Recency  

iv. Calculate Frequency  

v. Calculate Monetary Values  

vi. Create RFM Table  

<img src='RFM_Scores.PNG'>  

### 3. Customer Segmentation with RFM Scores  
Calculate RFM Scoring  

i. Creating the RFM Segmentation Table  

Plot RFM Segments  

<img src='Cluster.PNG'>  

<img src='Boxplots.PNG'>  

### 4. Applying K-Means Clustering  
Data Pre-Processing and Exploring  

i. Define and Plot Feature Correlations  

ii. Visualize Feature Distributions  

iii. Data Normalization  

K-Means Implementation  

i. Define Optimal Cluster Number (K) by using "Elbow Method" and "Silhouette Analysis"  

<img src='Elbow.PNG'>  

ii. Visualize the Clusters  

iii. Assign the label  

iv. Conclusion  

### 5. Create Cohort and Conduct Cohort Analysis  
Feature Engineering  

i. Extract the Month of the Purchase  

ii. Calculating time offset in Months i.e. Cohort Index  

Create 1st Cohort: User Number & Retention Rate  

i. Pivot Cohort and Cohort Retention  

ii. Visualize analysis of cohort 1 using seaborn and matplotlib  

<img src='Retention.PNG'>  

Create 2nd Cohort: Average Quantity Sold  

i. Pivot Cohort and Cohort Retention  

ii. Visualize analysis of cohort 2 using seaborn and matplotlib  

<img src='Quantity.PNG'>  



Create 3rd Cohort: Average Sales  

i. Pivot Cohort and Cohort Retention  

ii. Visualize analysis of cohort 3 using seaborn and matplotlib  

<img src='Price.PNG'>  
