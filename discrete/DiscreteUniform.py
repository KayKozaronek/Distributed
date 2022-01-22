import streamlit as st
import numpy as np
import plotly.express as px 

def distribution_function(start, end):
    n = end - start + 1
    return 1/n

def plot(start, end):
    xs = np.arange(start, end, 1)
    ys = np.repeat(distribution_function(start, end),len(xs))
    fig = px.bar(x=xs,
                 y=ys,
                 title= f'Discrete Uniform Distribution', 
                 labels={
                    "x": "Number of X successes",
                    "y": "Probability of seing X successes",
                    })

    st.plotly_chart(fig) 

def run():
    
    # Short Description 
    # st.write("""
    #          DESCRIPTION NEEDED
    #          """)
    
    # Parameter Sliders 
    start = st.slider(label='Starting point',
                  min_value=0,
                  max_value=99,
                  value=0,
                  step=1)
    end = st.slider(label='End point',
                    min_value = start,
                    max_value=100,
                    value=start + 1,
                    step=1)
    
    parameters = [start, end]
    
    return parameters