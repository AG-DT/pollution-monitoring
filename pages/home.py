
import dash
from dash import dcc, html
dash.register_page(
    __name__, 
    path="/", 
    name="Home", 
    title="Swachh Vayu",
)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children="Swachh Vayu", className="home-header"),
                html.P(children='''
                An Interactive Dashboard to Monitor the Atmospheric Pollutants in the Environment
                ''', className="home-header-brief"),
            ],
            className = "home-header-container",
        ),
        html.Div(
            children=[
                html.H2(children="About", className="intro-1"),
                html.P(
                    children='''
                    An interactive dashboard that allows users to visualize the Air Quality
                    of a region by monitoring the atmospheric pollutants in the air. The
                    data in question is extracted from the Sentinel 5 Precursor mission's 
                    Tropospheric Monitoring Instrument (TROPOMI) that is available on 
                    Google Earth Engine which allows the user to comprehend the environment 
                    using Time Series and Trendlines to either understand the yearly trend 
                    or to compare multi-year data which with help in gauging the current 
                    situation and give an idea about future trends. 
                ''', className="intro-description"),
                html.H2(
                    children="Sentinel-5 Precursor Mission", className="intro-2"
                ),
                html.P(
                    children='''
                    The Copernicus Sentinel-5 Precursor mission is the first Copernicus 
                    mission dedicated to monitoring our atmosphere. The main objective of the 
                    Copernicus Sentinel-5P mission is to perform atmospheric measurements with 
                    high spatio-temporal resolution, to be used for air quality, ozone & UV radiation, 
                    and climate monitoring & forecasting. The satellite was successfully launched on 
                    13 October 2017 from the Plesetsk cosmodrome in Russia.
                    ''', className="intro-2-description-1"
                ),
                html.Img(src=r'assets/copernicus-s5p.PNG', className="img-1"),
                html.P(
                    children=''' 
                    The Sentinel-5 Precursor mission instrument collects data useful for assessing air 
                    quality. The TROPOMI instrument is a multispectral sensor that records reflectance of 
                    wavelengths important for measuring atmospheric concentrations of ozone, methane, 
                    formaldehyde, aerosol, carbon monoxide, nitrogen oxide, and sulphur dioxide, as well as 
                    cloud characteristics at a spatial resolution of 0.01 arc degrees.
                    The TROPOMI instrument combines the strengths of SCIAMACHY, OMI and state-of-the-art 
                    technology to provide observations with performances that cannot be met by the current 
                    instruments in space. Performance of current in-orbit instruments are surpassed in terms 
                    of sensitivity, spectral resolution, spatial resolution and temporal resolution.
                    ''', className="intro-2-description-2"
                ),
                html.H2(
                    children="Google Earth Engine", className="intro-3"
                ),
                html.P(
                    children='''
                    Google Earth Engine combines a multi-petabyte catalog of satellite imagery and geospatial 
                    datasets with planetary-scale analysis capabilities. Scientists, researchers, and 
                    developers use Earth Engine to detect changes, map trends, and quantify differences on the 
                    Earth's surface. Earth Engine is now available for commercial use, and remains free for 
                    academic and research use. 
                    ''', className="intro-2-description-3"
                ),
                html.H2(
                    children="Swachh Vayu Dashboard", className="intro-4"
                ),
                html.P(
                    children='''
                    The dashboard monitors the concentration of atmospheric pollutants such as Aerosols, 
                    Carbon Monoxide (CO), Formaldehye (HCHO), Nitrogen Dioxide (NO\u2082), Ozone (O\u2083), 
                    and Sulphur Dioxide (SO\u2082). 
                    ''', className="intro-2-description-4"
                ),
                html.P(
                    children='''
                    The data is extracted from Sentinel-5 Precursor mission's TROPOspheric Monitoring 
                    Instrument (TROPOMI) that is avilable on Google Earth Engine. Atmospheric Pollutant 
                    data is only available for a period of three years which facilitates the user to compare 
                    the plots in the form of timeseries and moving averages. 
                    ''', className="intro-2-description-5"
                ),
                html.P(
                    children=[
                        '''
                        The concentration values are measured in molecules/m\u00b2. To view the concentration on a 
                        particular day, the cursor can be hovered over the timeseries which will display the 
                        concentration and the date at which the observation was taken. The plots can be viewed 
                        using the following links:
                        ''',
                        html.Li(dcc.Link('Year-wise Timeseries', href='/yearly-data')),
                        html.Li(dcc.Link('Multi-year Timeseries Visualization', href='/multi-year-data')),
                        html.Li(dcc.Link('Multi-year Trendlines Visualization', href='/multi-year-trend-data'))
                    ], className="intro-2-description-4"
                ),
            ],
            className="home-H2-container"
        ),
    ],
)
