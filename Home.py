import streamlit as st
import sys

sys.path.append("./check_uniform")
sys.path.append("./check_in")



from check_uniform_app import check_uniform 
from check_in_app import check_in 



st.set_page_config(layout="wide", page_title="Image Background")

st.sidebar.success("Select a a tool below.")

page_names_to_funcs = {
    "Check Uniform": check_uniform,
    "Check Location": check_in,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()