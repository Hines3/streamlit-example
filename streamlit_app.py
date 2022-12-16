from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

pip install seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import yfinance as yf


start_date = "2015-01-01"
stock_list = ['USO', '^OVX', 'SPY', '^TNX', 'DX-Y.NYB']


def getClose(tickers, start_date):

  df_final = pd.DataFrame()

  for stock in tickers:
    df = yf.download(stock, start=start_date).reset_index()
    df = df.fillna(0)
    close = df['Close']
    
    df_final[stock] = close

  return df_final

def findCorr(table):
  
  corr = table.corr()
  fig, ax = plt.subplots()
  fig.set_size_inches(11,11)

  return sns.heatmap(corr)

test = getClose(stock_list, start_date)
final = findCorr(test)
print(final)
