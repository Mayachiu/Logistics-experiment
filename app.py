import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("流通情報工学実験データ分析アプリ")
st.subheader("by Kazuki Uchiyama")

uploaded_file = st.file_uploader("ファイルを選んでください。", type="csv")

data = pd.read_csv(uploaded_file, encoding="shift-jis")
st.dataframe(data)

#列名取得
select_list= list(data)

option = st.sidebar.selectbox(
    "x軸に表示するデータを選んでください",
    select_list
)

"x軸は",option,"です"

option2 = st.sidebar.selectbox(
    "y軸に表示するデータを選んでください",
    select_list
)

"y軸は",option2,"です"

st.write(px.scatter(data,x =option,y = option2))