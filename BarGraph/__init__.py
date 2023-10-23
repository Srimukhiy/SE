import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_bar_chart(data,xaxis,yaxis):
    #create the data ; 
    fig, ax = plt.subplots();
    grouped = data.groupby(xaxis)[yaxis].mean()
    # Find the category with the highest mean value
    max_category = grouped.idxmax()
    # Find the category with the least mean value
    min_category = grouped.idxmin();
    ax.bar(grouped.index, grouped.values);
    ax.set_xlabel(xaxis);
    ax.set_ylabel(yaxis);
    ax.set_title("graph between"+xaxis+" versus "+yaxis);
    desc="A graph is drawn between"+xaxis+" versus "+yaxis+"Highest marks of category "+max_category+" least "+yaxis+" with category "+min_category;
    return fig,desc