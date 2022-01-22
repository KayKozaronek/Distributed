import streamlit as st
import plotly.express as px 
from scipy.special import factorial
import numpy as np 

def nCk(n,k):
    f = factorial
    return f(n) / f(k) / f(n-k)

def distribution_function(N, K, n, k):
    return nCk(K, k) * nCk(N-K, n-k) / nCk(N, n)

def plot(N, K, n):
    k = np.arange(start=max(0, n+K-N), 
                  stop=min(n,K), 
                  step=1)
    
    # st.write(k)
    # st.write(distribution_function(N, K, n, k))
    fig = px.bar(x=k,
                 y=distribution_function(N, K, n, k),
                 title= f'Hypergeometric Distribution', 
                 labels={
                    "x": "Value of Random Variable",
                    "y": "Probability",
                    })

    st.plotly_chart(fig)
    
# @st.cache
def run():    
    # Parameter Sliders 
    N = st.slider(label='Number of items in the population (N)',
                  min_value=0,
                  max_value=100,
                  value=50,
                  step=1)

    K = st.slider(label= 'Number of desired objects (K)',
                  min_value=0,
                  max_value=N-1,
                  value=int(N/2),
                  step=1)
        
    n = st.slider(label='Number of items in the sample (n)',
                  min_value=0,
                  max_value=N-1,
                  value=int(N/4),
                  step=1)

    parameters = [N, K, n]
    
    return parameters
    
