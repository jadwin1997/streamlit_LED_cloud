import streamlit as st
import serial
import time


# # ---------- SERIAL CONNECTION (cached so it opens once) ----------
# @st.cache_resource
# def get_serial_port():
#     # Update device path and baud rate to match your Arduino
#     ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
#     time.sleep(2)  # allow Arduino reset time
#     return ser




st.title("LED Controller")


effect = st.selectbox('Choose an effect',('Twinkle','Rainbow','Fill','Stormy'))
if (effect == 'Twinkle'):
    t_speed = st.slider("Select Twinkle Speed",0,10)
    t_color = st.color_picker("Select Twinkle Color")
if(effect == 'Fill'):
    f_color = st.color_picker("Select Fill Color")
if(effect == 'Rainbow'):
    r_speed = st.slider("Select Rainbow Speed",0,10)
if(effect == 'Stormy'):
    s_speed = st.slider("Select Stormy Speed",0,10)
    s_color = st.color_picker("Select Stormy Color")