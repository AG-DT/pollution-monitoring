
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
    path="/multi-year-trend-data", 
    name="Multi-year Trendlines", 
    title="Swachh Vayu",
)

cities = ["Agartala", "Ahmadabad", "Bengaluru", "Bhopal", "Delhi", "Hyderabad", "Jaipur", "Kolkata", 
          "Mumbai", "Visakhapatnam"]

parameters = ["AER_AI", "CO", "HCHO", "NO2", "O3", "SO2"]

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

num_days = 7

AER_AI = pd.read_csv("Datasets/AER_AI")
AER_AI["Timestamp"] = pd.to_datetime(AER_AI["Timestamp"], format="%Y-%m-%d")
AER_AI['rolling_avg'] = AER_AI.AER_AI.rolling(num_days).mean()
AER_AI.sort_values("Timestamp", inplace=True)

CO = pd.read_csv("Datasets/CO")
CO["Timestamp"] = pd.to_datetime(CO["Timestamp"], format="%Y-%m-%d")
CO['rolling_avg'] = CO.CO.rolling(num_days).mean()
CO.sort_values("Timestamp", inplace=True)

HCHO = pd.read_csv("Datasets/HCHO")
HCHO["Timestamp"] = pd.to_datetime(HCHO["Timestamp"], format="%Y-%m-%d")
HCHO['rolling_avg'] = HCHO.HCHO.rolling(num_days).mean()
HCHO.sort_values("Timestamp", inplace=True)

NO2 = pd.read_csv("Datasets/NO2")
NO2["Timestamp"] = pd.to_datetime(NO2["Timestamp"], format="%Y-%m-%d")
NO2['rolling_avg'] = NO2.NO2.rolling(num_days).mean()
NO2.sort_values("Timestamp", inplace=True)

O3 = pd.read_csv("Datasets/O3")
O3["Timestamp"] = pd.to_datetime(O3["Timestamp"], format="%Y-%m-%d")
O3['rolling_avg'] = O3.O3.rolling(num_days).mean()
O3.sort_values("Timestamp", inplace=True)

SO2 = pd.read_csv("Datasets/SO2")
SO2["Timestamp"] = pd.to_datetime(SO2["Timestamp"], format="%Y-%m-%d")
SO2['rolling_avg'] = SO2.SO2.rolling(num_days).mean()
SO2.sort_values("Timestamp", inplace=True)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.A(dcc.Link(r"< Back", href="/"), className="back"),
                html.P(children="🛰️", className="header-emoji"),
                html.H1(
                    children="Multi-year Trendlines Visualization", className="header-title"
                ),
                html.P(
                    children="Select a city from the dropdown "
                             "menu to compare atmospheric "
                             "data from 2019-2021 as a 7-day rolling average. "
                             "Click a trace from the legend "
                             "to hide the data from that year.",
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
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=
                        dl.Map(
                            [
                                dl.TileLayer(
                                    url='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
                                    maxZoom=25,
                                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
                                ),
                                dl.GestureHandling(),
                            ],
                            id="map-box-3",
                            #boxZoom=True,
                            trackResize=True,
                            #zoomControl=False,
                            zoomAnimation=True,
                            zoom=15,
                    ),
                    className="map-2",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-13", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-7",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-14", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-8",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-15", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-9",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-16", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-10",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-17", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-11",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="price-chart-18", 
                        config={
                            "showTips": True,
                            "displayModeBar": False,
                        },
                        responsive=True,
                    ),
                    className="card-12",
                ),
            ],
            className="wrapper-2",
        ),
    ]
)


@callback(
    [dash.Output("price-chart-13", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)
def update_charts_AER_AI(cities):
    AER_AI_2019_mask = (
        (AER_AI.City == cities)
        & (AER_AI.Year == 2019)
    )
    filtered_AER_AI_2019 = AER_AI.loc[AER_AI_2019_mask, :]
    
    AER_AI_2020_mask = (
        (AER_AI.City == cities)
        & (AER_AI.Year == 2020)
    )
    filtered_AER_AI_2020 = AER_AI.loc[AER_AI_2020_mask, :]
    
    AER_AI_2021_mask = (
        (AER_AI.City == cities)
        & (AER_AI.Year == 2021)
    )
    filtered_AER_AI_2021 = AER_AI.loc[AER_AI_2021_mask, :]
    
    price_chart_figure = {
        "data": [
            {
                "x": filtered_AER_AI_2019["DOY"],
                "y": filtered_AER_AI_2019["rolling_avg"],
                "customdata": filtered_AER_AI_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_AER_AI_2020["DOY"],
                "y": filtered_AER_AI_2020["rolling_avg"],
                "customdata": filtered_AER_AI_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_AER_AI_2021["DOY"],
                "y": filtered_AER_AI_2021["rolling_avg"],
                "customdata": filtered_AER_AI_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
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
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "UV Aerosol Index",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure]

@callback(
    [dash.Output("price-chart-14", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)
def update_charts_CO(cities):
    CO_2019_mask = (
        (CO.City == cities)
        & (CO.Year == 2019)
    )
    filtered_CO_2019 = CO.loc[CO_2019_mask, :]
    
    CO_2020_mask = (
        (CO.City == cities)
        & (CO.Year == 2020)
    )
    filtered_CO_2020 = CO.loc[CO_2020_mask, :]
    
    CO_2021_mask = (
        (CO.City == cities)
        & (CO.Year == 2021)
    )
    filtered_CO_2021 = CO.loc[CO_2021_mask, :]
    
    price_chart_figure_1 = {
        "data": [
            {
                "x": filtered_CO_2019["DOY"],
                "y": filtered_CO_2019["rolling_avg"],
                "customdata": filtered_CO_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_CO_2020["DOY"],
                "y": filtered_CO_2020["rolling_avg"],
                "customdata": filtered_CO_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_CO_2021["DOY"],
                "y": filtered_CO_2021["rolling_avg"],
                "customdata": filtered_CO_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
            },
        ],
        "layout": {
            "autosize": True,
            "title": {
                "text": "Carbon Monoxide Concentration",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "CO Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure_1]

@callback(
    [dash.Output("price-chart-15", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)
def update_charts_HCHO(cities):
    HCHO_2019_mask = (
        (HCHO.City == cities)
        & (HCHO.Year == 2019)
    )
    filtered_HCHO_2019 = HCHO.loc[HCHO_2019_mask, :]
    customdata_HCHO_2019  = np.stack((filtered_HCHO_2019['Timestamp']), axis=-1)
    
    HCHO_2020_mask = (
        (HCHO.City == cities)
        & (HCHO.Year == 2020)
    )
    filtered_HCHO_2020 = HCHO.loc[HCHO_2020_mask, :]
    
    HCHO_2021_mask = (
        (HCHO.City == cities)
        & (HCHO.Year == 2021)
    )
    filtered_HCHO_2021 = HCHO.loc[HCHO_2021_mask, :]
    
    price_chart_figure_2 = {
        "data": [
            {
                "x": filtered_HCHO_2019["DOY"],
                "y": filtered_HCHO_2019["rolling_avg"],
                "customdata": filtered_HCHO_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_HCHO_2020["DOY"],
                "y": filtered_HCHO_2020["rolling_avg"],
                "customdata": filtered_HCHO_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_HCHO_2021["DOY"],
                "y": filtered_HCHO_2021["rolling_avg"],
                "customdata": filtered_HCHO_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
            },
        ],
        "layout": {
            "title": {
                "text": "Formaldehyde Concentration",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "HCHO Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure_2]

@callback(
    [dash.Output("price-chart-16", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)    
def update_charts_NO2(cities):
    NO2_2019_mask = (
        (NO2.City == cities)
        & (NO2.Year == 2019)
    )
    filtered_NO2_2019 = NO2.loc[NO2_2019_mask, :]
    
    NO2_2020_mask = (
        (NO2.City == cities)
        & (NO2.Year == 2020)
    )
    filtered_NO2_2020 = NO2.loc[NO2_2020_mask, :]
    
    NO2_2021_mask = (
        (NO2.City == cities)
        & (NO2.Year == 2021)
    )
    filtered_NO2_2021 = NO2.loc[NO2_2021_mask, :]
    
    price_chart_figure_3= {
        "data": [
            {
                "x": filtered_NO2_2019["DOY"],
                "y": filtered_NO2_2019["rolling_avg"],
                "customdata": filtered_NO2_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_NO2_2020["DOY"],
                "y": filtered_NO2_2020["rolling_avg"],
                "customdata": filtered_NO2_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_NO2_2021["DOY"],
                "y": filtered_NO2_2021["rolling_avg"],
                "customdata": filtered_NO2_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
            },
        ],
        "layout": {
            "title": {
                "text": "Nitrogen Dioxide Concentration",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "NO2 Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure_3]

@callback(
    [dash.Output("price-chart-17", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)    
def update_charts_O3(cities):
    O3_2019_mask = (
        (O3.City == cities)
        & (O3.Year == 2019)
    )
    filtered_O3_2019 = O3.loc[O3_2019_mask, :]
    
    O3_2020_mask = (
        (O3.City == cities)
        & (O3.Year == 2020)
    )
    filtered_O3_2020 = O3.loc[O3_2020_mask, :]
    
    O3_2021_mask = (
        (O3.City == cities)
        & (O3.Year == 2021)
    )
    filtered_O3_2021 = O3.loc[O3_2021_mask, :]
    
    price_chart_figure_4 = {
        "data": [
            {
                "x": filtered_O3_2019["DOY"],
                "y": filtered_O3_2019["rolling_avg"],
                "customdata": filtered_O3_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_O3_2020["DOY"],
                "y": filtered_O3_2020["rolling_avg"],
                "customdata": filtered_O3_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_O3_2021["DOY"],
                "y": filtered_O3_2021["rolling_avg"],
                "customdata": filtered_O3_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
            },
        ],
        "layout": {
            "title": {
                "text": "Ozone Concentration",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "O3 Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure_4]

@callback(
    [dash.Output("price-chart-18", "figure")],
    [
        dash.Input("region-filter", "value"),
    ],
)    
def update_charts_SO2(cities):
    SO2_2019_mask = (
        (SO2.City == cities)
        & (SO2.Year == 2019)
    )
    filtered_SO2_2019 = SO2.loc[SO2_2019_mask, :]
    
    SO2_2020_mask = (
        (SO2.City == cities)
        & (SO2.Year == 2020)
    )
    filtered_SO2_2020 = SO2.loc[SO2_2020_mask, :]
    
    SO2_2021_mask = (
        (SO2.City == cities)
        & (SO2.Year == 2021)
    )
    filtered_SO2_2021 = SO2.loc[SO2_2021_mask, :]
    
    price_chart_figure_5 = {
        "data": [
            {
                "x": filtered_SO2_2019["DOY"],
                "y": filtered_SO2_2019["rolling_avg"],
                "customdata": filtered_SO2_2019.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2019",
            },
            
            {
                "x": filtered_SO2_2020["DOY"],
                "y": filtered_SO2_2020["rolling_avg"],
                "customdata": filtered_SO2_2020.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2020",
            },
            
            {
                "x": filtered_SO2_2021["DOY"],
                "y": filtered_SO2_2021["rolling_avg"],
                "customdata": filtered_SO2_2021.Timestamp,
                "type": "lines",
                "hovertemplate": "Date: %{customdata|%d %B %Y}"
                                 "<extra></extra>",
                "name": "2021",
            },
        ],
        "layout": {
            "title": {
                "text": "Sulphur Dioxide Concentration",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": False, 
                      "title": "Date Range",
                      "tickmode": 'array',
                      "tickvals": np.linspace(15,380,13)[:-1],
                      "ticktext": ['Jan', 'Feb', 'Mar', 'Apr', 
                                   'May', 'Jun', 'Jul', 'Aug', 
                                   'Sep', 'Oct', 'Nov', 'Dec'],
                     },
            "yaxis": {"fixedrange": False,
                      "title": "SO2 Concentration (molecules/m<sup>2</sup>)",
                     },
            "colorway": ["#17B897", "#FA1F1F", "#1F36FA"],
        },
    }
    return [price_chart_figure_5]

@callback(
    [dash.Output("map-box-3", "children")],
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
                id="map-box-3",
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
