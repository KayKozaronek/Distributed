import streamlit as st
import plotly.express as px 
import numpy as np 
from scipy.stats import t 


def plot(degrees): 
    xs = np.linspace(t.ppf(0.01, degrees),
                t.ppf(0.99, degrees), 1000)

    fig = px.area(x = xs, 
            y = t.pdf(xs, degrees),
            title = 'Student-t Distribution',
            labels = {
                'x': 'Value of Random Variable',
                'y': 'Probability'
            }
            )  
    fig.update_yaxes(range=[0,0.5])
    
    st.plotly_chart(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    degrees = st.slider(label='Adjust the degrees of freedom (n)',
                  min_value=1,
                  max_value=100,
                  value=10,
                  step=1)

    parameters = [degrees]
    
    return parameters
    
