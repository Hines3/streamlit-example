import streamlit as st
import yfinance as yf

# Get the stock ticker and date range from the user
ticker = st.text_input("Enter a stock ticker (e.g. AAPL):")
date_range = st.date_range_input("Enter a date range:")

# Use the Yahoo Finance API to retrieve the stock data
data = yf.download(ticker, start=date_range[0], end=date_range[1])

# Plot the stock chart using Streamlit's line_chart function
st.line_chart(data["Close"])
