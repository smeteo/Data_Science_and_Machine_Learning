import streamlit as st

# text/title
st.title('Streamlit Tutorials')

st.text('Hello Streamlit')

#header/subheader
st.header('This is a header')
st.subheader('This is a subheader')

# markdown
st.markdown('# This is Markdown')
st.markdown('### This is Markdown')

st.markdown('** This is bold a markdown **')
st.markdown('_This is italic a Markdown_')

# colorful text
st.success('Successfull')
st.info('This is an information')

#st.help(st.info)

st.warning('This is a warning')
st.error('This is an error')

# get help
st.help(range)

# writing text
st.write('Text with write func')

st.write('Hello, *World!* :sunglasses:')

# images
from PIL import Image
im = Image.open('Workplace.jpg')
st.image(im, width=300, caption='Workplace')

vid_file=open('ds_video.mp4','rb')
st.video(vid_file)

# checkbox
if st.checkbox('Show/Hide'):
    st.text("I'm showing because you checked the box")
    
st.checkbox('Hide/Seek')

# radio buttons
status = st.radio('Whatis your status?', ('Active','Inactive'))

if status == 'Active':
    st.success("You're active")
else:
    st.warning("You're inactive")
    
# selectbox
occupation = st.selectbox('Your Occupation', ['Programmer', 'Data Scientist', 'Doctor'])

st.write('You selected this option:', occupation)

# multiselect
location=st.multiselect('Where do you work?', ('London','Berlin','Paris','New York'))
st.write('You selected ', len(location),' location')

# slider
level=st.slider('What is your level', 0,40,10, step=5)
st.write('You selected', level)

# Button
st.button('Simple Button')

if st.button('About'):
    st.text('Streamlit is cool')
else:
    st.text('Hasta pronto')
    
# text input
firstname = st.text_input('Enter Your Firstname')
if st.button('Submit'):
    st.success(firstname.capitalize())

# text area
message = st.text_area('Enter your text', 'Type here...')
if st.button('submit'):
    result=message.title()
    st.success(result)
    
#date input
import datetime
today=st.date_input('Today is', datetime.datetime.now())

#st.help(st.date_input)

d = st.date_input('When is your birthday', datetime.date(2019,7,6))
st.write('Your birthday is:',d)

# time input

the_time=st.time_input('The time is', datetime.time(8,45))

# Raw Data
st.text('Display Text')

# Single code
st.code('import numpy as np')

# multiple codes

with st.echo():
    import numpy as np
    import pandas as pd
    
## progress bar
#import time
#my_bar = st.progress(0)
#for p in range(50):
#    my_bar.progress(p+1)
#    time.sleep(0.1)
    
## spinner
#with st.spinner('Waiting....'):
#    time.sleep(3)
#st.success('Finished')
#st.balloons()

st.sidebar.title('Churn Probability of a Single Customer')

import pickle
import pandas as pd

df=pickle.load(open('df_saved.pkl', 'rb'))

st.write(df.head())