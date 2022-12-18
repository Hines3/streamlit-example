import streamlit as st
import yfinance as yf

# Get the stock ticker and date range from the user
ticker = st.text_input("Enter a stock ticker (e.g. AAPL):")
date_range = st.date_input("Enter a start date:")
date_range2 = st.date_input("Enter a end date:")

# Use the Yahoo Finance API to retrieve the stock data
data = yf.download(ticker, start=date_range, end=date_range2)

# Plot the stock chart using Streamlit's line_chart function
st.line_chart(data["Close"])
