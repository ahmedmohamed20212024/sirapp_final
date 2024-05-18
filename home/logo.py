import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container
from st_pages import show_pages_from_config, add_page_title, hide_pages
from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title="Welcome", page_icon=":tada:", layout="wide")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown(f"""
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="initial-scale=1, width=device-width" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Athiti:wght@700&display=swap"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;1,400&display=swap"/>
"""
            , unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path + '/global.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/logo/logo.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/public/logo-screen@3x.png'

file_ = open(my_file, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

path = os.path.dirname(__file__)
my_file = path + '/public/logo-3@2x.png'

file_2 = open(my_file, "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

st.markdown(
    f"""         <style>
    .stApp {{
                 background: url(data:image/png;base64,{data_url});
                 background-repeat: no-repeat;
                 background-size: cover;
                 background-attachment: scroll;
                 width: 100%;
             }}
             </style>
             """,
    unsafe_allow_html=True
)

# add_page_title()


show_pages(
    [
        Page("logo.py", "logo", "🏠"),
        Page("login.py", "login", "🏠"),
        Page("register.py", "register", "🏠"),
        Page("contact.py", "contact", "🏠"),
        Page("home.py", "home", "🏠"),
        Page("cv_home.py", "cv_home", "🏠"),
        Page("cv_details.py", "cv_details", "🏠"),
        Page("services.py", "services", "🏠"),
    ]
)

h = f"""
<div class="logo-screen">
<a href="login" width="100%" height="600px">
    <img class="logo-3-icon" alt="" src="data:image/png;base64,{data_url2}" />
</a>
</div>
"""

st.markdown(h, unsafe_allow_html=True)
