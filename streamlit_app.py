import streamlit as st
import backend as be

st.header('ACS Varible Checker')

with open('description.md') as f:
    st.write(f.read())
    
col1, col2 = st.columns(2)
with col1:
    var_name = st.text_input("ACS Variable Name: ", "B08006_017E")

with col2:
    acs = st.selectbox("Select ACS: ", [1, 5])

st.dataframe(be.get_labels_for_variable(var_name, acs), hide_index=True)

st.write("Created by [Ari Lamstein](https://www.arilamstein.com). View the code [here](https://github.com/arilamstein/acs-var-checker).")