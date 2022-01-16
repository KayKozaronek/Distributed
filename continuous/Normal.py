import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 


def distribution_function(mean, variance, x):
    return 1 / np.sqrt(variance * 2 * np.pi) * np.exp(-(x - mean)**2 / (2*variance)) 

def plot(mean, variance):
    term = 4*np.sqrt(variance)
    # plot_range_1 = [mean - term, mean + term] 
    plot_range_2 = [-50, 50]
    x = np.arange(plot_range_2[0], plot_range_2[1], 0.01)
    fig, ax = plt.subplots()
    ax.plot(x, distribution_function(mean, variance, x))
    
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value of Random Variable')
    ax.set_ylabel('Probability ')

    st.pyplot(fig)

# @st.cache
def run():    
    # Parameter Sliders 
    mean = st.slider(label='Set the center of your distribution (mean)',
                  min_value=-50,
                  max_value=50,
                  value=0,
                  step=1)
    
    variance = st.slider(label='This parameter determines the spread of your data (Variance)',
                  min_value=0,
                  max_value=100,
                  value=25,
                  step=1)

    parameters = [mean, variance]
    
    return parameters
    
