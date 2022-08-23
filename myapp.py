import yfinance as yf
import streamlit as st
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Brands
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

tickerSymbol = st.text_input("Enter  ticker symbol of brands")
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2022-6-22')
st.write("""
# Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
# Volume Price
""")
st.line_chart(tickerDf.Volume)
st.write("""# HighPrice""")
st.line_chart(tickerDf.High)
st.write("""# OpeningPrice """)
st.line_chart(tickerDf.Open)
