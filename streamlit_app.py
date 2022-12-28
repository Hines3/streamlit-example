import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from finta import TA

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ALL BUILT FUNCTIONS FOR CODE

# GET CLOSING CHART OF STOCK
def getClose(tickers, start_date):

  for stock in tickers:
    df = yf.download(stock, start=start_date, interval='1D').reset_index()
    df = df.fillna(0)

  return df

def getRSI(data):
  condition = 0

  df = TA.RSI(data)
  df = df.fillna(0)

  last = df[len(df)-1]
  
  if 50 <= last <= 70:
    condition = 'BUY'
  elif last > 70:
    condition = 'BUY'
  elif 30 <= last < 50:
    condtition = 'SELL'
  elif last < 30:
    condition = 'SELL'

  return condition

def getMACD(data):
  condition = 0
  df = TA.MACD(data)
  df = df.fillna(0)

  MACD = df['MACD'][len(df)-1]
  SIGNAL = df['SIGNAL'][len(df)-1]

  if MACD < 0 or SIGNAL < 0:
    if MACD > SIGNAL:
      condition = 'SELL'
    if MACD <= SIGNAL:
      condition = 'SELL'
  if MACD >= 0 or SIGNAL >= 0:
    if MACD > SIGNAL:
      condition = 'BUY'
    if MACD <= SIGNAL:
      condition = 'BUY'

  return condition
  
def getADX(data):
  condition = 0

  df = TA.ADX(data)
  df = df.fillna(0)

  last = df[len(df)-1]

  if last >= 20:
    condition = 'Strong Direction'
  else:
    condition = 'Directionless'

  return condition

def getROC(data):
  condition = 0

  df = TA.ROC(data)
  df = df.fillna(0)

  last = df[len(df)-1]

  if last >= 0:
    condition = 'BUY'
  else:
    condition = 'SELL'

  return condition

def getBBANDS(data):
  condition = 0

  df = TA.BBANDS(data)
  df = df.fillna(0)

  last = df['BB_MIDDLE'][len(df)-1]
  last_close = data['Close'][len(data)-1]

  if last_close < last:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getMOM(data):
  condition = 0

  df = TA.MOM(data)
  df = df.fillna(0)

  last = df[len(df)-1]
  

  if last < 0:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getSMA(data):
  condition = 0

  df = TA.SMA(data)
  df = df.fillna(0)

  last = df[len(df)-1]
  last_close = data['Close'][len(data)-1]

  if last_close < last:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getAO(data):
  condition = 0

  df = TA.AO(data)
  df = df.fillna(0)

  last = df[len(df)-1]
  

  if last < 0:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getEBBP(data):
  condition = 0

  df = TA.EBBP(data)
  df = df.fillna(0)

  BULL = df['Bull.'][len(df)-1]
  BEAR = df['Bear.'][len(df)-1]

  if BULL + BEAR < 0:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getSAR(data):
  condition = 0

  df = TA.SAR(data)
  df = df.fillna(0)

  last = df[len(df)-1]  
  last_close = data['Close'][len(data)-1]

  if last > last_close:
    condition = 'SELL'
  else:
    condition = 'BUY'

  return condition

def getALL(ticker_list, start_date):
  df = getClose(ticker_list, start_date)

  a = getADX(df)
  b = getAO(df)
  c = getRSI(df)
  d = getMACD(df)
  e = getSAR(df)
  f = getEBBP(df)
  g = getSMA(df)
  h = getMOM(df)
  i = getBBANDS(df)
  j = getROC(df)

  ls = [a,b,c,d,e,f,g,h,i,j]

  return ls



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


















# Project Details
st.title("Stock DashBoard")
st.header("10 Momentum Trend Indicator Anaylsis")

ticker = st.text_input('Stock Ticker')
start_date = st.date_input('Start Date')
df = getALL([ticker], start_date)

st.write(df)

st.line_chart(getClose([ticker], start_date)
