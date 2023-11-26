import streamlit as st; 
from pages.connect_to_db import connect;
import time;
from switch_page import switch_page;
#this page is created to show which graphs were fullly developed using 
#step 1 --create a table and then show the rows over the db.
#step2 -- create a connection and then cccess the charts ; 


def submit():

    msg = st.toast("Working on changes");
    time.sleep(2);
    msg.toast("Deploying changes ...");
    time.sleep(2);
    msg.toast("Deployment successfull");
    time.sleep(2);


# def create_charttable(c):
# 	c.execute('CREATE TABLE IF NOT EXISTS chart(chartname TEXT,visibility TEXT)')
# def add_chartdata(chartname,visibility,c,conn):
# 	c.execute('INSERT INTO chart(chartname,visibility) VALUES (?,?)',(chartname,visibility))
# 	conn.commit(c)

def view_all_charts(c):
	c.execute('SELECT * FROM chart');
	data = c.fetchall()
	return data

st.info("if we remove the graph from here, reflects to the user ");
#read the charts and display the details on the

def insert_changes(c,conn,options,all_graphs):
    for i in all_graphs:
        if i in options:
            c.execute('update chart set visibility = "True" '+ ' where chartname="'+i+'"');
            conn.commit();
        else:
            c.execute('update chart set visibility ="False" '+' where chartname="'+i+'"');
            conn.commit();

def start():
    #connect to db;
    if st.button('+charts'):
        switch_page('add_chart')
    c,conn = connect.connection();
    # c.execute('DELETE FROM chart');
    # conn.commit();
    data = view_all_charts(c); 
    print(data)
    #for first time we insert the data into the table; 
    #get the chart detials; 
    #to display all the types of charts 
    selection_graphs=[];all_graphs=[];
    for i,j,k in data:
        if k == 'True':
            selection_graphs.append(i);
        all_graphs.append(i);
    options = st.multiselect(
    'graphs to be displayed to user',
    all_graphs,selection_graphs);

    if st.button("Submit"):
        print(options);
        #nert into the session variables
        #inert or change the data visibility to true or false.
        #to insert the 
        insert_changes(c,conn,options,all_graphs);
        data = view_all_charts(c); 
        
    st.session_state['charts_visibility'] = options;
    
    
start();