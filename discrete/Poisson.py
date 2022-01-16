import streamlit as st
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np 


def distribution_function(l, k):
    return np.exp(-l) * (l**k) / factorial(k)

def plot(l, x_range):
    k = np.arange(x_range)
    fig, ax = plt.subplots()
    ax.bar(k, distribution_function(l,k))
    
    ax.set_title('Poisson Distribution')
    ax.set_xlabel('Value of Random Variable')
    ax.set_ylabel('Probability ')

    st.pyplot(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    l = st.slider(label='MISSING DESCRIPTION (lambda)',
                  min_value=0.0,
                  max_value=5.0,
                  value=1.0,
                  step=0.1)
        
    x_range = st.slider(label='MISSING DESCRIPTION (x_range)',
                  min_value=0,
                  max_value=50,
                  value=25,
                  step=1)

    parameters = [l, x_range]
    
    return parameters
    
