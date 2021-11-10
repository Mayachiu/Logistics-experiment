import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("流通情報工学実験データ分析アプリ(β)")
st.subheader("by Kazuki Uchiyama")

st.write("時刻変換後のCSVファイル(XXX_t.csv)をアップロード")
uploaded_file = st.file_uploader("ファイルを選んでください。", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding="shift-jis")
    st.dataframe(data)

    #列名取得
    select_list= list(data)

    option1 = st.sidebar.selectbox(
        "x軸に表示するデータを選んでください",
        select_list
    )

    "x軸は",option1,"です"

    option2 = st.sidebar.selectbox(
        "y軸に表示するデータを選んでください",
        select_list
    )

    "y軸は",option2,"です"


    st.write(px.scatter(data,x =option1 ,y = option2))

    st.write(px.line(data,x =option1 ,y = option2))

    st.write(px.histogram(data,x =option1 ,y = option2))

    st.write(px.scatter_3d(data, x="X軸加速度", y="Y軸加速度", z="Z軸加速度"))