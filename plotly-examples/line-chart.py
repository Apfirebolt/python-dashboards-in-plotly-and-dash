#######
# Contain Line Charts examples in Plotly
######

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import time

df = pd.read_csv('../data/hdfc.csv')

def line_chart():
    # Read only 10 values from stock data csv file
    x_values = df['Open'][:10]
    y_values = df['Volume'][:10]

    # create traces
    trace0 = go.Scatter(
        x = x_values + 25,
        y = y_values+5,
        mode = 'markers',
        name = 'markers'
    )
    trace1 = go.Scatter(
        x = x_values,
        y = y_values,
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    trace2 = go.Scatter(
        x = x_values - 25,
        y = y_values,
        mode = 'lines',
        name = 'lines'
    )
    data = [trace0, trace1, trace2]  # assign traces to data
    layout = go.Layout(
        title = 'Line chart for Volume vs Open Price'
    )
    fig = go.Figure(data=data,layout=layout)
    pyo.plot(fig, filename='line-chart.html')


# Calculate time taken to plot the graph
start_time = time.time()
line_chart()
print("--- '%.3f' seconds ---" % (time.time() - start_time))
