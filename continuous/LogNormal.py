import streamlit as st
import plotly.express as px 
import numpy as np 
from scipy.stats import lognorm 


def plot(mean, std): 
    xs = np.linspace(lognorm.ppf(0.01, std),
                lognorm.ppf(0.99, std), 1000)

    fig = px.area(x = xs, 
            y = lognorm.pdf(xs, s=std, loc=mean),
            title = 'Log-Normal Distribution',
            labels = {
                'x': 'Value of Random Variable',
                'y': 'Probability'
            }
            )  
    # fig.update_yaxes(range=[0,0.5])
    
    st.plotly_chart(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    mean = st.slider(label='Adjust the mean (μ)',
                  min_value=-1.0,
                  max_value=1.0,
                  value=0.0,
                  step=0.1)
    
    std = st.slider(label='Adjust the standard deviation (σ)',
                  min_value=0.01,
                  max_value=1.0,
                  value=0.5,
                  step=0.01)

    parameters = [mean, std]
    
    return parameters
    
