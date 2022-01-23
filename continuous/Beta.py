import streamlit as st
import plotly.express as px 
import numpy as np 
from scipy.stats import beta 


def plot(a, b): 
    xs = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 1000)
    fig = px.area(x = xs, 
            y = beta.pdf(xs, a, b),
            title = 'Beta Distribution',
            labels = {
                'x': 'Value of Random Variable',
                'y': 'Probability'
            }
            )  
    fig.update_yaxes(range=[0,8])
    
    st.plotly_chart(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    a = st.slider(label='Adjust the shape parameter (α)',
                  min_value=0.0,
                  max_value=5.0,
                  value=1.0,
                  step=0.1)
    
    b = st.slider(label='Adjust the shape parameter (β)',
                  min_value=0.0,
                  max_value=5.0,
                  value=1.0,
                  step=0.1)

    parameters = [a, b]
    
    return parameters
    
