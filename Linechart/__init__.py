import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_line_chart(data,yaxis):
    #create the data; 
    fig, ax = plt.subplots();
    print(data.index);
    ax.plot(list(data.index), list(data[yaxis]),marker='o');
    xaxis = 'Student Index';
    ax.set_xlabel('StudentIndex')
    ax.set_ylabel(yaxis);
    ax.set_title("Line graph on "+xaxis+"versus"+yaxis);
    desc="A Line graph is drawn between"+xaxis+"versus"+yaxis +" can see the trend and understand it";
    return fig,desc