import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def distribution_function(start, end):
    return 1/(end-start)

def run():
    st.write("Hello it's Continuous Uniform")
    
    # Short Description 
    st.write("""
             DESCRIPTION NEEDED
             """)
    
    # Parameter Sliders 
    start = st.slider(label='Starting point',
                  min_value=0.0,
                  max_value=1.0,
                  value=0.1,
                  step=0.01)
    end = st.slider(label='End point',
                    min_value = 0.0,
                    max_value=1.0,
                    value=0.9,
                    step=0.01)
    
    parameters = [start, end]
    
    return distribution_function, parameters
    
