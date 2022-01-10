import dash_auth
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

USERNAME_PASSWORD_PAIRS = [
    ['Amit', '007'],['Prafulla', '12345']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width':'50%'})

@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]

if __name__ == '__main__':
    app.run_server()
