import streamlit as st
import plotly.express as px 
import numpy as np 


def distribution_function(l,x):
    return l * np.exp(-l*x)

def plot(l, x_range):
    xs = np.linspace(0, x_range, 1000)
    fig = px.area(x=xs,
                y=distribution_function(l, xs),
                title= f'Exponential Distribution', 
                labels={
                "x": "Value of Random Variable X",
                "y": "Probability",
                })
    
    st.plotly_chart(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    l = st.slider(label='Set the value for lambda',
                  min_value=0.0,
                  max_value=50.0,
                  value=1.0,
                  step=0.1)
    
    x_range = st.slider(label='Upper end of plot',
                  min_value=0,
                  max_value=100,
                  value=25,
                  step=1)

    parameters = [l, x_range]
    
    return parameters
    
