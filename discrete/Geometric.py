import streamlit as st
import numpy as np
import plotly.express as px 

def distribution_function(p, k):
    q = 1-p
    return (q**k) *p

def plot(p):
    xs = np.arange(10)
    fig = px.bar(x=xs,
                 y=distribution_function(p, xs),
                 title= f'Geometric Distribution', 
                 labels={
                    "x": "Value of Random Variable",
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
                  value=0.5,
                  step=0.01)
    
    parameters = [p]
    
    return parameters