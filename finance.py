import yfinance as yf 
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google !
         """)

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-01-01', end='2023-01-01')


st.header("Closing Price")
st.line_chart(tickerDf.Close)
st.header("Volume")
st.line_chart(tickerDf.Volume)

