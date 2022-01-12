import streamlit as st

def distribution_function(start, end):
    n = end - start + 1
    return 1/n

def run():
    st.write("Hello it's Discrete Uniform")
    
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