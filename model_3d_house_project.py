#!/usr/bin/env python

import numpy as np
import geopandas as gpd
import rasterio
import pyproj
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from pyproj import Transformer
from rasterio.enums import Resampling
from rasterio.windows import from_bounds
from flask import Flask
from gevent.pywsgi import WSGIServer
from dms2dec.dms_convert import dms2dec


#read and plot the GeoTiff file
img = rasterio.open('data/geotif/dsm/DHMVIIDSMRAS1m_k13.tif')

#transform from long, lat (degrees) to x, y coordinates
transformer = Transformer.from_crs(4326,31370)

#setup api connection dash
app = dash.Dash(__name__)

#dash layout
app.layout = html.Div(style={"font-family":"verdana"}, children=[
    html.H1("3d plot of coordinate", style={'text-align': 'center'}
    ),

    html.Div(id='inputs', style={"textAlign":"center"}, children=[
        html.H3("Longitude:"),
        #ask for longitude input on dash platform
        html.Div(className='coordinate_input', children=[
            dcc.Input(id="long_d", value='51', placeholder="Input longitude degrees"
            ),
            dcc.Input(id="long_m", value='12', placeholder="Input longitude minutes"
            ),
            dcc.Input(id="long_s", value='30.1', placeholder="Input longitude seconds"
        )]),

        html.H3("Latitude:"),
        #ask for latitude input on dash platform
        html.Div(className='coordinate_input', children=[
            dcc.Input(id="lat_d", value='3', placeholder="Input latitude degrees"
            ),
            dcc.Input(id="lat_m", value='13', placeholder="Input latitude minutes"
            ),
            dcc.Input(id="lat_s", value='29.3', placeholder="Input latitude seconds"
        )]),
        html.Br(), 
        #make button 
        html.Button("PLOT IT BABY!", id='button') 
    
    ]),
    html.Div(id='outputs', children=[
        #show graph on dash platform
        dcc.Graph(id='output_container', style={"height":700, "display":"block"})
    ])
])

#dash callback
@app.callback(
    Output("output_container", "figure"),
    [Input('button', 'n_clicks')],
    state=[State("long_d", 'value'),
        State("long_m", 'value'),
        State("long_s", 'value'),
        State("lat_d", 'value'),
        State("lat_m", 'value'),
        State("lat_s", 'value')
])

def number_render(button, long_d, long_m, long_s, lat_d, lat_m, lat_s):
    #convert dms to dd coordinate
    dd_long = dms2dec(f'''{long_d}°{long_m}'{long_s}"N''')
    dd_lat = dms2dec(f'''{lat_d}°{lat_m}'{lat_s}"E''')
    #convert dd to lambert 72
    x, y = transformer.transform(dd_long, dd_lat)
    #create bounding box
    x_left = x - 100
    x_right = x + 100
    y_top = y + 100
    y_bottom = y - 100
    #read in bounding box
    rst = img.read(1, window=from_bounds(x_left, y_bottom, x_right, y_top, img.transform))
    #create geopandas dataframe out of bounding box
    rst_gdf = gpd.GeoDataFrame(rst)
    rst_gdf = rst_gdf[::-1]
    #make 3d plot out of dataframe
    fig = go.Figure(data=[go.Surface(z=rst_gdf.values)])
    fig.update_layout(autosize=True)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
