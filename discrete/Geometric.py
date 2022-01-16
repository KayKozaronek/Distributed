import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def distribution_function(p, k):
    q = 1-p
    return (q**k) *p

def plot(p, x_range):
    xs = np.arange(x_range)
    fig, ax = plt.subplots()
    ax.bar(xs, distribution_function(p, xs))
    
    ax.set_title('Geometric Distribution')
    ax.set_xlabel('Value of Random Variable')
    ax.set_ylabel('Probability')

    st.pyplot(fig)

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
    
    x_range = st.slider(label='Use this slider to resize your x-axis (Note: This is not a parameter of the Geometric Distribution)',
                  min_value=0,
                  max_value=100,
                  value=50,
                  step=1)
    parameters = [p, x_range]
    
    return parameters