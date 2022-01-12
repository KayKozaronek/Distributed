import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def distribution_function(start, end):
    n = end - start + 1
    return 1/n

def plot(start, end):
    xs = np.arange(start, end, 1)
    fig, ax = plt.subplots()
    ax.bar(xs, distribution_function(start, end))
    
    ax.set_title('Discrete Uniform Distribution')
    ax.set_xlabel('Number of X successes')
    ax.set_ylabel('Probability of seing X successes')

    st.pyplot(fig)

def run():
    st.write("Hello it's Discrete Uniform")
    
    # Short Description 
    st.write("""
             DESCRIPTION NEEDED
             """)
    
    # Parameter Sliders 
    start = st.slider(label='Starting point',
                  min_value=0,
                  max_value=100,
                  value=0,
                  step=1)
    end = st.slider(label='End point',
                    min_value = start,
                    max_value=100,
                    value=10,
                    step=1)
    
    parameters = [start, end]
    
    return parameters