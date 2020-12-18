# Decision Trees and Random Forest
Based on artificial data set, this notebook consists of Decision Tree and Random Forest models 
with steps below;  
            -Data Input  
            -Exploratory Data Analysis  
            -Data Visualization  
            -Splitting Test and Train Data  
            -Decision Tree Model  
            -Predictions and Evaluations  
            -Confusion Matrix  
            -Random Forest Model  
              
            



   
**Data Exploration**  

| Feature |Description |  
| --- | --- |
|credit.policy | 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.|
|purpose| The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").|
|int.rate| The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.|
|installment| The monthly installments owed by the borrower if the loan is funded.|
|log.annual.inc| The natural log of the self-reported annual income of the borrower.|
|dti| The debt-to-income ratio of the borrower (amount of debt divided by annual income).|
|fico| The FICO credit score of the borrower.|
|days.with.cr.line| The number of days the borrower has had a credit line.|
|revol.bal| The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).|
|revol.util| The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).|
|inq.last.6mths| The borrower's number of inquiries by creditors in the last 6 months.|
|delinq.2yrs| The number of times the borrower had been 30+ days past due on a payment in the past 2 years.|
|pub.rec| The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).|