# Women's Clothing Sentiment Analysis Project  
This analysis will focus on using Natural Language techniques to find broad trends in the written thoughts of the customers. The goal in this project is to predict whether customers recommend the product they purchased using the information in their review text.

One of the challenges in this project is to extract useful information from the Review Text variable using text mining techniques. The other challenge is that you need to convert text files into numeric feature vectors to run machine learning algorithms.

At the end of this project, you will learn how to build sentiment classification models using algorithms Logistic Regression, Naive Bayes, Support Vector Machine, Random Forest and Ada Boosting.

Before diving into the project, please take a look at the Determines and Tasks.  


### Data  
The data is a collection of 22641 Rows and 10 column variables. Each row includes a written comment as well as additional customer information. Kaggle source : [https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews](https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews)

Also each row corresponds to a customer review, and includes the variables:

Feature Information:  

Clothing ID: Integer Categorical variable that refers to the specific piece being reviewed.  

Age: Positive Integer variable of the reviewers age.  

Title: String variable for the title of the review.  

Review Text: String variable for the review body.  

Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best.

Recommended IND: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended.

Positive Feedback Count: Positive Integer documenting the number of other customers who found this review positive.

Division Name: Categorical name of the product high level division.

Department Name: Categorical name of the product department name.

Class Name: Categorical name of the product class name.

The basic goal in this project is to predict whether customers recommend the product they purchased using the information in their Review Text. Especially, it should be noted that the expectation in this project is to use only the "Review Text" variable and neglect the other ones. Of course, if you want, you can work on other variables individually.

Project Structure is separated in five tasks: EDA, Feature Selection and Data Cleaning , Text Mining, Word Cloud and Sentiment Classification with Machine Learning.

Classically, you can start to know the data after doing the import and load operations. You need to do missing value detection for Review Text, which is the only variable you need to care about. You can drop other variables.

You will need to apply noise removal and lexicon normalization processes by using the capabilities of the nltk library to the data set that is ready for text mining.

Afterwards, you will implement Word Cloud as a visual analysis of word repetition.

Finally, You will build models with five different algorithms and compare their performance. Thus, you will determine the algorithm that makes the most accurate emotion estimation by using the information obtained from the Review Text variable.

### Steps
1. Exploratory Data Analysis
Import Modules, Load Discover the Data
2. Feature Selection and Data Cleaning
Feature Selection and Rename Column Name
Missing Value Detection
3. Text Mining
Tokenization
Noise Removal
Lexicon Normalization
4. WordCloud - Repetition of Words
Detect Reviews
Collect Words
Create Word Cloud
5. Sentiment Classification with Machine Learning
Train - Test Split
Vectorization
TF-IDF
Logistic Regression
Naive Bayes
Support Vector Machine
Random Forest
AdaBoost
Model Comparison
