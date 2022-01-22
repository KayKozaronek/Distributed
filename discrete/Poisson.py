import streamlit as st
import plotly.express as px 
from scipy.special import factorial
import numpy as np 


def distribution_function(l, k):
    return np.exp(-l) * (l**k) / factorial(k)

def plot(l):
    xs = np.arange(20) 
    fig = px.bar(x=xs,
                 y=distribution_function(l, xs),
                 title= f'Poisson Distribution', 
                 labels={
                    "x": "Value of Random Variable",
                    "y": "Probability",
                    })
    

    st.plotly_chart(fig) 

# @st.cache
def run():    
    # Parameter Sliders 
    l = st.slider(label='The mean rate of occurrence for the event being measured (λ = lambda)',
                  min_value=0.0,
                  max_value=10.0,
                  value=1.0,
                  step=0.1)

    parameters = [l]
    
    return parameters
    
