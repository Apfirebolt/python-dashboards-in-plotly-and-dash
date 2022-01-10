import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.ConfirmDialog(
        id='confirm-danger',
        message='Danger danger! Are you sure you want to continue?',
    ),

    dcc.Dropdown(
        options=[
            {'label': i, 'value': i}
            for i in ['Safe', 'Danger!!']
        ],
        id='dropdown-danger'
    ),
    html.Div(id='output-danger')
])


@app.callback(Output('confirm-danger', 'displayed'),
              Input('dropdown-danger', 'value'))
def display_confirm(value):
    if value == 'Danger!!':
        return True
    return False


@app.callback(Output('output-danger', 'children'),
              Input('confirm-danger', 'submit_n_clicks'))
def update_output(submit_n_clicks):
    if submit_n_clicks:
        return 'It wasnt easy but we did it {}'.format(submit_n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)