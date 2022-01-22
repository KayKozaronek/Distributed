import streamlit as st
import plotly.express as px 
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(r, n, p):
    q = 1-p
    return nCk(r+n-1, r-1) * (p**r) * (q**n)

def plot(r, p):
    n = np.arange(2* r * 1/p) #Range was chosen through experimentation NOT OPTIMAL
    fig = px.bar(x=n,
                 y=distribution_function(r, n, p),
                 title= f'Negative Binomial Distribution', 
                 labels={
                    "x": "Number of successes",
                    "y": "Probability",
                    })

    st.plotly_chart(fig) 


# @st.cache
def run():    
    # Parameter Sliders 
    r = st.slider(label='Number of failures until the experiment is stopped (r)',
                  min_value=1,
                  max_value=10,
                  value=5,
                  step=1)

    p = st.slider(label='Probability of success(p)',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.9,
                  step=0.01)
    
    parameters = [r,p]
    
    return parameters
    
