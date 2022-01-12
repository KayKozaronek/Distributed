import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def distribution_function(start, end):
    return np.repeat(1/(end-start), 1000)

def plot(start, end, block_plot):
    if block_plot:
        pass
    else:
        xs = np.linspace(start, end, 1000)
        fig, ax = plt.subplots()
        ax.plot(xs, distribution_function(start, end))
        
        ax.set_title('Continuous Uniform Distribution')
        ax.set_xlabel('Number of X successes')
        ax.set_ylabel('Probability of seing X successes')

        st.pyplot(fig)


def run():
    st.write("Hello it's Discrete Uniform")
    
    # Short Description 
    # st.write("""
    #          DESCRIPTION NEEDED
    #          """)
    
    # Parameter Sliders 
   
    start = st.slider(label='Starting point',
                  min_value=0.0,
                  max_value=100.0,
                  value=0.1,
                  step=0.1)
    
    end = st.slider(label='End point',
                    min_value = 0.0,
                    max_value=100.0,
                    value = 10.0,
                    step=0.1)

    if start > end:
        end = start + 10 
        st.write('Choose another end point. Your endpoint should be larger than your starting point')
        block_plot = True
    else: 
        block_plot = False
    
    parameters = [start, end, block_plot]
    
    return parameters