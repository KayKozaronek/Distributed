import streamlit as st
import numpy as np
import plotly.express as px 

def distribution_function(start, end):
    return np.repeat(1/(end-start), 1000)

def plot(start, end, block_plot):
    if block_plot:
        pass
    else:
        xs = np.linspace(start, end, 1000)
        fig = px.area(x=xs,
                 y=distribution_function(start, end),
                 title= f'Continuous Uniform Distribution', 
                 labels={
                    "x": "Value of Random Variable X",
                    "y": "Probability",
                    })

    st.plotly_chart(fig) 
        

def run():    
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