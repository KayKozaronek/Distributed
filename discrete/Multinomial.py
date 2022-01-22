import streamlit as st
import plotly.express as px 
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(n, p, k):
    return nCk(n,k) * p**k * (1-p)**(n-k)

def plot(n, p):
    k = np.arange(n)
    fig = px.bar(x=k,
                 y=distribution_function(n, p, k),
                 title= f'Multinomial Distribution', 
                 labels={
                    "x": "Value of Random Variable",
                    "y": "Probability",
                    })

    st.plotly_chart(fig)
    
# @st.cache
def run():    
    # Parameter Sliders 
    param_1 = st.slider(label='MISSING',
                  min_value=0,
                  max_value=100,
                  value=100,
                  step=1)

    param_2 = st.slider(label='MISSING',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.9,
                  step=0.01)
    
    parameters = [param_1, param_2]
    
    return parameters
    
