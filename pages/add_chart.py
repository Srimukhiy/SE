import streamlit as st; 
from pages.connect_to_db import connect;
#add the name of the charts; 
def create_charttable(c):
	#c.execute('drop table chart')
	c.execute('CREATE TABLE IF NOT EXISTS chart(chartname TEXT,description TEXT, visibility TEXT)')
def add_chartdata(chartname,desc, visibility,c,conn):
	c.execute('INSERT INTO chart(chartname,description,visibility) VALUES (?,?,?)',(chartname,desc,visibility))
	conn.commit()
st.subheader("Additon of charts ");

c,conn = connect.connection();
chartname = st.text_input("name_of_the_chart");
if chartname==None or len(chartname)==0:
	st.error("chartname is mandatory")
desc = st.text_input("description about the chart");
if desc==None or len(desc)==0:
	st.error("chart description is mandatory");
visibility  = st.radio("select user visibility for this graph",["True", "False"],index=None);
if visibility==None:
	 st.error("please select true/false");
if st.button("add") and chartname and desc and visibility:
	create_charttable(c);
	add_chartdata(chartname,desc,visibility,c,conn)
	st.success("chart added succeefully")
	
