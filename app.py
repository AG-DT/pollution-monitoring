
import dash
from dash import html, Dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    
    {        
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",        
    }
]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, external_stylesheets],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
               )
server = app.server

app.title = "Swachh Vayu"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=r"assets/nrsc-logo.jpg", height="60px")),
                        dbc.Col(dbc.NavbarBrand("Swachh Vayu", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://www.nrsc.gov.in/",
                style={"textDecoration": "none"},
                target="_blank",
            ),
            dbc.Nav(
                children=[
                    dbc.NavItem(
                        children=[  
                        dbc.NavLink("Google Earth Engine", 
                                    href="https://earthengine.google.com/", 
                                    external_link=True,
                                    target="_blank",
                                   ),
                        ],
                    ),
                    dbc.NavItem(
                        children=[
                            dbc.NavLink("Sentinel-5P", 
                                        href="https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-5p", 
                                        external_link=True,
                                        target="_blank",
                                       ),
                        ],
                    ),
                ],
                horizontal='end',
            ),
        ],
    ),
    color="primary",
    dark=True,
    className="mb-2"
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
    style={
        'padding': '0px',
        'margin': '0px'
    },
)

if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader=False)
