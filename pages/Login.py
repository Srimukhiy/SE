# DB Management
import sqlite3 
import streamlit as st;
import pandas as pd;
import hashlib
import time;
from switch_page import switch_page;
from pages.connect_to_db import connect;
import re;
st.set_page_config(initial_sidebar_state="collapsed");  
def validate_password(password):  
    if len(password) < 8:  
        return "Minimum length of 8 characters" 
    if not re.search("[a-z]", password):  
        return "one letter between[a-z]"  
    if not re.search("[A-Z]", password):  
        return "minimum one capital letter"
    if not re.search("[0-9]", password):  
        return "a number is must to be in password"
    return "True"

def create_usertable(c):
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def add_userdata(username,password,c,conn):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()
def login_user(username,password,c):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
def view_all_users(c):
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
def main():
	# conn = sqlite3.connect('data.db')
	# c = conn.cursor();
	c,conn = connect.connection()
	menu = ["Login","SignUp"]
	choice = st.selectbox("",menu)
	if choice == "Home":
		st.subheader("Home")
	elif choice == "Login":
		st.subheader("Login Section")
		username = st.text_input("UserName")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			with st.spinner('Wait for it...'):
				time.sleep(1)
			# if password == '12345':
			create_usertable(c)
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd),c)
			if result:
				st.success("Logged In as {}".format(username));
				addcharts , configurechart = st.columns(2);
				switch_page("Configure_charts");

			else:
				st.warning("Incorrect Username/Password")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		#add the password validation to check whether constraints were ssatisfied.
		val = validate_password(new_password) 
		if val and val!="True":
			st.error(val);
		elif val and val=="True":
			st.success(" password is valid !!");
		if st.button("Signup") and val and val=="True":
			create_usertable(c)
			add_userdata(new_user,make_hashes(new_password),c,conn)
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")
main();