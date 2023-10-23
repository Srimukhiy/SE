import streamlit as st
from streamlit_option_menu import option_menu
import AboutUs,ContactUs;
from pages import Home;
from switch_page import switch_page;

st.set_page_config(initial_sidebar_state="collapsed");

def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "AboutUs", "ContactUs","FileUpload","Charts"],  # required
        icons=["house", "book", "envelope","",""],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        styles={
                "container": {"padding": "10!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "28px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "10px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            })
    
    return selected

selected = streamlit_menu()


if selected == "Home":
    Home.Home();
if selected == "AboutUs":
    AboutUs.app();
if selected == "ContactUs":
    ContactUs.app();
if selected == "FileUpload":
    switch_page("fileupload");
    #fileupload.app();
if selected =="Charts":
    switch_page("charts");



