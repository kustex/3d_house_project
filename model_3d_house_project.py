#!/usr/bin/env python

import numpy as np
import geopandas as gpd
import rasterio
import pyproj
import plotly.graph_objects as go
from pyproj import Transformer
from rasterio.enums import Resampling
from rasterio.windows import from_bounds

#convert DMS to DD
degrees_coordinate_long = float(input("What are the degrees of your longitude coordinate? "))
minutes_coordinate_long = float(input("What are the minutes of your longitude coordinate? "))
seconds_coordinate_long = float(input("What are the seconds of your longitude coordinate? ")) 
dd_long = degrees_coordinate_long + (minutes_coordinate_long/60) + (seconds_coordinate_long/3600)

degrees_coordinate_lat = float(input("What are the degrees of your latitude coordinate? "))
minutes_coordinate_lat= float(input("What are the minutes of your latitude coordinate? "))
seconds_coordinate_lat = float(input("What are the seconds of your latitude coordinate? ")) 
dd_lat = degrees_coordinate_lat + (minutes_coordinate_lat/60) + (seconds_coordinate_lat/3600)

#transform from long, lat (degrees) to x, y coordinates
transformer = Transformer.from_crs(4326,31370)
x, y = transformer.transform(dd_long, dd_lat)

#create bounding box around x, y coordinates
x_left = x - 25
x_right = x + 25
y_top = y + 25
y_bottom = y - 25

#read and plot the GeoTiff file
img = rasterio.open('data/geotif/dsm/DHMVIIDSMRAS1m_k13.tif')
rst = img.read(1, window=from_bounds(x_left, y_bottom, x_right, y_top, img.transform))

#making geodataframe out of ndarray of selection for Geotiff file
rst_gdf = gpd.GeoDataFrame(rst)

#making 3d plot 
fig = go.Figure(data=[go.Surface(z=rst_gdf.values)])
fig.update_layout(title='Surface plot', autosize=True)
fig.show()
