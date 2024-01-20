import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.linear_model import LogisticRegression
import time

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
x = data['x']

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل تشخیص سلامت جنین</h1>", unsafe_allow_html=True)
    st.write("<h3 style='text-align: center; color: gray;'>برای نتیجه دقیق مشخصات توسط پزشک متخصص وارد شده و ارزیابی گردد</h3>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

    st.write("<h5 style='text-align: center; color: gray;'>Fetal Accelerations / 15 s</h5>", unsafe_allow_html=True)
    accelerations = st.slider('میزان افزایش ضربان قلب جنین در هر 15 ثانیه', 0.00, 0.05, 0.01)

    st.write("<h5 style='text-align: center; color: gray;'>Fetal Movement</h5>", unsafe_allow_html=True)
    fetal_movement = st.slider('میزان رشد جنین که توسط مادر حس می گردد', 0.00, 0.50000, 0.01)

    st.write("<h5 style='text-align: center; color: gray;'>Fetal Prolonged Peceleration</h5>", unsafe_allow_html=True)
    prolongued_decelerations = st.slider('ضربان قلب غیرطبیعی جنین از هر 2 تا 10 دقیقه', 0.000, 0.05, 0.01)

    st.write("<h5 style='text-align: center; color: gray;'>Fetal Abnormal STV</h5>", unsafe_allow_html=True)
    abnormal_short_term_variability = st.slider('تغییر پذیری کوتاه مدت و غیرطبیعی ساقه مغز', 12.00, 90.00, 15.00)

    st.write("<h5 style='text-align: center; color: gray;'>Fetal Abnormal STV Time Percentage</h5>", unsafe_allow_html=True)
    percentage_of_time_with_abnormal_long_term_variability = st.slider('درصد زمانی تغییر پذیری کوتاه مدت ضربان قلب جنین با فرکانس 3 تا 10 سیکل/دقیقه', 0.00, 91.00, 1.00)

    st.write("<h5 style='text-align: center; color: gray;'>Fetal LTV Mean Value</h5>", unsafe_allow_html=True)
    mean_value_of_long_term_variability = st.slider('میانگین تنوع بلند مدت', 0.00, 51.00, 5.00)

    button = st.button('معاینه و تشخیص')
    if button:
        x = np.array([[accelerations, fetal_movement, prolongued_decelerations,
                       abnormal_short_term_variability, percentage_of_time_with_abnormal_long_term_variability,
                       mean_value_of_long_term_variability]])

        y_prediction = model.predict(x)
        if y_prediction == 1.0:
            with st.chat_message("assistant"):
                with st.spinner('''درحال بررسی، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''بررسی انجام شد')
                    st.write("<h4 style='text-align: right; color: gray;'>بر اساس داده های وارد شده، جنین سالم است</h4>", unsafe_allow_html=True)
        
        else:
            with st.chat_message("assistant"):
                with st.spinner('''درحال بررسی، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''بررسی انجام شد')
                    st.write("<h4 style='text-align: right; color: gray;'>بر اساس داده های وارد شده، جنین مشکوک به ناهنجاری است</h4>", unsafe_allow_html=True)
                    st.write("<h5 style='text-align: right; color: gray;'>برای بررسی دقیق تر به پزشک متخصص مراجعه کنید</h5>", unsafe_allow_html=True)
show_page()
