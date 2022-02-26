import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)

left_columns, right_columns = st.columns(2)
button = left_columns.button('右カラムに文字を表示')
if button:
    right_columns.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#
# st.write('あなたの趣味：', text)
# st.write('コンディション:', condition)

# if st.checkbox('Show Image'):
#    img = Image.open('./img/yuta.jpg')
#    st.image(img, caption='com. Yuta', use_column_width=True)
