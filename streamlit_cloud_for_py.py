import streamlit as st
import serial
import time

# !!! IMPORTANT: Replace 'COM4' with your actual port name !!!
# !!! Ensure the baud rate matches the Arduino sketch (e.g., 9600) !!!

ser = serial.Serial('/dev/ttyACM0',115200, timeout=1) 
time.sleep(2) # Give the Arduino time to reset after the port is opened



st.title("LED Controller")


effect = st.selectbox('Choose an effect',('Twinkle','Rainbow','Fill','Stormy'))
if (effect == 'Twinkle'):
    ser.write(b'1')
    t_speed = st.slider("Select Twinkle Speed",0,10)
    t_color = st.color_picker("Select Twinkle Color")
if(effect == 'Fill'):
    ser.write(b'2')
    f_color = st.color_picker("Select Fill Color")
if(effect == 'Rainbow'):
    r_speed = st.slider("Select Rainbow Speed",0,10)
if(effect == 'Stormy'):
    s_speed = st.slider("Select Stormy Speed",0,10)
    s_color = st.color_picker("Select Stormy Color")