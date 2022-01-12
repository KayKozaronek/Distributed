import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from discrete import Binomial, DiscreteUniform
from continuous import ContinuousUniform
from utils import CONTINUOUS_OPTIONS, DISCRETE_OPTIONS

st.title('Welcome to Distributed')

# Continuous vs. distributions 
'## Select the type of distribution'
distribution_type = st.radio(label='What type of distribution do you want to learn about?',
                    options=['Continuous', 'Discrete'])

f'## Pick your favorite {distribution_type.lower()} distribution:'

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

eval(selection.replace(' ', '')).plot(*parameters)
