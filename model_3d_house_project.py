#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import geopandas as gpd
import rasterio
from rasterio.windows import from_bounds
from rasterio.enums import Resampling
from rasterio.plot import show
from pyproj import Proj, transform
import plotly.graph_objects as go

img = rasterio.open('data/geotif/dsm/DHMVIIDSMRAS1m_k13.tif')

#convert DMS to DD
degrees_coordinate_lat = float(input("What are the degrees of your latitude coordinate?"))
minutes_coordinate_lat= float(input("What are the minutes of your latitude coordinate?"))
seconds_coordinate_lat = float(input("What are the seconds of your latitude coordinate?")) 
dd_lat = degrees_coordinate_lat + (minutes_coordinate_lat/60) + (seconds_coordinate_lat/3600)

degrees_coordinate_long = float(input("What are the degrees of your longitude coordinate?"))
minutes_coordinate_long = float(input("What are the minutes of your longitude coordinate?"))
seconds_coordinate_long = float(input("What are the seconds of your longitude coordinate?")) 
dd_long = degrees_coordinate_long + (minutes_coordinate_long/60) + (seconds_coordinate_long/3600)

print(dd_lat, dd_long)

#long_bruge = 3.22424
#lat_bruge = 51.20892

#transform from long, lat (degrees) to x, y coordinates
epsg31370 = Proj(init='epsg:31370')
x, y = epsg31370(dd_lat, dd_long)
print(y, x)

#create bounding box around x, y coordinates
x_left = x - 50
x_right = x + 50
y_top = y + 50
y_bottom = y - 50

#read and plot the GeoTiff file
rst = img.read(1, window=from_bounds(x_left, y_bottom, x_right, y_top, img.transform))
#rasterio.plot.show(rst, cmap='gray')

#making geodataframe out of ndarray of selection for Geotiff file
rst_gdf = gpd.GeoDataFrame(rst)

#making surfaceplot out of geodataframe
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#
#x = np.arange(0,80,1)
#y = np.arange(0,80,1)
#x, y = np.meshgrid(x,y)
#
#ax.plot_surface(x,y,rst_gdf, cmap=cm.coolwarm)
#plt.show()

fig = go.Figure(data=[go.Surface(z=rst_gdf.values)])
fig.update_layout(title='Surface plot', autosize=True)
fig.show()
