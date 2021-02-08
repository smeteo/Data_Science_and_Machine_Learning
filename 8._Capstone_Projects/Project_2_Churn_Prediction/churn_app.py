import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
import webbrowser

st.sidebar.title("Churn Probability and Prediction of an Employee")

im = Image.open("image.jpg")
st.image(im, width=500)


#xg_model = pickle.load(open("XGBoost","rb"))
xgb_model = pickle.load(open("XGBoost.pkl","rb"))
rf_model = pickle.load(open("RF.pkl","rb"))



departments = ['Sales','Technical','Support','IT','Product_mng','Marketing','RandD','Accounting','HR','Management']
salary_level = ['Low', 'Medium','High']
work_accidents = ['Yes','No']
promotions= ['Yes','No']


st.sidebar.header("Configure the Employee Features:")
department = st.sidebar.selectbox("What is the department of the employee?", (departments))
salary = st.sidebar.selectbox("What is the salary of the employee?",(salary_level))
work_accident = st.sidebar.selectbox("Has the employee ever had a work accident?",(work_accidents))
promotion = st.sidebar.selectbox("Has the employee been promoted in the last five years?",(promotions))

satisfaction = st.sidebar.slider("What is the percentage of the employee's satisfaction level?",0,100,50,1)
evaluation = st.sidebar.slider("What is the percentage of the employer's last evaluation level?",0,100,50, step=1)
project_count= st.sidebar.slider("How many projects has the employee worked on?",2,7,3, step=1)
montly_hours= st.sidebar.slider("What is the employee's average monthly working hours?",96,310,200, step=1)
spend_time= st.sidebar.slider("How many years has the employee been with the company?",2,10,3, step=1)

department_encode={  'Sales':7, 
                     'Technical':9, 
                     'Support':8, 
                     'IT':0, 
                     'Product_mng':6, 
                     'Marketing':5,
                     'RandD':1, 
                     'Accounting':2, 
                     'HR':3, 
                     'Management':4}

salary_encode = {'Low':0,
                 'Medium':1,
                 'High':2}


yes_no_encode = {'Yes':1, 'No':0}

my_dict = {'satisfaction_level':satisfaction/100, 
           'last_evaluation':evaluation/100, 
           'number_project':project_count,
           'average_montly_hours':montly_hours, 
           'time_spend_company':spend_time, 
           'Work_accident':yes_no_encode[work_accident],
           'promotion_last_5years':yes_no_encode[promotion], 
           'Departments':department_encode[department], 
           'salary':salary_encode[salary],
            }

df = pd.DataFrame.from_dict([my_dict])
st.write('')
#st.dataframe(data=df, width=500, height=400)


st.subheader("1.Select features of an employee from left sidebar")

st.image('left.png', width=100)


st.write('')

st.subheader("2.Choose a Machine Learning Model:")
model = st.radio('',[
    #'XGBoost Classifier', 
                     'Random Forest Classifier',
                     'XGBOOST Classifier'
                    ])


# Button
if st.button("Predict"):
    import time
    with st.spinner("ML Model is loading..."):
        my_bar=st.progress(0)
        for p in range(0,101,10):
            my_bar.progress(p)
            time.sleep(0.1)
    
        if model=='Random Forest Classifier':
            churn_probability = rf_model.predict_proba(df)
            is_churn= rf_model.predict(df)
            
#        elif model=='XGBoost Classifier':
#            churn_probability= xg_model.predict_proba(df)
#            is_churn= xg_model.predict(df)
            
        elif model=='XGBOOST Classifier':
            churn_probability= xgb_model.predict_proba(df)
            is_churn= xgb_model.predict(df)
        
           
    
        st.success(f'The Probability of the Employee Churn (leave) is %{round(churn_probability[0][1]*100,1)}')
        
        if is_churn[0]:
            st.warning("The Employee will leave")
        else:
            st.success("The Employee will not leave")
            
st.subheader("Description")            
st.markdown("""

This is a Human Recources Analytics Project based on real data set. Dataset consist of 15.000 sample employee information such as the attributes on left side of the page.


Open source dataset can be found on Kaggle. 
""")





#if st.button('Click here to see datasource'):
    #webbrowser.open_new_tab('https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Employee+Churn+in+Python/HR_comma_sep.csv')
st.write("Click here to see real data source [Link](https://www.kaggle.com/c/employee-churn-prediction/data)")
st.write("Click here to download csv file [Link](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Employee+Churn+in+Python/HR_comma_sep.csv)")

    
    
#https://www.kaggle.com/c/employee-churn-prediction/data
    
st.markdown("""

The purpose of that project is to predict, based on the information submitted, whether the employee will going to leave (churn) the company or not in near future.  

Supervised Machine Learning, Random Forest and XGBOOST Classification algoritms used in that model. Change parameters on the left, you'll realize the effect on outcome.

""")


st.write(" ")

st.markdown("Prepared by: XXxxx")
#if st.button('LinkedIn'):
    #webbrowser.open_new_tab('https://www.linkedin.com/xxxx')


#if st.button('GitHub'):
    #webbrowser.open_new_tab('https://github.com/xxxxx')
    
#if st.button('Tableau'):
    #webbrowser.open_new_tab('https://public.tableau.com/profile/xxxx/')
    
#[['this is an image link']('linkedin.png')]('https://streamlit.io')
#['this is a text link']('https://streamlit.io')

st.write("Find me on [LinkedIn](https://www.linkedin.com/in/xxxxx/) / [GitHub](https://github.com/xxxx) / [Tableau](https://public.tableau.com/profile/xxxxx) ")
st.write("Find me on [LinkedIn](https://www.linkedin.com/in/xxxxx/) / [GitHub](https://github.com/xxxx) / [Tableau](https://public.tableau.com/profile/xxxxx) ")


#st.markdown('[![](left.jpg)](site.com)')
