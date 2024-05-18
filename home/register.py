import os

from streamlit_extras.stylable_container import stylable_container
import streamlit as st
from PIL import Image
import base64


st.set_page_config(page_title="register", page_icon=":tada:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


path = os.path.dirname(__file__)
my_file = path + '/register/global.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/register/register.css'

local_css(my_file)


file_ = open(os.path.dirname(__file__)+"/public/logo-3@2x.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_2 = open(os.path.dirname(__file__)+"/public/log-in-screen2@3x.png", "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

st.markdown(
    f"""
     <style>
     .stApp {{
         background: url(data:image/png;base64,{data_url2});
         background-repeat: no-repeat;
         background-size: cover;
         background-attachment: scroll;
     }}
     </style>
     """,
    unsafe_allow_html=True,
)


form = f"""
<div class="log-in-screen2">
      <img class="logo-2-icon" alt="" src="data:image/png;base64,{data_url}" alt="cat png" />
      <section class="main-container">
        <form action="home" class="content-area" method="GET">
          <div class="form-container">
            <div class="input-fields">
              <div class="credentials">
                <div class="email-field"></div>
                <input class="email_" placeholder="Phone number or email@gmail.com " type="email" required/>
              </div>
              <div class="name-field">
                <div class="name-field-child"></div>
                <input class="full-name" placeholder="Full Name " type="text" required/>
              </div>
            </div>
            <div class="username-field">
              <div class="username-input"></div>
              <input class="usernames" placeholder="Usernames" type="text" required/>
            </div>
          </div>
          <div class="password-field">
            <div class="password-input-area">
              <div class="password-entry"></div>
              <input class="password" placeholder="password" type="password" required/>
            </div>
            <div class="submit-button-area">
              <button class="rectangle-parent">
                <div class="frame-child"></div>
                <a href="home" target="_self" >
                <i class="i">التالي</i>
                </a>
              </button>
            </div>
          </div>
        </form>
      </section>
    </div>
"""
st.markdown(form, unsafe_allow_html=True)
