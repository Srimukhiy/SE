import streamlit as st; 
import time;
#to upload a file ; 
from switch_page import switch_page;
from TextTospeech import text_to_speech;
from SpechToText import input;
import AboutUs,ContactUs;


def wait():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def Home():
    st.title("Data Visualization");
    text_to_speech("Please Say Get started !! or press on screen");
    #get the input from voice commands 
    message = st.chat_message("assistant");
    message.write("Listening...");
    text = input();
    wait();
    user_message = st.chat_message("user");
    user_message.write(text);
    #creation of get started button to show all those
    if (st.button("Get started ", use_container_width=True) or (text and "start" in text)):  
        st.session_state['but_get_started'] = True;
        text_to_speech("Proceeding to next step to upload a file");
        wait();
        switch_page("fileupload");
    


# #desgning the pages into tabs for st.tabs
# tab1, tab2, tab3 = st.tabs(["Home", "AboutUs", "ContactUs"]);

#     Home();


Home();