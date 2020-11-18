### 3d house project

#### what:
based on input coordinates (degrees minutes seconds) give me 3d plot of the place (currently only for part 13 on the NGI map: http://www.geopunt.be/catalogus/datasetfolder/5be63750-0f1c-46e2-b60f-479a2b6cbcc7). 
The script was based on this part of Belgium, because we knew that our coach would only give coordinates of his house during the live presentation of the project.  

#### why:
this project was the first soloproject we got during the ai data operator bootcamp at BeCode 

#### when:
i made this script in the week from the 9th - 15th november 2020. 

#### how:
using python 
step 1. take dms coordinates input of user.
step 2. convert dms coordinates to decimal degree coordinates.
step 3. using pyproj, convert dd coordinates to x,y lambert 72 (epsg 31370), because our geotiff file is based on this coordinate reference system.  
step 4. create bounding box around the x y coordinate
step 5. open geotiff file using rasterio
step 6. with rasterio package read in bounding-box from geotiff file and save to variable 
step 7. make pandas dataframe out of variable using geopandas or pandas. 
step 8. make 3d plot out of dataframe using plotly

#### who:
lucas kustermans aka kustex

#### to do:
- expand capabilities to show 3d-plot of coordinates based on more than one geotiff file. 


