import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier 

@st.cache_data # it a decorator to use save function result
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names) #feature_names is column names
    df['species']=iris.target
    return df,iris.target_names #target_names is class names


df,target_names=load_data()
model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)
sepal_width = st.sidebar.slider("Sepal width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)
petal_length = st.sidebar.slider("Petal length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)
petal_width = st.sidebar.slider(
    "Petal width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

input_data =[[sepal_length,sepal_width,petal_length,petal_width]]

# pridict
pridiction =model.predict(input_data)
pridictet_species =target_names[pridiction[0]]

st.write("pridictin")
st.write(f"The predected species is  : {pridictet_species}")