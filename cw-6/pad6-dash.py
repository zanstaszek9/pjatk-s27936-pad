from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df2 = pd.read_csv("https://raw.githubusercontent.com/zanstaszek9/pjatk-s27936-pad/master/cw-6/data/winequelity.csv")

df2_proper_columns = df2.loc[:, df2.columns.difference(['Unnamed: 0'])].columns.values;

app.layout = html.Div([
    html.Div([


        html.Div([
            html.Div(
                dash_table.DataTable(df2.head(10).to_dict('records'))
            ), 

            html.Br(), 
            dcc.RadioItems(
                ['Regresja', 'Klasyfikacja'],
                'Regresja',
                id='crossfilter-xaxis-type',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            ),
            dcc.Dropdown(
                df2_proper_columns,
                df2_proper_columns[0],
                id='crossfilter-xaxis-column',
            )
            
        ],
        style={'width': '30%', 'display': 'inline-block'})

    
    ], style={
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'width': '80%', 'display': 'inline-block', 'padding': '0 20'}),

])


@app.callback(
    Output('crossfilter-indicator-scatter', 'figure'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'))
def update_graph(xaxis_column_name, chart_type):
    if chart_type == 'Regresja' :
        fig = px.scatter(df2, x=xaxis_column_name, y='pH', trendline="ols", trendline_color_override="red")

    else: 
        fig = px.pie(df2, values=xaxis_column_name, names='target')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
