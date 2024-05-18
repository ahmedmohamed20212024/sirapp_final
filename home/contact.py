import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="contact", page_icon=":tada:", layout="wide")

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
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,200;0,300;0,400;0,500;0,600;0,800;1,800&display=swap"/>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Athiti:wght@700&display=swap" />
  </head>
"""
            , unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path + '/global.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/contact/contact.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/public/rectangle-41.png'

file_ = open(my_file, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

path = os.path.dirname(__file__)
my_file = path + '/public/vector1.png'

file_2 = open(my_file, "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

path = os.path.dirname(__file__)
my_file = path + '/public/claritysettingssolid.png'

file_3 = open(my_file, "rb")
contents3 = file_3.read()
data_url3 = base64.b64encode(contents3).decode("utf-8")
file_3.close()

path = os.path.dirname(__file__)
my_file = path + '/public/vector-1.png'

file_4 = open(my_file, "rb")
contents4 = file_4.read()
data_url4 = base64.b64encode(contents4).decode("utf-8")
file_4.close()

path = os.path.dirname(__file__)
my_file = path + '/public/logo-21@2x.png'

file_5 = open(my_file, "rb")
contents5 = file_5.read()
data_url5 = base64.b64encode(contents5).decode("utf-8")
file_5.close()

path = os.path.dirname(__file__)
my_file = path + '/public/group.png'

file_6 = open(my_file, "rb")
contents6 = file_6.read()
data_url6 = base64.b64encode(contents6).decode("utf-8")
file_6.close()

path = os.path.dirname(__file__)
my_file = path + '/public/rectangle-12@2x.png'

file_7 = open(my_file, "rb")
contents7 = file_7.read()
data_url7 = base64.b64encode(contents7).decode("utf-8")
file_7.close()


path = os.path.dirname(__file__)
my_file = path + '/public/vector-2.png'

file_8 = open(my_file, "rb")
contents8 = file_8.read()
data_url8 = base64.b64encode(contents8).decode("utf-8")
file_8.close()


path = os.path.dirname(__file__)
my_file = path + '/public/vector-3.png'

file_9 = open(my_file, "rb")
contents9 = file_9.read()
data_url9 = base64.b64encode(contents9).decode("utf-8")
file_9.close()

path = os.path.dirname(__file__)
my_file = path + '/public/fontistoinstagram.png'

file_10 = open(my_file, "rb")
contents10 = file_10.read()
data_url10 = base64.b64encode(contents10).decode("utf-8")
file_10.close()


path = os.path.dirname(__file__)
my_file = path + '/public/dashiconslinkedin.png'

file_11 = open(my_file, "rb")
contents11 = file_11.read()
data_url11 = base64.b64encode(contents11).decode("utf-8")
file_11.close()


path = os.path.dirname(__file__)
my_file = path + '/public/fabrandstiktok.png'

file_12 = open(my_file, "rb")
contents12 = file_12.read()
data_url12 = base64.b64encode(contents12).decode("utf-8")
file_12.close()

h = f"""<div class="home-screen">
      <img class="home-screen-child" alt="" src="data:image/png;base64,{data_url}" alt="cat svg" />
      <textarea class="home-screen-item" rows="{12}" cols="{20}"> </textarea>
      <div class="main-content">
        <div class="main-content-inner">
          <div class="nav-icon-parent">
            <img class="nav-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url2}" alt="cat svg" />
            <img class="claritysettings-solid-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg"/>
            <div class="logo-area">
              <img class="change-your-password" alt="" src="data:image/png;base64,{data_url4}" alt="cat svg"/>
            </div>
          </div>
        </div>
        <img class="logo-2-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url5}" alt="cat svg" />
      </div>
      <main class="footer">
        <section class="card-small"></section>
        <section class="bottom-bar-parent">
          <div class="bottom-bar"></div>
          <img class="frame-child" loading="lazy" alt="" />
          <div class="mada">Mada</div>
          <h2 class="h2">مدى</h2>
          <h2 class="h21">روابط مهمة</h2>
          <h2 class="h22">اتصل بنا</h2>
          <h2 class="h23">السيرة الذاتية الاحترافية © 2024</h2>
          <input class="name-input" placeholder="الاسم" type="text" />
          <textarea class="message-box" placeholder="الرسالة" rows="{5}" cols="{16}">
          </textarea>
          <input class="email-box" placeholder="الإيميل" type="text" />
          <div class="submit-button">
            <div class="submit-button-child"></div>
            <i class="i" id="text11">إرسال</i>
            <div class="group-wrapper">
              <img class="group-icon" alt="" src="data:image/png;base64,{data_url6}" alt="cat svg" />
            </div>
          </div>
          <i class="i1">
            <p class="p">من نحن</p>
          </i>
          <i class="i2">المدونة</i>
          <i class="i3">سياسة الخصوصية </i>
          <i class="i4">الشروط والأحكام</i>
          <div class="social-media-bar">
            <img class="social-media-bar-child" alt="" src="data:image/png;base64,{data_url7}" alt="cat svg" />
            <button class="rivisa-fill">
              <img class="visa-icon-shape" alt="" src="data:image/png;base64,{data_url8}" alt="cat svg" />
            </button>
            <img class="social-media-bar-item" loading="lazy" alt="" />
            <div class="ioncard">
              <img class="unsubcribed-to-all" alt="" src="data:image/png;base64,{data_url9}" alt="cat svg" />
            </div>
            <img class="fontistoinstagram-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url10}" alt="cat svg" />
            <img class="dashiconslinkedin" loading="lazy" alt="" src="data:image/png;base64,{data_url11}" alt="cat svg"/>
            <img class="fa-brandstiktok-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url12}" alt="cat svg"/>
          </div>
          <h2 class="h24">التواصل الاجتماعي</h2>
          <i class="i5">المراجعات</i>
        </section>
      </main>
    </div>
    """
st.markdown(h, unsafe_allow_html=True)
