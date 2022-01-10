#######
# Live Update
######
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1(id='live-update-text', style={
            'textAlign': 'center',
            'color': 'gray',
            'font-weight': '700',
        }),
    dcc.Interval(
        id='interval-component',
        interval=1000, # Refreshes every second
        n_intervals=0
    )
])

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_layout(n):
    return 'Refreshed {} times'.format(n)

if __name__ == '__main__':
    app.run_server()
