import streamlit as st
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(r, n, p):
    q = 1-p
    return nCk(r+n-1, r-1) * (p**r) * (q**n)

def plot(r, p, x_range):
    n = np.arange(x_range)
    fig, ax = plt.subplots()
    ax.bar(n, distribution_function(r, n, p))
    
    ax.set_title('Binomial Distribution')
    ax.set_xlabel('Number of X successes')
    ax.set_ylabel('Probability of seing X successes')

    st.pyplot(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    r = st.slider(label='MISSING DESCRIPTION (r)',
                  min_value=0,
                  max_value=100,
                  value=100,
                  step=1)

    p = st.slider(label='MISSING DESCRIPTION (p)',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.9,
                  step=0.01)
        
    x_range = st.slider(label='Use this slider to resize your x-axis (Note: This is not a parameter of the Geometric Distribution)',
                  min_value=0,
                  max_value=500,
                  value=50,
                  step=5)

    parameters = [r,p, x_range]
    
    return parameters
    
