import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="cv_home", page_icon=":tada:", layout="wide")

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
my_file = path + '/cv_home/global.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/cv_home/cv_home.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/public/mdiarrowleftbold.png'

file_ = open(my_file, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

path = os.path.dirname(__file__)
my_file = path + '/public/group.png'

file_2 = open(my_file, "rb")
contents2 = file_2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file_2.close()

path = os.path.dirname(__file__)
my_file = path + '/public/mingcuteeditfill.png'

file_3 = open(my_file, "rb")
contents3 = file_3.read()
data_url3 = base64.b64encode(contents3).decode("utf-8")
file_3.close()

path = os.path.dirname(__file__)
my_file = path + '/public/template-4@2x.png'

file_4 = open(my_file, "rb")
contents4 = file_4.read()
data_url4 = base64.b64encode(contents4).decode("utf-8")
file_4.close()

path = os.path.dirname(__file__)
my_file = path + '/public/rectangle-42.png'

file_5 = open(my_file, "rb")
contents5 = file_5.read()
data_url5 = base64.b64encode(contents5).decode("utf-8")
file_5.close()

path = os.path.dirname(__file__)
my_file = path + '/public/claritysettingssolid.png'

file_6 = open(my_file, "rb")
contents6 = file_6.read()
data_url6 = base64.b64encode(contents6).decode("utf-8")
file_6.close()

path = os.path.dirname(__file__)
my_file = path + '/public/tablerbell.png'

file_7 = open(my_file, "rb")
contents7 = file_7.read()
data_url7 = base64.b64encode(contents7).decode("utf-8")
file_7.close()


path = os.path.dirname(__file__)
my_file = path + '/public/vector.png'

file_8 = open(my_file, "rb")
contents8 = file_8.read()
data_url8 = base64.b64encode(contents8).decode("utf-8")
file_8.close()


path = os.path.dirname(__file__)
my_file = path + '/public/logo-2@2x.png'

file_9 = open(my_file, "rb")
contents9 = file_9.read()
data_url9 = base64.b64encode(contents9).decode("utf-8")
file_9.close()


h = f"""<div class="home-screen2">
      <div class="home-screen2-inner">
        <div class="group">
          <a href="contact" target="_self" ><h3 class="h3">من نحن</h3></a>
          <div class="frame">
            <a href="" target="_self" ><h3 class="h31">المدونة</h3></a>
          </div>
          <div class="frame-div">
            <a href="services" target="_self"><h3 class="h32">الخدمات المميزة</h3></a>
          </div>
          <a href="home" target="_self" ><h3 class="h33">الصفحة الرئسية</h3></a>
        </div>
      </div>
      <main class="frame-group">
        <section class="frame-container">
          <div class="mingcutedownload-line-parent">
            <div class="mingcutedownload-line"></div>
            <div class="mdiarrow-left-bold-wrapper">
              <img class="mdiarrow-left-bold-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url}" alt="cat svg"/>
            </div>
            <div class="parent1">
              <h2 class="h25">السيرة الذاتية</h2>
              <div class="profile-divider"></div>
              <img  class="group-icon1" loading="lazy" alt="" src="data:image/png;base64,{data_url2}" alt="cat svg"/>
            </div>
          </div>
          <img class="line-icon" loading="lazy" alt="" />
          <div class="frame-child1"></div>
          <div class="frame-child2"></div>
          <div class="frame-child3"></div>
          <div class="frame-parent1">
            <div class="frame-wrapper">
              <div class="frame-parent2">
                <div class="frame-parent3">
                  <div class="frame-wrapper1">
                    <div class="frame-parent4">
                      <div class="wrapper1">
                        <div class="div8"><a href="cv_details" target="_self" >التفاصيل الشخصية </a></div>
                      </div>
                      <img class="mingcuteedit-fill-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg"/>
                    </div>
                  </div>
                  <img class="details-divider-icon" alt="" />
                </div>
                <div class="frame-wrapper2">
                  <div class="frame-parent5">
                    <div class="frame-wrapper3">
                      <div class="parent2">
                        <div class="div9">الملف التعريفي</div>
                        <img class="mingcuteedit-fill-icon1" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg" />
                      </div>
                    </div>
                    <img class="profile-divider-icon" loading="lazy" alt="" />
                    <div class="frame-wrapper4">
                      <div class="frame-parent6">
                        <div class="wrapper2">
                          <div class="div10">الخبرة العملية</div>
                        </div>
                        <img class="mingcuteedit-fill-icon2" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="frame-parent7">
                  <div class="frame-wrapper5">
                    <div class="k-views-parent">
                      <img class="k-views-icon" alt="" />
                      <div class="frame-wrapper6">
                        <div class="frame-parent8">
                          <div class="wrapper3">
                            <div class="div11">المؤهلات الدراسية</div>
                          </div>
                          <img class="mingcuteedit-fill-icon3" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="certification-divider-parent">
                    <img class="certification-divider-icon" loading="lazy" alt="" />
                    <div class="frame-wrapper7">
                      <div class="frame-parent9">
                        <div class="wrapper4">
                          <div class="div12">الشهادات</div>
                        </div>
                        <img class="mingcuteedit-fill-icon4" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="line-parent">
                  <img class="frame-child4" alt="" />
                  <div class="frame-wrapper8">
                    <div class="frame-parent10">
                      <div class="wrapper5">
                        <div class="div13">المهارات</div>
                      </div>
                      <img class="mingcuteedit-fill-icon5" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg"/>
                    </div>
                  </div>
                </div>
                <div class="line-group">
                  <img class="frame-child5" alt="" />
                  <div class="frame-wrapper9">
                    <div class="frame-parent11">
                      <div class="wrapper6">
                        <div class="div14">
                          <p class="p6">اللغات</p>
                        </div>
                      </div>
                      <img class="mingcuteedit-fill-icon6" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg"/>
                    </div>
                  </div>
                </div>
                <div class="frame-wrapper10">
                  <div class="visit-website-parent">
                    <img class="visit-website-icon" loading="lazy" alt="" />
                    <div class="frame-wrapper11">
                      <div class="frame-parent12">
                        <div class="wrapper7">
                          <div class="div15">الهوايات</div>
                        </div>
                        <img class="mingcuteedit-fill-icon7" alt="" src="data:image/png;base64,{data_url3}" alt="cat svg"/>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <img class="template-4-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url4}" alt="cat svg"/>
          </div>
        </section>
        <div class="frame-parent13">
          <div class="bubbles-parent">
            <div class="bubbles"></div>
            <div class="bubbles1"></div>
            <div class="bubbles2"></div>
            <div class="frame-child6"></div>
          </div>
          <div class="wrapper8">
            <h1 class="h1">كيف يعمل</h1>
          </div>
          <div class="pointers">
            <div class="frame-parent14">
              <div class="step-number-wrapper">
                <div class="step-number">1</div>
              </div>
              <div class="div16">
                <p class="blank-line3">&nbsp;</p>
                <p class="p7">ملء الحقول الفارغة</p>
                <p class="p8">
                  ابدأ بملء المعلومات ذات الصلة في سيرتك الذاتية.
                </p>
              </div>
            </div>
            <div class="choose-template-step">
              <div class="frame-parent15">
                <div class="step-number-container">
                  <div class="step-number1">2</div>
                </div>
                <div class="div17">
                  <p class="p9">اختر نموذجًا</p>
                  <p class="p10">اختر نموذجًا وخصِّصه حسب صفاتك الشخصية.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="frame-wrapper12">
            <div class="frame-parent16">
              <div class="step-number-frame">
                <div class="step-number2">3</div>
              </div>
              <div class="div18">
                <p class="p11">نزِّل سيرتك الذاتية</p>
                <p class="p12">
                  نزِّل سيرتك الذاتية وحرِّرها بعد ذلك بسهولة بالغة.
                </p>
              </div>
            </div>
          </div>
        </div>
      </main>
      <header class="vector-parent">
        <img class="rectangle-icon" alt="" src="data:image/png;base64,{data_url5}" alt="cat svg" />
        <img class="claritysettings-solid-icon3" loading="lazy" alt="" src="data:image/png;base64,{data_url6}" alt="cat svg" />
        <img class="tablerbell-icon2" loading="lazy" alt="" src="data:image/png;base64,{data_url7}" alt="cat svg" />
        <img class="notification-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url8}" alt="cat svg" />
        <img class="logo-2-icon3" alt="" src="data:image/png;base64,{data_url9}" alt="cat svg" />
      </header>
    </div>
    """

st.markdown(h, unsafe_allow_html=True)
