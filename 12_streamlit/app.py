import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("HELLO String")

## Display  a simple Text
st.write("This is a simple Text")

## Creat a single Data frame
df = pd.DataFrame({
    'First column':[1,2,3,4],
    'Second Column':[30,40,50,60]

})

# Display the data frame
st.write("Here the data frame") # write are use to disply perticuler data frame
st.write(df)


# Creat a line chart
char_data =pd.DataFrame(
    np.random.rand(20,3),columns=['a','b','c']
)
st.line_chart(char_data)


