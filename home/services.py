import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="services", page_icon=":tada:", layout="wide")

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
    <meta name="viewport" content="initial-scale=1, width=device-width" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,200;0,300;0,400;0,500;0,600;0,800;1,800&display=swap"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Athiti:wght@700&display=swap" />
  </head>
"""
            , unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path + '/global1.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/services/services.css'

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
my_file = path + '/public/gameiconsexitdoor.png'

file_6 = open(my_file, "rb")
contents6 = file_6.read()
data_url6 = base64.b64encode(contents6).decode("utf-8")
file_6.close()

h = f"""
<div class="home">
      <div class="header">
        <div class="navigation">
          <a href="contact" target="_self" ><i class="i">من نحن </i></a>
          <div class="blog-navigation">
            <a href="" target="_self" ><i class="i1">المدونة</i></a>
          </div>
          <div class="features-navigation">
            <a href="services" target="_self"><i class="i2">الخدمات المميزة</i></a>
          </div>
          <div class="home-navigation">
            <a href="home" target="_self" ><i class="i3">الصفحة الرئسية </i></a>
            <header class="notification-area">
              <img class="notification-area-child" src="data:image/png;base64,{data_url}"/>
              <img class="status-bar-icon" src="data:image/png;base64,{data_url2}"/>
              <img class="logo-2-icon" src="data:image/png;base64,{data_url3}"/>
              <img class="tablerbell-icon" src="data:image/png;base64,{data_url4}"/>
              <img class="claritysettings-solid-icon" src="data:image/png;base64,{data_url5}"/>
            </header>
          </div>
        </div>
      </div>
      <div class="home-child"></div>
      <section class="frame-parent">
        <div class="rectangle-parent">
          <div class="frame-child"></div>
          <div class="div">
            <p class="p">
              احصل على استخدام غير محدود لجميع الأدوات و الوظائف بسعر ثابت.
            </p>
          </div>
          <div class="price-info">
            <div class="rectangle-group">
              <div class="frame-item"></div>
              <div class="monthly-cost">
                <div class="price">
                  <div class="div1">
                    <p class="p1">15ريال / شهرياً</p>
                    <p class="p2">(يتم تجديد العضوية تلقائيًا)</p>
                  </div>
                  <div class="subscription-button">
                    <div class="button-content">
                      <div class="button-shape"></div>
                      <div class="div2">ابدأ</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="trial-info">
                <div class="trial-info-child"></div>
                <div class="div3">
                  يمكنك التجربة لمدة 14 يومًا نظير تكلفة قدرها ‏0.99 ريال
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="close-button">
          <img class="game-iconsexit-door" loading="lazy" alt="" src="data:image/png;base64,{data_url6}" alt="cat svg"/>
        </div>
      </section>
    </div>"""

st.markdown(h, unsafe_allow_html=True)
