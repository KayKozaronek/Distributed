import streamlit as st
import plotly.express as px 
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(n, p, k):
    return nCk(n,k) * p**k * (1-p)**(n-k)

def plot(n, p):
    k = np.arange(0, n, 1)

    fig = px.bar(x=k,
                 y=distribution_function(n, p, k),
                 title= f'Binomial Distribution', 
                 labels={
                    "x": "Number of X successes",
                    "y": "Probability of seing X successes",
                    })

    st.plotly_chart(fig)  

# @st.cache
def run():    
    # Short Description 
    # st.write("""
    #          The Bernoulli distirbution uses one Parameter (p) which describes the probability of succes. 
    #          Imagine the following: You're flipping a cat and you want to know what the probability of it landing on it's feet is. 
    #          You think it's 90 % (p = 0.9).
    #          Now you perform the experiment and count how many times your cat lands on its feet and how many times you have to save have last minute from hurting itself.
    #          Let's say you perform the experiment 100 times. 
    #          The bernoulli experiment now tells you how likely your cat is to land this many times on it's feet
    #          """)
    
    # Parameter Sliders 
    n = st.slider(label='Out of a pool of some items (n)',
                  min_value=0,
                  max_value=100,
                  value=100,
                  step=1)

    p = st.slider(label='With a probability of successfully picking these items (p)',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.9,
                  step=0.01)
    
    parameters = [n,p]
    
    return parameters
    
