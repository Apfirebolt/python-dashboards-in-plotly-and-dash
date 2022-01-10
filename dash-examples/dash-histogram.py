import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/hdfc.csv')

# Histogram would plot the number of times specific range value occurs, for example 160-169 open price occurred 3 times
data = [go.Histogram(
    x=df['Open'][:100],
    name='Open Prices',
), go.Histogram(
    x=df['Close'][:100],
    name='Close Prices'
)]

layout = go.Layout(
    title="Open Price Histogram"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stock-histogram.html')