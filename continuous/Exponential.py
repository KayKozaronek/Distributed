import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 


def distribution_function():
    pass

def plot():
    
    x = np.arange()
    fig, ax = plt.subplots()
    ax.plot(x, distribution_function(x))
    
    ax.set_title('Exponential Distribution')
    ax.set_xlabel('Value of Random Variable')
    ax.set_ylabel('Probability ')

    st.pyplot(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    param_a = st.slider(label='',
                  min_value=-50,
                  max_value=50,
                  value=0,
                  step=1)
    
    param_b = st.slider(label='',
                  min_value=0,
                  max_value=100,
                  value=25,
                  step=1)

    parameters = []
    
    return parameters
    
