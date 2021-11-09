import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("流通情報工学実験データ分析アプリ")
st.subheader("by Kazuki Uchiyama")

uploaded_file = st.file_uploader("ファイルを選んでください。", type="csv")

data = pd.read_csv(uploaded_file, encoding="shift-jis")
st.dataframe(data)
