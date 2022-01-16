import streamlit as st
import matplotlib.pyplot as plt
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(w, b, n, k):
    return nCk(w, k) * nCk(b, n-k) / nCk(w+b, n)

def plot(w, b, n):
    k = np.arange(n)
    fig, ax = plt.subplots()
    ax.bar(k, distribution_function(w, b, n, k))
    
    ax.set_title('Hypergeometric Distribution')
    ax.set_xlabel('Value of Random Variable')
    ax.set_ylabel('Probability ')

    st.pyplot(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    w = st.slider(label='MISSING DESCRIPTION (w)',
                  min_value=0,
                  max_value=100,
                  value=50,
                  step=1)

    b = st.slider(label='MISSING DESCRIPTION (b)',
                  min_value=0,
                  max_value=100,
                  value=50,
                  step=1)
        
    n = st.slider(label='MISSING DESCRIPTION (n)',
                  min_value=0,
                  max_value=100,
                  value=50,
                  step=1)

    parameters = [w, b, n]
    
    return parameters
    
