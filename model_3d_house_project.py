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

img = rasterio.open('data/geotif/dsm/DHMVIIDSMRAS1m_k13.tif')

#ask for coordinates
long_coordinate = float(input("What is the longitude of your coordinate?"))
lat_coordinate = float(input("What is the latidude of your coordinate?"))

#print("%0.10f %0.10f" % (long_coordinate, lat_coordinate))

long_bruge = 3.22424
lat_bruge = 51.20892

#print("%0.10f %0.10f" % (long_bruge, lat_bruge))

#transform from long, lat (degrees) to x, y coordinates
epsg31370 = Proj(init='epsg:31370')
x, y = epsg31370(long_coordinate, lat_coordinate)
print(x, y)

#create bounding box around x, y coordinates
x_left = x - 10
x_right = x + 10
y_top = y + 10
y_bottom = y - 10

#read and plot the GeoTiff file
rst = img.read(1, window=from_bounds(x_left, y_bottom, x_right, y_top, img.transform))
#rasterio.plot.show(rst, cmap='gray')

#making geodataframe out of ndarray of selection for Geotiff file
rst_gdf = gpd.GeoDataFrame(rst)

#making surfaceplot out of geodataframe
fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(0,20,1)
y = np.arange(0,20,1)
x, y = np.meshgrid(x,y)

surf = ax.plot_surface(x,y,rst_gdf, cmap=cm.coolwarm)
plt.show()
