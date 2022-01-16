import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def distribution_function(p):
    return [p, (1-p)]

def plot(p):
    xs = np.array([0,1])
    fig, ax = plt.subplots()
    ax.bar(xs, distribution_function(p), width=0.1)
    
    ax.set_title('Bernoulli Distribution')
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
    
    parameters = [p]
    
    return parameters