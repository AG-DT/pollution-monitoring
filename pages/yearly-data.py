
import warnings
warnings.filterwarnings('ignore')

import dash
from dash import dcc, html, callback
import dash_leaflet as dl
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as ps

import pandas as pd
import numpy as np

dash.register_page(
    __name__, 
    path="/yearly-data", 
    name="Year-wise Timeseries", 
    title="Swachh Vayu",
)

cities = ["Agartala", "Ahmadabad", "Bengaluru", "Bhopal", 
          "Delhi", "Hyderabad", "Jaipur", "Kolkata", 
          "Mumbai", "Visakhapatnam"]

parameters = ["AER_AI", "CO", "HCHO", "NO2", "O3", "SO2"]

years = [2019, 2020, 2021]

chart_color = "#4169E1"

lat_long = {
    "Agartala": [23.830238405248906, 91.28244481488565],
    "Ahmadabad": [23.021623553577683, 72.57970682937923],
    "Bengaluru": [12.97911995793008, 77.59129976916228],
    "Bhopal": [23.258486221909365, 77.40198899604252],
    "Delhi": [28.651717881566853, 77.22193892976026],
    "Hyderabad": [17.360589001518093, 78.47406095404506],
    "Jaipur": [26.9154578978753, 75.81898221782217],
    "Kolkata": [22.572671808150375, 88.36388102056003],
    "Mumbai": [19.075990078907964, 72.877392924389],
    "Visakhapatnam": [17.723128139032767, 83.30128405343771],
           }

AER_AI = pd.read_csv("Datasets/AER_AI")
AER_AI["Timestamp"] = pd.to_datetime(AER_AI["Timestamp"], format="%Y-%m-%d")
AER_AI.sort_values("Timestamp", inplace=True)

CO = pd.read_csv("Datasets/CO")
CO["Timestamp"] = pd.to_datetime(CO["Timestamp"], format="%Y-%m-%d")
CO.sort_values("Timestamp", inplace=True)

HCHO = pd.read_csv("Datasets/HCHO")
HCHO["Timestamp"] = pd.to_datetime(HCHO["Timestamp"], format="%Y-%m-%d")
HCHO.sort_values("Timestamp", inplace=True)

NO2 = pd.read_csv("Datasets/NO2")
NO2["Timestamp"] = pd.to_datetime(NO2["Timestamp"], format="%Y-%m-%d")
NO2.sort_values("Timestamp", inplace=True)

O3 = pd.read_csv("Datasets/O3")
O3["Timestamp"] = pd.to_datetime(O3["Timestamp"], format="%Y-%m-%d")
O3.sort_values("Timestamp", inplace=True)

SO2 = pd.read_csv("Datasets/SO2")
SO2["Timestamp"] = pd.to_datetime(SO2["Timestamp"], format="%Y-%m-%d")
SO2.sort_values("Timestamp", inplace=True)

external_stylesheets = [
    
    {        
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",        
    }
]

layout = html.Div(
    children=[        
        html.Div(
            children=[
                html.A(dcc.Link(r"< Back", href="/"), className="back"),
                html.P(children="🛰️", className="header-emoji"),
                html.H1(
                    children="Year-wise Timeseries Visualization", className="header-title"
                ),
                html.P(
                    children="Display the timeseries of various atmospheric "
                             "parameters in the city and year of your choice. "
                             "Choose the city and year from the dropdown menu below.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Choose A City", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": city, "value": city}
                                for city in cities
                            ],
                            placeholder="Select a city",
                            value="Hyderabad",
                            clearable=False,
                            #searchable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Choose An Year", className="menu-title"),
                        dcc.Dropdown(
                            id="date-filter",
                            options=[
                                {"label": year, "value": year}
                                for year in years
                            ],
                            placeholder="Select a year",
                            value=2021,
                            clearable=False,
                            #searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=
                dl.Map(
                    [
                        dl.TileLayer(
                            url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                            maxZoom=25,
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                        ),
                        dl.GestureHandling()
                        #dl.FullscreenControl()
                    ],
                    id="map-box-1",
                    #boxZoom=True,
                    trackResize=True,
                    #zoomControl=False,
                    zoomAnimation=True,
                    zoom=15,
            ),
            className="map-1",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart", 
                        config={"displayModeBar": False},
                        responsive=True,
                    ),
                    className="card-1",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-1", 
                        config={"displayModeBar": False},
                        responsive=True
                    ),
                    className="card-2",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-2", 
                        config={"displayModeBar": False},
                        responsive=True
                    ),
                    className="card-3",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-3", 
                        config={"displayModeBar": False},
                        responsive=True
                    ),
                    className="card-4",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-4", 
                        config={"displayModeBar": False},
                        responsive=True
                    ),
                    className="card-5",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-5", 
                        config={"displayModeBar": False},
                        responsive=True
                    ),
                    className="card-6",
                ),
            ],
            className="wrapper-1",
        ),
    ]
)


@callback(
    [dash.Output("price-chart", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)
def update_charts_AER_AI(cities, year):
    mask = (
        (AER_AI.City == cities)
        & (AER_AI.Year == year)
    )
    filtered_AER_AI = AER_AI.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_AER_AI["Timestamp"],
                "y": filtered_AER_AI["AER_AI"],
                "type": "lines",
                "hovertemplate": "UV Aerosol Index: %{y:.6f}"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "UV Aerosol Index",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "UV Aerosol Index",
                     },
            "colorway": [chart_color],
        },
    }
    return [price_chart_figure]

@callback(
    [dash.Output("price-chart-1", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)
def update_charts_CO(cities, year):
    mask = (
        (CO.City == cities)
        & (CO.Year == year)
    )
    filtered_CO = CO.loc[mask, :]
    price_chart_figure_1 = {
        "data": [
            {
                "x": filtered_CO["Timestamp"],
                "y": filtered_CO["CO"],
                "type": "lines",
                "hovertemplate": "CO Concentration: %{y:.6f} molecules/m<sup>2</sup>"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Concentration of Carbon Monoxide",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "CO Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": [chart_color],
        },
    }
    return [price_chart_figure_1]

@callback(
    [dash.Output("price-chart-2", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)
def update_charts_HCHO(cities, year):
    mask = (
        (HCHO.City == cities)
        & (HCHO.Year == year)
    )
    filtered_HCHO = HCHO.loc[mask, :]
    price_chart_figure_2 = {
        "data": [
            {
                "x": filtered_HCHO["Timestamp"],
                "y": filtered_HCHO["HCHO"],
                "type": "lines",
                "hovertemplate": "HCHO Concentration: %{y:.6f} molecules/m<sup>2</sup>"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Concentration of Formaldehyde",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "HCHO Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": [chart_color],
        },
    }
    return [price_chart_figure_2]

@callback(
    [dash.Output("price-chart-3", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)    
def update_charts_NO2(cities, year):
    mask = (
        (NO2.City == cities)
        & (NO2.Year == year)
    )
    filtered_NO2 = NO2.loc[mask, :]
    price_chart_figure_3 = {
        "data": [
            {
                "x": filtered_NO2["Timestamp"],
                "y": filtered_NO2["NO2"],
                "type": "lines",
                "hovertemplate": "NO2 Concentration: %{y:.6f} molecules/m<sup>2</sup>"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Concentration of Nitrogen Dioxide",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "NO2 Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": [chart_color],
        },
    }
    return [price_chart_figure_3]

@callback(
    [dash.Output("price-chart-4", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)    
def update_charts_O3(cities, year):
    mask = (
        (O3.City == cities)
        & (O3.Year == year)
    )
    filtered_O3 = O3.loc[mask, :]
    price_chart_figure_4 = {
        "data": [
            {
                "x": filtered_O3["Timestamp"],
                "y": filtered_O3["O3"],
                "type": "lines",
                "hovertemplate": "O3 Concentration: %{y:.6f} molecules/m<sup>2</sup>"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Concentration of Ozone",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "O3 Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": [chart_color],
        },
    }
    return [price_chart_figure_4]

@callback(
    [dash.Output("price-chart-5", "figure")],
    [
        dash.Input("region-filter", "value"),
        dash.Input("date-filter", "value"),
    ],
)    
def update_charts_SO2(cities, year):
    mask = (
        (SO2.City == cities)
        & (SO2.Year == year)
    )
    filtered_SO2 = SO2.loc[mask, :]
    price_chart_figure_5 = {
        "data": [
            {
                "x": filtered_SO2["Timestamp"],
                "y": filtered_SO2["SO2"],
                "type": "lines",
                "hovertemplate": "SO2 Concentration: %{y:.6f} molecules/m<sup>2</sup>"
                                 "<br>"
                                 "Date: %{x}"
                                 "<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Concentration of Sulphur Dioxide",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                     },
            "yaxis": {"fixedrange": False,
                      "title": "SO2 concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": [chart_color],
        },
    }
    
    return [price_chart_figure_5]

@callback(
    [dash.Output("map-box-1", "children")],
    [dash.Input("region-filter", "value")],
)
def update_maps(cities):
    
    if cities == "Agartala":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=15,
        )
        return [map_change]

    elif cities == "Ahmadabad":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=12,
        )
        return [map_change]

    elif cities == "Bengaluru":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=12,
        )
        return [map_change]

    elif cities == "Bhopal":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=13,
        )
        return [map_change]

    elif cities == "Delhi":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=13,
        )
        return [map_change]

    elif cities == "Hyderabad":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=12,
        )
        return [map_change]

    elif cities == "Jaipur":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=15,
        )
        return [map_change]

    elif cities == "Mumbai":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=12,
        )
        return [map_change]

    elif cities == "Kolkata":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=15,
        )
        return [map_change]

    elif cities == "Visakhapatnam":
        map_change = dl.Map(
                [
                    dl.TileLayer(
                        url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                        maxZoom=25,
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                    ),
                    dl.GestureHandling()
                    #dl.FullscreenControl()
                ],
                animate=True,
                #id="map-box",
                center=lat_long[cities],
                #boxZoom=True,
                trackResize=True,
                #zoomControl=False,
                zoomAnimation=True,
                zoom=14,
        )
        return [map_change]
    
    else:
        
        return dash.no_update
