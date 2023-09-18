import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px 

### Problem 4 ###
iris = sns.load_dataset("iris")
st.write("""
# Iris Dataset
How are sepal and petal dimensions associated with Iris species?
""")
fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_length', color='species')         
st.plotly_chart(fig)