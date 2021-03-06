#######
# A very basic Input/Output callback.
######
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize':28, 'color': 'red'}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),
    [Input('number-in', 'value')])
def output(number):
    return number

if __name__ == '__main__':
    app.run_server()
