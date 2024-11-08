import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
import numpy as np


ticker_symbol = st.text_input("Enter the stock name", "AAPL")
start_date = st.date_input("START DATE", value = datetime.date(2019,1,7))
end_date = st.date_input("END DATE", value = datetime.date(2023,1,7))

data = yf.download(ticker_symbol, start=start_date, end=end_date)

st.write(data)

st.line_chart(data["Volume"])

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.line_chart(chart_data)

