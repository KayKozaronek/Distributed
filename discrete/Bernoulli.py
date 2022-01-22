import streamlit as st
import numpy as np
import plotly.express as px

def distribution_function(p):
    return [(1-p), p]

def plot(p):
    xs = np.array([0,1])
    fig = px.bar(x=xs,
                 y=distribution_function(p),
                 title= f'Bernoulli (p = {p})', 
                 labels={
                    "x": "Value of Random Variable X",
                    "y": "Probability",
                    })

    st.plotly_chart(fig)    

def run():    
    # Short Description 
    # st.write("""
    #          DESCRIPTION NEEDED
    #          """)
    
    # Parameter Sliders 
    p = st.slider(label='Probability of Success',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.6,
                  step=0.01)
    
    parameters = [p]
    
    return parameters