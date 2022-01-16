import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from discrete import Binomial, DiscreteUniform, Bernoulli, Geometric, NegativeBinomial, Hypergeometric
from continuous import ContinuousUniform
from utils import CONTINUOUS_OPTIONS, DISCRETE_OPTIONS

st.title('Welcome to Distributed')
st.write("""
         Curious about probability distributions?\n
         Build a strong intuition by playing around and visualizing your experiemnts.\n
         Follow the steps below and don't forget to have fun.
         """)
# Continuous vs. distributions 
'## 1. Select the type of distribution'
distribution_type = st.radio(label='What type of distribution do you want to learn about?',
                    options=['Continuous', 'Discrete'])

f'## 2. Pick your favorite {distribution_type.lower()} distribution:'

# Continuous options:
if distribution_type == 'Continuous':
    selection = st.selectbox(label='Continuous Distribution',
                             options=CONTINUOUS_OPTIONS)
# Discrete Options: 
else:
    selection = st.selectbox(label='Discrete Distribution',
                             options=DISCRETE_OPTIONS)
   

# Play around with the parameters
parameters = eval(selection.replace(' ', '')).run()

f'## 3. See the Results'
eval(selection.replace(' ', '')).plot(*parameters)
