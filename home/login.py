import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="login", page_icon=":tada:", layout="wide")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


path = os.path.dirname(__file__)
my_file = path + '/login/global.css'

local_css(my_file)
path = os.path.dirname(__file__)
my_file = path + '/login/login.css'

local_css(my_file)

file_ = open(os.path.dirname(__file__)+"/public/log-in-screen@3x.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

file_2 = open(os.path.dirname(__file__)+"/public/rectangle-5.png", "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

file_3 = open(os.path.dirname(__file__)+"/public/image@2x.png", "rb")
contents3 = file_3.read()
data_url3 = base64.b64encode(contents3).decode("utf-8")
file_3.close()

file_4 = open(os.path.dirname(__file__)+"/public/rectangle-4.png", "rb")
contents4 = file_4.read()
data_url4 = base64.b64encode(contents4).decode("utf-8")
file_4.close()

file_5 = open(os.path.dirname(__file__)+"/public/logo-2@2x.png", "rb")
contents5 = file_5.read()
data_url5 = base64.b64encode(contents5).decode("utf-8")
file_5.close()

file_6 = open(os.path.dirname(__file__)+"/public/-1@2x.png", "rb")
contents6 = file_6.read()
data_url6 = base64.b64encode(contents6).decode("utf-8")
file_6.close()

st.markdown(
    f"""         <style>
    .stApp {{
                 background-image: url(data:image/png;base64,{data_url});
                 background-repeat: no-repeat;
                 background-size: cover;
                 background-attachment: scroll;
                 width: 100%;
             }}
             </style>
             """,
            unsafe_allow_html=True
        )
form = f"""
<div class="log-in-screen">
  <div class="main-container">
    <div class="parent">
      <h1 class="h1">مرحبا بكم</h1>
      <div class="form-container">
        <form action="home" class="auth-options" method="GET">
          <div class="input-area">
            <div class="phone-email-input">
              <div class="password-field">
              <div class="password-box"></div>
              <input class="password-box" type="email" name="email" placeholder="Your phone or email@gmail.com" required>
            </div>
              <div class="email-input">
                <img class="email-input-child" alt="" src="data:image/png;base64,{data_url2}" alt="cat png"/>
              </div>
            </div>
            <div class="password-field">
              <div class="password-box"></div>
              <input class="password-box" type="password" name="password" placeholder="Your password" required>
            </div>
          </div>
          <button class="auth-buttons1">
            <div class="auth-buttons-child"></div>
            <a href="home" target="_self" ><i class="i1">تسجيل دخول</i></a>
          </button>
          <button class="auth-buttons1">
            <div class="auth-buttons-item"></div>
            <a href="register" target="_self" ><i class="i1">إنشاء حساب</i></a>
          </button>
        </form>
      </div>
    </div>
  </div>
  <img class="image-icon" alt="" src="data:image/png;base64,{data_url3}" alt="cat png" />
  <div class="header">
    <img class="header-child" alt="" src="data:image/png;base64,{data_url4}" alt="cat png"/>
    <img class="logo-2-icon"  alt="" src="data:image/png;base64,{data_url5}" alt="cat png"/>
    <img class="icon"  alt="" src="data:image/png;base64,{data_url6}" alt="cat png"/>
  </div>
</div>
"""
st.markdown(form, unsafe_allow_html=True)
