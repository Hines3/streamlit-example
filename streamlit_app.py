
import streamlit as st
import yfinance as yf
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from statsmodels.tsa.forecasting.stl import STLForecast

# Define a function to retrieve stock price data using yfinance
def get_stock_data(ticker, start_date):
    data = yf.download(ticker, start_date)
    return data['Close']

# Define the main function of your Streamlit app
def main():
    # Add a title to your app
    st.title("Stock Price Forecasting App")
    
    # Add a sidebar with input fields for the ticker and start date
    st.sidebar.title("Input Parameters")
    ticker = st.sidebar.text_input("Ticker", "XME")
    start_date = st.sidebar.date_input("Start Date")
    
    # Retrieve the stock price data
    df = get_stock_data(ticker, start_date)
    
    # Perform seasonal-trend decomposition of the time series data using STL
    stl = STL(df, period=13)
    res = stl.fit()
    
    # Plot the STL decomposition
    st.write("Seasonal-Trend Decomposition")
    fig = res.plot()
    st.pyplot(fig)
    
    # Perform time series forecasting using ARIMA and STL
    st.write("Time Series Forecasting")
    st.write("ARIMA Model Parameters: order=(1, 1, 0), trend='t', period=12")
    stlf = STLForecast(df, ARIMA, period=12, model_kwargs=dict(order=(1, 1, 0), trend="t"))
    stlf_res = stlf.fit()
    forecast = stlf_res.forecast(24)
    fig, ax = plt.subplots()
    ax.plot(df, label='Actual')
    ax.plot(forecast, label='Forecast')
    ax.legend()
    st.pyplot(fig)
    
    # Display the summary statistics of the forecasting model
    st.write("Summary Statistics of the Forecasting Model")
    st.write(stlf_res.summary())

# Call the main function of your Streamlit app
if __name__ == "__main__":
    main()
