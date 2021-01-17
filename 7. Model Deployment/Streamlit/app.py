import streamlit as st
import sklearn

#text/title
st.title("Streamlit Tutorials")
st.text("Hello Streamlit")

#header/subheader
st.header("This is a header")
st.subheader("This is a subheader")

#markdown
st.markdown("# This is a Markdown")

st.markdown("** This is also a markdown **")

#colorfull Text
st.success("Successfull")
st.info("This is an information")
#st.help(st.info)
st.warning("This is a warning")
st.error("This is an error")

#get help
st.help(range)

#writing text
st.write("Text with write func")

#images
from PIL import Image
im = Image.open("picture.png")
st.image(im, width=300, caption="GD")
#st.help(st.image)

vid_file=open("IMG_3751.MOV", 'rb')
st.video(vid_file)

#checkbox
if st.checkbox("Show/Hide"):
    st.text("I'm showing because you checked the box")
    
st.checkbox("Hide/Seek")

#radio buttons
status = st.radio("What is your status?", ("Active", "Inactive"))
#st.help(st.radio)
if status == "Active":
    st.success("You are active!")
else:
    st.warning("You are inactive")
    
    
#selectbox
occupatoion=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option:", occupatoion)

#multiselect
location=st.multiselect("Where do you work?", ("London", "Istanbul", "Moscow", "Berlin"))
st.write("You selected:", len(location), "locations")

#slider
level=st.slider("What is your level", 0, 40, 10, step=5)
st.write("You selected", level)

#Button
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is Cool")
else:
    st.text("Hasta Pronto")
    
    
#text input
firstname=st.text_input("Enter Your Firstname")
if st.button("Submit"):
    result=firstname.title()
    st.success(result)
    
#text area
message=st.text_area("Enter your text", "Type Here...")
if st.button("submit"):
    result=message.title()
    st.success(result)
    
#date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())

#st.help(st.date_input)
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

#time input

the_time=st.time_input("The time is", datetime.time(8,45))

#Raw Data
st.text("Display Text")

#single code
st.code("import numpy as np")

#multiple codes
with st.echo():
    import numpy as np
    import pandas as pd
    
    
#progress bar
#import time
#my_bar=st.progress(0)
#for p in range(50):
#    my_bar.progress(p+1)
#    time.sleep(0.1)
 
#spinner
#import time
#with st.spinner("Waiting......"):
#    time.sleep(3)
#st.success("Finished")
#st.balloons()

st.sidebar.title("Churn Probability of a Single Customer")

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Richard Title </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
import pickle
import pandas as pd

df=pickle.load(open("df_saved.pkl", "rb"))

st.write(df.head())
st.table(df.head())
st.dataframe(df.head())

tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))

def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample

df= single_customer()

import pickle
import pandas as pd
pickle.dump(rf_reg, open('rf_model', 'wb'))
pickle.dump(model, open('xgb_model', 'wb'))








