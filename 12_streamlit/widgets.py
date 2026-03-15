# it use to creat intrective application
import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter Your name :")

age = st.slider("Enter your age :",0,100,25)
st.write(f"Your age is {age}")

option=["Python","C","C++","Java","Javascript"]
choice =st.selectbox(f"Chosen Your Favriot language :",option)
st.write(f"You Selected {choice}")


if name:
    st.write(f"Hello {name}")


data ={
    "Name":['Ashish','Aman','Sahil','Roy'],
    "Age":[20,22,17,30],
    "City":["Rajasthan","Delhi","Mp","landon"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file =st.file_uploader('Chose a CSV file',type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)