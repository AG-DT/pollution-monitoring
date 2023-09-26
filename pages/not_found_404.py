
from dash import html
import dash

dash.register_page(__name__, path="/404")
links = [
    'https://swachh-vayu.ue.r.appspot.com/',
    'https://swachh-vayu.ue.r.appspot.com/yearly-data',
    'https://swachh-vayu.ue.r.appspot.com/multi-year-data/',
    'https://swachh-vayu.ue.r.appspot.com/multi-year-trend-data/'
]


layout = html.Div(
    children=[
        html.H1("Error 404. Not Found!"),
        html.P("Try the following links:"),
        html.Ul(id='my-list', children=[html.Li(i) for i in links])
    ]
)
