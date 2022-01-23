import streamlit as st
import plotly.express as px 
import numpy as np 
from scipy.stats import gamma

def plot(a, scale):
    # rv = gamma(a)
    xs = np.linspace(gamma.ppf(0.01, a),
                gamma.ppf(0.99, a), 100)
    
    fig = px.area(x=xs, 
                y= gamma.pdf(xs, a =a, scale=scale),
                title= f'Gamma Distribution', 
                labels={
                "x": "Value of Random Variable X",
                "y": "Probability",
                })
        
    st.plotly_chart(fig)
        
# @st.cache
def run():    
    # Parameter Sliders 
    a = st.slider(label='Adjust the shape parameter (α)',
                  min_value=0.0,
                  max_value=10.0,
                  value=1.0,
                  step=0.01)
    
    scale = st.slider(label='Adjust the inverse scale parameter (β)',
                  min_value=0.0,
                  max_value=10.0,
                  value=1.0,
                  step=0.01)

    parameters = [a, scale]
    
    return parameters
    
