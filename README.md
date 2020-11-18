### 3d house project

#### What:
<p>Based on input coordinates (degrees minutes seconds) give me 3d plot of the place (currently only for part 13 on the NGI map: http://www.geopunt.be/catalogus/datasetfolder/5be63750-0f1c-46e2-b60f-479a2b6cbcc7).<br> 
The script was based on this part of Belgium, because we knew that our coach would only give coordinates of his house during the live presentation of the project.  

#### Why:
This project was the first soloproject we got during the ai data operator bootcamp at BeCode. The goal was to 'consolidate' our knowledge of certain packages (numpy, pandas, matplotlib) that we learned to use during the first month of the bootcamp. Working with new libraries was also part of the challenge.  

#### When:
I made this script in the week from the 9th - 15th november 2020. 

#### How:
Using python<br> 
The geotiff file used in the script is located inside the k_13.zip.<br> 
You can find it at: http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m</p>

- step 1. Take dms coordinates input of user.
- step 2. Convert dms coordinates to decimal degree coordinates.
- step 3. Using pyproj, convert dd coordinates to x,y lambert 72 (epsg 31370), because our geotiff file is based on this coordinate reference system.  
- step 4. Create bounding box around the x y coordinate.
- step 5. Open geotiff file using rasterio.
- step 6. With rasterio package read in bounding-box from geotiff file and save to variable. 
- step 7. Make pandas dataframe out of variable using geopandas or pandas. 
- step 8. Make 3d plot out of dataframe using plotly.

#### Who:
Lucas Kustermans aka Kustex

#### To do:
- Expand capabilities to show 3d-plot of coordinates based on more than one geotiff file. 


