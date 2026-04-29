import streamlit as st
import pandas as pd
from src.ranking import rank

st.set_page_config(layout="wide")
st.title("Breakout Trading Dashboard")

try:
    df = pd.read_csv("data/signals.csv")
except:
    st.warning("No data yet. Wait for first run.")
    st.stop()

df = rank(df)

st.metric("High Conviction Trades", len(df[df["Signal"]=="HIGH CONVICTION"]))

st.subheader("Top Ranked Stocks")
st.dataframe(df.head(10))

st.subheader("All Stocks")
st.dataframe(df)
