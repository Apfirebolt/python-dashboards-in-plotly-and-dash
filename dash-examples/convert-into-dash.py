import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/hdfc.csv')

app.layout = html.Div([
    dcc.Graph(id='scatter1',
        figure={
            'data': [
                go.Scatter(
                    x = df['Open'],
                    y = df['Close'],
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'circle',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'HDFC Open vs Close Prices',
                xaxis = {'title': 'Open Prices'},
                yaxis = {'title': 'Close Prices'},
                hovermode='closest'
            )
        }),
        dcc.Graph(id='scatter2',
        figure={
            'data': [
                go.Scatter(
                    x = df['Open'],
                    y = df['High'],
                    mode = 'markers',
                    marker = {
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'circle',
                        'line': {'width': 2}
                        }
                )
            ],
            'layout': go.Layout(
                title = 'HDFC Open vs High Prices',
                xaxis = {'title': 'Open Prices'},
                yaxis = {'title': 'High Prices'},
                hovermode='closest'
            )
        })
])

if __name__ == '__main__':
    app.run_server()
