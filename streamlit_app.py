import streamlit as st
import backend as be

st.header('ACS Varible Checker')

with open('description.md') as f:
    st.write(f.read())
    
var_name = st.text_input("ACS Variable Name: ", "B08006_017E")
                         
st.dataframe(be.get_labels_for_variable(var_name), hide_index=True)

st.write("Created by [Ari Lamstein](https://www.arilamstein.com). View the code [here](https://github.com/arilamstein/acs-var-checker).")