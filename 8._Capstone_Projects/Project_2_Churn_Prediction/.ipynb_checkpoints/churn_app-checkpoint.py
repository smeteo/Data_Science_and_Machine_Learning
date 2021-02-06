import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

st.sidebar.title("Church Probeblity and Prediction of an Employee")

im = Image.open("image.jpg")
st.image(im, width=700)


#xg_model = pickle.load(open("XGBoost","rb"))
knn_model = pickle.load(open("Knn","rb"))
rf_model = pickle.load(open("RF","rb"))



departments = ['sales','technical','support','IT','product_mng','marketing','RandD','accounting','hr','management']
salary_level = ['low', 'medium','high']
work_accidents = ['Yes','No']
promotions= ['Yes','No']


st.sidebar.header("Configure the Employee Features:")
department = st.sidebar.selectbox("What is the department of the employee?", (departments))
salary = st.sidebar.selectbox("What is the salary of the employee?",(salary_level))
work_accident = st.sidebar.selectbox("Has the employee ever had a work accident?",(work_accidents))
promotion = st.sidebar.selectbox("Has the employee been promoted in the last five years?",(promotions))

satisfaction = st.sidebar.slider("What is the percentage of the satisfaction level?",0,100,50,1)
evaluation = st.sidebar.slider("What is the percentage of the employer's last evaluation level?",0,100,50, step=1)
project_count= st.sidebar.slider("How many projects does the employee work on?",2,7,3, step=1)
montly_hours= st.sidebar.slider("What is the employee's monthly working hours?",96,310,200, step=1)
spend_time= st.sidebar.slider("How many years has the employee been with the company?",2,10,3, step=1)

department_encode={  'sales':7, 
                     'technical':9, 
                     'support':8, 
                     'IT':0, 
                     'product_mng':6, 
                     'marketing':5,
                     'RandD':1, 
                     'accounting':2, 
                     'hr':3, 
                     'management':4}

salary_encode = {'low':0,
                 'medium':1,
                 'high':2}


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
st.dataframe(data=df, width=700, height=400)
st.write('')

st.subheader("Choose a ML Model:")
model = st.radio('',[
    #'XGBoost Classifier', 
                     'Random Forest Classifier',
                     'KNN Classifier'
                    ])


# Button
if st.button("Submit"):
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
            
        elif model=='KNN Classifier':
            churn_probability= knn_model.predict_proba(df)
            is_churn= knn_model.predict(df)
        
           
    
        st.success(f'The Probability of the Employee Churn is %{round(churn_probability[0][1]*100,1)}')
        
        if is_churn[0]:
            st.warning("The Employee is CHURN")
        else:
            st.success("The Employee is NOT CHURN")