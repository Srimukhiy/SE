import streamlit as st;
import pandas as pd;
#to upload the file . 
#create a session varbale fileuploaded successfully;
#audio output text to speech 
from switch_page import switch_page;
from TextTospeech import text_to_speech;
from SpechToText import input;


def fileupload():
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        text_to_speech("File uploaded successfully");
        st.success("File uploaded successfully!");
        
        st.session_state["file_uploaded"] = True
        file_details = {"Filename": uploaded_file.name, "Filesize": uploaded_file.size, "Filetype": uploaded_file.type}
        st.success(file_details);
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file);
        #create or push into session variable 
        
        st.session_state['dataframe']= df;
        # Display the data from the CSV file
        st.write("Data from the uploaded file:")
        st.write(df);
        #input the speech such as bar graph or pie chart or line graph;
        text_to_speech("Say Charts  to proceed furthur")
        message = st.chat_message("assistant");
        message.write("Listening...");
        text2 = input();
        if text2:
            umessage = st.chat_message("user");
            umessage.write(text2);
        
        if text2 and "chart" in text2:
            switch_page("charts");
        else:
            if st.button("Charts Visualization",use_container_width=True):
                switch_page("charts");

def app():    
    if 'but_get_started' in st.session_state:
        if 'file_uploaded' not in st.session_state:
            st.session_state.file_uploaded = False
        fileupload();
    else:
        switch_page("NavBar");

app();


