#######
# Bar Chart in Plotly for Close Price vs Volume of HDFC Stock
######

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import time

def plot_single_bar_chart():
    df = pd.read_csv('../data/hdfc.csv')

    data = [go.Bar(
        x=df['Close'][:10], 
        y=df['Volume'][:10],
        name = 'Gold',
        marker=dict(color='#FFD700') # set the marker color to gold
    )]
    layout = go.Layout(
        title='Close price vs Volume for HDFC'
    )
    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='bar-chart.html')

# Calculate time taken to plot the graph
start_time = time.time()
plot_single_bar_chart()
print("--- '%.3f' seconds ---" % (time.time() - start_time))
