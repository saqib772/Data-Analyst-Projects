import numpy as np
import pandas as pd
import plotly.graph_objects as go
data = pd.read_csv("TTM.csv")
print(data.head())


figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Tata Motors Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()

print(data.corr())


# !pip install autots
# You Must install This Library
from autots import AutoTS
model = AutoTS(forecast_length=5, frequency='infer', ensemble='simple')
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
prediction = model.predict()
forecast = prediction.forecast
print(forecast)


