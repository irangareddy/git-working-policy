import streamlit as st

from git_working_policy.app.branch_name_view import branch_name_view
from git_working_policy.app.welcome import welcome_view

page_names_to_funcs = {
    "—": welcome_view,
    "Branch Name": branch_name_view,
}

demo_name = st.sidebar.selectbox("Choose a option", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
