<h1>3d house project</h1>

<h2>What:</h2>
<p>Based on input coordinates (degrees minutes seconds) this script will give a 3d plot of the place on the Dash platform. Currently it is only applicable for coordinates based on part 13 of the NGI map: http://www.geopunt.be/catalogus/datasetfolder/5be63750-0f1c-46e2-b60f-479a2b6cbcc7).<br> 
The script was based on this part of Belgium, because we knew that our coach would only give coordinates of his house during the live presentation of the project.  

<h2>Example:</h2>
Place: St. Salvator's Cathedral Bruge, Belgium<br>
Coordinates: long: 51°12'19.8" lat: 3°13'17.0"<br>

<p align="center">
    <img src="/assets/st_salvathor_bruge.png" width="350">
</p>

<h2>Why:</h2>
This project was the first soloproject we got during the ai data operator bootcamp at BeCode. The goal was to 'consolidate' our knowledge of certain packages (numpy, pandas, matplotlib) that we learned to use during the first month of the bootcamp. Working with new libraries was also part of the challenge.  

<h2>When:</h2>
I made this script in the week from the 9th - 15th november 2020. 

<h2>How to make it work on your local pc:</h2>
Using python<br> 
The geotiff file used in the script is located inside the k_13.zip.<br> 
You can find it at: http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m</p>

1. Clone the repository on your local device  
2. Cd to the directory where the repo is located  
3. Create new virtualenv or activate your virtualenv  
4. run 'pip install -r requirements.txt' in your shell
5. run 'mkdir data' in your shell
6. Copy the DHVIIDSMRAS1m_k13.tif file from the k_13.zip to the 'data' folder   
7. run 'python model_3d_house_project.py' in you shell  
8. Take dms coordinates input(float) of user.  

<h2>Flow of the script:</h2>
* Take dms coordinates input(float) of user.  
* Convert dms coordinates to decimal degree coordinates.  
* Using pyproj, convert dd coordinates to x,y lambert 72 (epsg 31370), because our geotiff file is based on this coordinate reference system.  
* Create bounding box around the x y coordinate.  
* Open geotiff file using rasterio.  
* With rasterio package read in bounding-box from geotiff file and save to variable.  
* Make pandas dataframe out of variable using geopandas or pandas.  
* Make 3d plot out of dataframe using plotly.  

<h2>Who:</h2>
Lucas Kustermans aka Kustex

<h2>To do:</h2>
- Expand capabilities to show 3d-plot of coordinates based on more than one geotiff file. 


