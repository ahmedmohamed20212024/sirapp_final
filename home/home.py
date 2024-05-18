import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="home", page_icon=":tada:", layout="wide")

st.markdown(
    f"""         <style>
    .stApp {{
                
                 background-repeat: no-repeat;
                 background-size: cover;
                 background-attachment: scroll;
                 width: 100%;
             }}
             </style>
             """,
    unsafe_allow_html=True
)


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown(f"""
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,200;0,300;0,400;0,500;0,600;0,800;1,800&display=swap" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Athiti:wght@700&display=swap" />
</head>"""
            , unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path + '/global.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/home/home.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/public/rectangle-4.png'

file_ = open(my_file, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

path = os.path.dirname(__file__)
my_file = path + '/public/vector.png'

file_2 = open(my_file, "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

path = os.path.dirname(__file__)
my_file = path + '/public/logo-2@2x.png'

file_3 = open(my_file, "rb")
contents3 = file_3.read()
data_url3 = base64.b64encode(contents3).decode("utf-8")
file_3.close()

path = os.path.dirname(__file__)
my_file = path + '/public/tablerbell.png'

file_4 = open(my_file, "rb")
contents4 = file_4.read()
data_url4 = base64.b64encode(contents4).decode("utf-8")
file_4.close()

path = os.path.dirname(__file__)
my_file = path + '/public/claritysettingssolid.png'

file_5 = open(my_file, "rb")
contents5 = file_5.read()
data_url5 = base64.b64encode(contents5).decode("utf-8")
file_5.close()

path = os.path.dirname(__file__)
my_file = path + '/public/image@2x.png'

file_6 = open(my_file, "rb")
contents6 = file_6.read()
data_url6 = base64.b64encode(contents6).decode("utf-8")
file_6.close()

path = os.path.dirname(__file__)
my_file = path + '/public/group-1.png'

file_7 = open(my_file, "rb")
contents7 = file_7.read()
data_url7 = base64.b64encode(contents7).decode("utf-8")
file_7.close()

h = f"""<div class="home-screen">
      <div class="main-container">
        <div class="parent">
          <a href="contact" target="_self" ><i class="i">من نحن </i></a>
          <div class="wrapper">
            <a href="" target="_self" ><i class="i1">المدونة</i></a>
          </div>
          <div class="container"><a href="services" target="_self"><i class="i2">الخدمات المميزة</i></a>
          </div>
          <a href="home" target="_self" ><i class="i3">الصفحة الرئسية </i></a>
        </div>
      </div>
      <main class="notification-area">
        <img class="notification-area-child" alt="" src="data:image/png;base64,{data_url}" alt="cat svg"/>
        <img class="inputorginal-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url2}" alt="cat svg"/>
        <img class="logo-2-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url3}" alt="cat png"/>
        <img class="tablerbell-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url4}" alt="cat svg"/>
        <img class="claritysettings-solid-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url5}" alt="cat svg"/>
        <img class="image-icon" alt="" src="data:image/png;base64,{data_url6}" alt="cat png" />
      </main>
      <h1 class="cv">أنشئ cv مثالي </h1>
      <div class="c-v-step-container-parent">
        <div class="c-v-step-container">
          <div class="instruction-panel">
            <div class="instruction-panel-child"></div>
            <div class="div">
              املأ التفاصيل الخاصة بك، واختر القالب المناسب،
            </div>
            <div class="download-step">
              <div class="div1">ثم قم بتنزيل سيرتك الذاتية على الفور.</div>
            </div>
          </div>
          <div class="action-button-container">
            <div class="action-button-panel">
              <div class="action-button"></div>
              <div class="div2"><a href="cv_home" target="_self" ><i class="i2">إنشاء سيرة ذاتية </i></a></div>
            </div>
          </div>
        </div>
        <div class="assistant-container-wrapper">
          <div class="assistant-container">
            <div class="assistant-content">
              <div class="input-container">
                <div class="input-container-child"></div>
                <div class="input-area">
                  <div class="rectangle-parent">
                    <div class="frame-child"></div>
                    <b class="b">أطلب مني شىء.....</b>
                  </div>
                </div>
                <img class="input-container-item" loading="lazy" alt="" src="data:image/png;base64,{data_url7}" alt="cat svg" />
                </div>
              <div class="div3">
                <p class="blank-line">&nbsp;</p>
                <p class="blank-line1">&nbsp;</p>
                <p class="blank-line2">&nbsp;</p>
                <p class="p">
                  الوحيد الذي يقدم خاصية الاستعداد للمقابلة الوظيفية بمساعدة
                  الذكاء الاصطناعي
                </p>
                <p class="p1">و نماذج سيرة ذاتية مميزة</p>
              </div>
            </div>
            <div class="a-i-panel">
              <h1 class="ai">AI</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    """

st.markdown(h, unsafe_allow_html=True)
