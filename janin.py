import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import time

st.set_page_config(page_title='تشخیص ناهنجاری جنین - RoboAi', layout='centered', page_icon='👶🏻')

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['model']
x = data['x']

def show_page():
    st.write("<h3 style='text-align: center; color: blue;'>تشخیص ناهنجاری جنین 🧬</h3>", unsafe_allow_html=True)
    st.write("<h6 style='text-align: center; color: black;'>Robo-Ai.ir طراحی شده و توسعه</h6>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")
    container = st.container(border=True)
    container.write("<h6 style='text-align: right; color: gray;'>تشخیص ناهنجاری جنین با هوش مصنوعی 🔬</h6>", unsafe_allow_html=True)
    st.write('')

    with st.sidebar:
        st.write("<h5 style='text-align: center; color: blcak;'>تشخیص ناهنجاری جنین با یادگیری ماشین</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: gray;'>ساخته شده برای تشخیص ناهنجاری جنین بر اساس آزمایش</h5>", unsafe_allow_html=True)
        st.divider()
        st.write("<h5 style='text-align: center; color: black;'>طراحی و توسعه</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center; color: gray;'>حمیدرضا بهرامی</h5>", unsafe_allow_html=True)

    accelerations = st.slider('میزان افزایش ضربان قلب جنین در هر 15 ثانیه', 0.00, 0.05, 0.01)
    st.divider()

    fetal_movement = st.slider('میزان رشد جنین که توسط مادر حس می گردد', 0.00, 0.50000, 0.01)
    st.divider()

    prolongued_decelerations = st.slider('ضربان قلب غیرطبیعی جنین از هر 2 تا 10 دقیقه', 0.000, 0.05, 0.01)
    st.divider()

    abnormal_short_term_variability = st.slider('تغییر پذیری کوتاه مدت و غیرطبیعی ساقه مغز', 12.00, 90.00, 15.00)
    st.divider()

    percentage_of_time_with_abnormal_long_term_variability = st.slider('درصد زمانی تغییر پذیری کوتاه مدت ضربان قلب جنین با فرکانس 3 تا 10 سیکل/دقیقه', 0.00, 91.00, 1.00)
    st.divider()

    mean_value_of_long_term_variability = st.slider('میانگین تنوع بلند مدت', 0.00, 51.00, 5.00)
    st.divider()

    button = st.button('ارزیابی')
    if button:
        with st.chat_message("assistant"):
                with st.spinner('''درحال ارزیابی ، لطفا صبور باشید'''):
                    time.sleep(2)
                    st.success(u'\u2713''ارزیابی انجام شد')
                    x = np.array([[accelerations, fetal_movement, prolongued_decelerations, abnormal_short_term_variability,
                                    percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability]])

        y_prediction = model.predict(x)
        if y_prediction == 1.0:
            text1 = 'بر اساس ارزیابی من ، جنین سالم است'
            text2 = 'Based on my analysis, Fetus is healthy'
            def stream_data1():
                for word in text1.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data1)
            def stream_data2():
                for word in text2.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data2)
            
        else:
            text5 = 'بر اساس ارزیابی من ، احتمال وجود ناهنجاری در جنین بالا است'
            text6 = 'برای ارزیابی بهتر به پزشک متخصص مراجعه کنید'
            text7 = 'Based on my analysis, the possibility of Fetus being unhealthy is high'
            text8 = "For more certainty, visit a specialist doctor"
            def stream_data5():
                for word in text5.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data5)
            def stream_data6():
                for word in text6.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data6)
            def stream_data7():
                for word in text7.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data7)
            def stream_data8():
                for word in text8.split(" "):
                    yield word + " "
                    time.sleep(0.09)
            st.write_stream(stream_data8)
show_page()
