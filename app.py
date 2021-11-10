import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("流通情報工学実験データ分析アプリ(β)")
st.subheader("by Kazuki Uchiyama")

uploaded_file = st.file_uploader("時刻変換後のCSVファイル(XXX_t.csv)をアップロード", type="csv")

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

    option3 = st.sidebar.selectbox(
            "グラフの種類を選んでください",
            ["散布図", "折れ線", "ヒストグラム"]
        )

    if option3 == "散布図":
        st.write(px.scatter(data,x =option1 ,y = option2))
    if option3 == "折れ線":
        st.write(px.line(data,x =option1 ,y = option2))
    if option3 == "ヒストグラム":
        st.write(px.histogram(data,x =option1 ,y = option2))

    