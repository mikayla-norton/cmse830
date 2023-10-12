import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpg = sns.load_dataset("mpg")

x = [0.5,1]
y = [2,1]
dataset = pd.DataFrame({'x': x, 'y': y})

#st.set_page_config(layout="wide")

st.title("ICA - Wednesday October 11: Regression by Hand")
st.write("Group 10: Mikayla Norton, Md Faisal, Michael Guel, Abigael Mogusu")
data = st.selectbox("Please choose a dataset", ["mpg", "simple"])

model = st.selectbox("Please choose model type", ["line", "RBF-NN"])

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')



if data == "mpg":
    numerics = mpg.columns[0:7]
    for i in numerics:
        mpg[i] = pd.to_numeric(mpg[i])
    x = st.selectbox("Please choose your x variable", numerics, index=0)
    y = st.selectbox("Please choose your y variable", numerics, index=3)
    if x == y:
        st.error("Please select different x and y variables")
    min_m = float(-max(mpg[y]/mpg[x]))
    max_m  = float(max(mpg[y]/mpg[x]))
    min_b = float(-max(mpg[y]))
    max_b = float(max(mpg[y]))
    x = mpg[x]
    y = mpg[y]

    
else:
    min_m = -20.0
    max_m = 20.0
    min_b = -20.0
    max_b = 20.0
    x = dataset['x']
    y = dataset['y']

if model == "line":
    m = st.slider("Select your slope", min_m, max_m, step = 0.1)
    b = st.slider("Select your intercept", min_b, max_b, step = 0.1)
    fig, ax = plt.subplots() 
    ax.scatter(x,y)
    abline(m,b)
    st.pyplot(fig)

    MSE = sum(y-(m*x+b))**2
    MAE = sum(abs(y-(m*x+b)))
    st.write("MAE: " + str(MAE))
    st.write("MSE: " + str(MSE))

else:
    centers = st.multiselect("Please select centers", list(range(0,100)), max_selections=2)
    bandwidth = st.selectbox("Please select bandwidth", list(range(0,100)))
    weights = st.multiselect("Please select weights", list(range(0,100)), max_selections=2)

    # f1 = weights[0] *np.exp(-(centers[0]-centers[0])**2/(bandwidth**2)) + weights[1] *np.exp(-(centers[0]-centers[1])**2/(bandwidth**2))
    # f2 = weights[0] *np.exp(-(centers[1]-centers[0])**2/(bandwidth**2)) + weights[1] *np.exp(-(centers[0]-centers[0])**2/(bandwidth**2))
    fx = weights[0] * np.exp(-(x-centers[0])**2/(bandwidth**2)) + weights[1] * np.exp(-(x-centers[1])**2/(bandwidth**2)) 
    fig, ax = plt.subplots() 
    ax.plot(x,fx)
    st.pyplot(fig)