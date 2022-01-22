import streamlit as st
import pandas as pd
import plotly.express as px
from discrete import DiscretePlot

def distribution_function(p):
    return [(1-p), p]

p = st.slider(label='Probability of Success',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.5,
                  step=0.01)


DiscretePlot.plot(p, distribution_fuction= distribution_function )