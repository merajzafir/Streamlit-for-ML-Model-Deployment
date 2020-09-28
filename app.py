import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Welcome to Natural Language Processing')

st.write("Here's our first attempt at using data to create a table:")
df=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]})
df

if st.checkbox('I agree'):
        st.write('Great!')

contacted = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
'Contact: ', contacted

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected:', option
# Most of the elements you can put into your app can also be put into a sidebar
# using this syntax: st.sidebar.[element_name](). Here are a few examples
# st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart()
st.sidebar.write("Welcome!!!")

x = 4
#st.write(x, 'squared is', x * x)
x, 'squared is', x * x

st.text("Welcome Again!")

x = st.sidebar.slider('x')  # 👈 this is a widget
x, 'squared is', x * x
# On first run, the app above should output the text “0 squared is 0”. Then
# every time a user interacts with a widget, Streamlit simply reruns your script
# from top to bottom, assigning the current state of the widget to your variable.
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
