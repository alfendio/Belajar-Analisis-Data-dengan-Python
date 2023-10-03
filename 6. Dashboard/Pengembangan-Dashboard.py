# Alfendio Alif Faudisyah

import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# 1. Pengenalan Streamlit
st.title('Alfendio Alif Faudisyah')

st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# 2. Basic Element dalam Streamlit

# 2.1 Write
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

# 2.2 Text
# markdown()
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# title()
st.title('Belajar Analisis Data')

# header()
st.header('Pengembangan Dashboard')

# subheader()
st.subheader('Pengembangan Dashboard')

# caption()
st.caption('Copyright (c) 2023')

# code()
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# text()
st.text('Halo, calon praktisi data masa depan.')

# latex()
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

# 2.3 Data Display
# dataframe()
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

# table()
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

# metric()
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# json()
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# 2.4 Chart
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# 3. Basic Widgets dalam Streamlit

# 3.1 Input Widget
# Text input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# Text-area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# Number input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# Date input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# File uploader
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Camera input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

# 3.2 Button Widgets 
# Button
if st.button('Say hello'):
    st.write('Hello there')

# Checkbox
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

# Radio button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    # horizontal=False #error
)

# Select Box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Multiselect
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)


 