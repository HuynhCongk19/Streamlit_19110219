import streamlit as st
from PIL import ImageTk, Image

import tensorflow as tf
import numpy as np
from tensorflow import keras

    

st.set_page_config(
    page_title="Học Máy - 19110219",
    page_icon="👋",
)

st.sidebar.title('Trịnh Công Huynh')
st.write("# Trịnh Công Huynh - 19110219")

st.sidebar.success("Chọn phần muốn demo")

st.markdown(
    """
     Bài tập cuối kỳ môn Học Máy gồm:
    
    1. Phát hiện khuôn mặt

    2. Nhận dạng khuôn mặt của chính mình

    3. Nhận dạng 10 chữ số viết tay

    4. Dự báo nhà Cali
    <style>
    body {
        background-image: url('pages/data/images.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
   

)
