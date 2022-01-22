import streamlit as st
import plotly.express as px 
import numpy as np 


def distribution_function(mean, variance, x):
    return 1 / np.sqrt(variance * 2 * np.pi) * np.exp(-(x - mean)**2 / (2*variance)) 

def plot(mean, variance):
    term = mean - 4*np.sqrt(variance)
    # plot_range_1 = [mean - term, mean + term] 
    plot_range_2 = [-50, 50]
    xs = np.linspace(plot_range_2[0], plot_range_2[1], 1000)

    fig = px.area(x=xs,
                y=distribution_function(mean, variance, xs),
                title= f'Normal Distribution (Gaussian)', 
                labels={
                    "x": "Value of Random Variable X",
                    "y": "Probability",
                })
    
    st.plotly_chart(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    mean = st.slider(label='Set the center of your distribution (mean)',
                  min_value=-20,
                  max_value=20,
                  value=0,
                  step=1)
    
    variance = st.slider(label='This parameter determines the spread of your data (Variance)',
                  min_value=0,
                  max_value=100,
                  value=25,
                  step=1)

    parameters = [mean, variance]
    
    return parameters
    
