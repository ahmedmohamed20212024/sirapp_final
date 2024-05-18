import base64
import os

import requests
import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="cv_details", page_icon=":tada:", layout="wide")

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
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Athiti:wght@700&display=swap" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;1,400&display=swap"/>
  </head>
"""
            , unsafe_allow_html=True)

path = os.path.dirname(__file__)
my_file = path + '/global2.css'

local_css(my_file)

path = os.path.dirname(__file__)
my_file = path + '/cv_details/cv_details.css'

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
my_file = path + '/public/template-4@2x.png'

file_3 = open(my_file, "rb")
contents3 = file_3.read()
data_url3 = base64.b64encode(contents3).decode("utf-8")
file_3.close()

h = f"""
<div class="website-structure">
      <main class="home-page">
        <header class="navigation-menu">
          <div class="mingcutedownload-line"></div>
          <a href="cv_home" target="_self" >
          <img class="mdiarrow-left-bold-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url}"/></a>
          <div class="sidebar">
            <h1 class="h1">السيرة الذاتية</h1>
          </div>
          <div class="main-content">
            <img class="group-icon" loading="lazy"
              alt="" src="data:image/png;base64,{data_url2}" />
          </div>
        </header>
        <div class="home-page-child"></div>
        <section class="home-page-inner">
          <div class="line-parent">
            <img class="frame-child" loading="lazy" alt="" />
            <div class="job-details">
              <div class="job-card">
                <div class="job-summary">
                  <b class="b">الخبرة العملية</b>
                  <div class="job-information">
                    <div class="job-information-child"></div>
                    <div class="job-position-details">
                      <div class="position-title">
                        <div class="div">المركز الوظيفي</div>
                      </div>
                      <div class="position-name">
                        <div class="position-name-child"></div>
                        <input class="ux-design-intern" placeholder="UX Design Intern" type="text" />
                      </div>
                    </div>
                    <div class="company-location-details">
                      <div class="location-information">
                        <div class="city-information">
                          <div class="city-label">
                            <div class="div1">جهة صاحب العمل</div>
                            <div class="dates-information">
                              <div class="div2">المدينة</div>
                            </div>
                          </div>
                        </div>
                        <div class="month-label-parent">
                          <div class="month-label">
                            <div class="month-label-child"></div>
                            <input class="abc-company" placeholder="ABC Company" type="text" />
                          </div>
                          <div class="month-label1">
                            <div class="month-label-item"></div>
                            <input class="los-angeles" placeholder="Los Angeles" type="text"/>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="end-date-details">
                      <div class="end-duration">
                        <div class="end-month-info">
                          <div class="div3">تاريخ البدء</div>
                        </div>
                        <div class="empty">
                          <div class="rectangle-parent">
                            <div class="frame-item"></div>
                            <i class="jan">JAN</i>
                          </div>
                          <div class="rectangle-group">
                            <div class="frame-inner"></div>
                            <i class="i">2018</i>
                          </div>
                        </div>
                        <div class="skills-information">
                          <div class="skills-details">
                            <div class="div4">تاريخ الانتهاء</div>
                          </div>
                          <div class="skill-summary">
                            <div class="experience-overview">
                              <div class="design-skills">
                                <div class="design-skills-child"></div>
                                <i class="jan1">JAN</i>
                              </div>
                            </div>
                            <div class="rectangle-container">
                              <div class="rectangle-div"></div>
                              <i class="i1">2023</i>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="job-information-inner">
                      <div class="frame-parent">
                        <div class="wrapper">
                          <div class="div5">الوصف</div>
                        </div>
                        <div class="description-summary">
                          <div class="description-summary-child"></div>
                          <i class="skilled-ux-designer">Skilled UX Designer specializing in user-centered
                          designs. Strong foundation in visual design,
                          prototyping and user research methods. Committed to
                          delivering exceptional user experiences</i>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <img class="template-4-icon" loading="lazy" alt="" src="data:image/png;base64,{data_url3}"/>
            </div>
          </div>
        </section>
      </main>
    </div>
"""

st.markdown(h, unsafe_allow_html=True)
