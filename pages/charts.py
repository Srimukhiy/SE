import streamlit as st;
from BarGraph import render_bar_chart;
from switch_page import switch_page;
import time;
from SpechToText import input;
from TextTospeech import text_to_speech;
from Piechart import render_pie_chart;
from Linechart import render_line_chart;
from pages.connect_to_db import connect;
st.set_page_config(initial_sidebar_state="collapsed");
#to display the charts for the file uploaded.
def wait():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def to_get_charts_names_visible():
    #to get the charts names visible
    #step1 connect to db 
    #step2 to get the details
    #step 3 get the names with only true visibility
    c,conn = connect.connection();
    #get the names with 
    c.execute('select chartname from chart where visibility = "True"');
    data = c.fetchall();
    res=[];
    for i in data:
        res.append(i[0]);
    return res;

def charts_plotting():
    if "file_uploaded" in st.session_state and st.session_state.file_uploaded == True:
        #to disply the type of chart and print it
        flag=0;
        #input the voce command --------and then proceed for sleection of chart;
        st.header("Graphs Visualization");
        #st.progress to be used here while displayng the charts ;
        #choose 1 for brgraph , 2 pie chart and 3 for line graph;
        res = to_get_charts_names_visible();
        text_to_speech("Please Say Name Of graph u like to visualze from Bar,  Pie and Line");
        #get the input from voice commands 
        message = st.chat_message("assistant");
        message.write("Listening...");
        text2 = input();
        wait();
        user_message = st.chat_message("user");
        user_message.write(text2);
        graph = st.radio("Choose the graph Type to Visualize👇",res,key="visibility",
        label_visibility="visible",
        disabled=False,index=None,
        horizontal=True);
        #Listening code with bot for voice commmands 
        df = st.session_state['dataframe'];
        if (text2 and "bar" in text2) or graph == "BarGraph":
            #show the columsn to be selected .. 
            #pick the x-axis column for the visualization 
            #get the data frame 
    
            xaxis = st.selectbox("X-axis columns to be selected ",("gender","race/ethnicity","parental level of education","lunch"));
            yaxis = st.selectbox("Y-axis columns to be selected",("math score","reading score","writing score"));

            st.header("Bargraph is slected");

            fig,desc = render_bar_chart(df,xaxis,yaxis);
            
            st.pyplot(fig);
            text_to_speech(desc);
            wait();
            message = st.chat_message("assistant");
            message.write(desc);
        elif graph == "piechart" or ( text2 and "pie" in text2):
            xaxis = st.selectbox("selcet a column on which pie chart to be selected ",("gender","race/ethnicity","parental level of education","lunch","test preparation course"));
            fig,desc = render_pie_chart(df,xaxis);
            st.pyplot(fig);
            text_to_speech(desc);
            wait();
            message = st.chat_message("assistant");
            message.write(desc);

        elif graph =="LineGraph":
            yaxis = st.selectbox("select a column on which u want to apply the line graph ",("math score","reading score","writing score"));
            
            fig,desc = render_line_chart(df,yaxis);
            st.pyplot(fig);
            text_to_speech(desc);
            wait();
            message = st.chat_message("assistant");
            message.write(desc);
    
    elif "but_get_started" in st.session_state and st.session_state['but_get_started']==True:
        switch_page("fileupload");
    else:
        switch_page("NavBar");
charts_plotting(); 