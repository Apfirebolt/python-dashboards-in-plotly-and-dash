#######
# This plots 20 random data points between 1 and 100 in both
# vertical and horizontal directions.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import time

def plot_graph():
    np.random.seed(42)
    # random_x = np.random.randint(1,81,80)
    # random_y = np.random.randint(1,81,80)

    random_x = [1, 5, 8, 2, 9]
    random_y = [2, 6, 19, 21, 8]

    data = [go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers',
    )]
    
    pyo.plot(data, filename='scatter-graph.html')

def plot_with_layout():
    random_x = [1, 5, 8, 2, 9]
    random_y = [2, 6, 19, 21, 8]

    data = [go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers',
        marker = dict(      # change the marker style
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    ))]

    layout = go.Layout(
    title = 'Scatterplot Chart', # Graph title
    xaxis = dict(title = 'Some x-values'), # x-axis label
    yaxis = dict(title = 'Some y-values'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
    )

    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='scatter-graph.html')


# Calculate time taken to plot the graph
start_time = time.time()
plot_with_layout()
print("--- '%.3f' seconds ---" % (time.time() - start_time))
