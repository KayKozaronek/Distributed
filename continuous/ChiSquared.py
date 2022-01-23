import streamlit as st
import plotly.express as px 
import numpy as np 
from scipy.stats import chi2


def plot(degrees): 
    xs = np.linspace(chi2.ppf(0.01, degrees),
                chi2.ppf(0.99, degrees), 1000)

    fig = px.area(x = xs, 
            y = chi2.pdf(xs, degrees),
            title = 'Student-t Distribution',
            labels = {
                'x': 'Value of Random Variable',
                'y': 'Probability'
            }
            )  
    if degrees > 2: 
        fig.update_yaxes(range=[0,0.25])
    elif degrees == 1:
        fig.update_yaxes(range=[0,2])
    
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
    
