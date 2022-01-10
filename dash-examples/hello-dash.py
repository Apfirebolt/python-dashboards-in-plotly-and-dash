# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
import pandas as pd

app = dash.Dash()

colors = {
    'background': '#f5deda',
    'text': '#302b2a'
}

def plot_example_graph():
    app.layout = html.Div(
        children=[
    html.H1(
        children='HDFC Stock Graph',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-weight': '700',
        }
    ),
    html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [4, 7, 5, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 3, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Dash Data Visualization'
            }
        }
    )],
    style={'backgroundColor': colors['background'], 'padding': '1rem'}    
    )


def plot_stock_graph():
    df_hdfc = pd.read_csv('../data/hdfc.csv')
    df_adani = pd.read_csv('../data/adaniports.csv')

    app.layout = html.Div(
        children=[
    html.H1(
        children='HDFC Stock Graph',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-weight': '700',
        }
    ),
    html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df_hdfc['Open'], 'y': df_hdfc['Close'], 'type': 'bar', 'name': 'HDFC Data'},
                {'x': df_adani['Open'], 'y': df_adani['Close'], 'type': 'bar', 'name': 'Adani Data', 'marker' : { "color" : 'red'}},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Stock Data Visualization in Dash'
            }
        },
        animate=True,
    )],
    style={'backgroundColor': colors['background'], 'padding': '1rem'}    
    )


# plot_example_graph()
plot_stock_graph()

if __name__ == '__main__':
    app.run_server()
