import streamlit as st;
import matplotlib.pyplot as plt

def render_pie_chart(data,xaxis):
    category_counts = data[xaxis].value_counts()
    max_count = category_counts.max()

# Calculate the minimum count percentage
    min_count = category_counts.min()
    total_count = category_counts.sum()
    min_count_percentage = (min_count / total_count) * 100
    max_count_percentage = (max_count/total_count)*100;
    least_category = category_counts.idxmin()
    highest_category = category_counts.idxmax()

    fig, ax = plt.subplots()
    category_counts.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    ax.axis('equal');
    desc = " pie chart is drawn for the column "+xaxis+"with the  "+highest_category+"of percentage "+str(round(max_count_percentage,1))+" with least category of "+least_category+"of percentage"+str(min_count_percentage);
    return fig,desc;

