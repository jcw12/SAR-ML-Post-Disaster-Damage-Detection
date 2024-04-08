import xml.etree.ElementTree as ET
from shapely.geometry import Polygon
import geopandas as gpd


import os
import zipfile
import tempfile
import shutil

from shapely.geometry import box

def find_bursts(SLC_path, bbox, temp_folder):
    XMLs = find_annotations(SLC_path, temp_folder)
    swaths = XMLstoPolys(XMLs)
    for i in range(1,4):
        intersecting = intersecting_features(swaths[i], bbox)
        if len(intersecting) != 0:
            print('SWATH:',i, min(intersecting['Burst']), max(intersecting['Burst']))
            
            #Swath, MinBurst, MaxBurst
            return i, min(intersecting['Burst']), max(intersecting['Burst'])
    #intersecting = intersecting_features(bursts, bbox)
    #print(intersecting)
    
    

def intersecting_features(gdf, bbox):
    # Create a bounding box geometry
    bbox_geom = box(*bbox)
    
    # Check for intersection
    intersecting = gdf[gdf.geometry.intersects(bbox_geom)]
    
    return intersecting

def find_annotations(SLC_path, temp_folder):
    annos = []
    new_file_paths = []
    with zipfile.ZipFile(SLC_path, 'r') as zip:
        for name in zip.namelist():
            if 'annotation/s1a-iw' in name and 'vv' in name:
                annos.append(name)
                # Extract file directly to temp_folder without preserving folder structure
                filename = os.path.basename(name)
                new_file_path = os.path.join(temp_folder, filename)
                with zip.open(name) as source, open(new_file_path, 'wb') as target:
                    target.write(source.read())
                new_file_paths.append(new_file_path)

    return new_file_paths


def XMLstoPoly(XMLs):
    merged_gdf = None
    for XML in XMLs:
        
        if 'iw1' in XML:
            iw = 1
        elif 'iw2' in XML:
            iw = 2
        elif 'iw3' in XML:
            iw = 3
        
        tree = ET.parse(XML)
        root = tree.getroot()

        # Initialize lists to store latitude and longitude coordinates
        latitudes = []
        longitudes = []

        # Iterate over geolocationGridPoint elements
        for point in root.findall('.//geolocationGridPoint'):
            latitude = float(point.find('latitude').text)
            longitude = float(point.find('longitude').text)
            latitudes.append(latitude)
            longitudes.append(longitude)

        # Determine the number of polygons to create
        num_points = len(latitudes)
        num_polygons = min(num_points // 21, 10) if num_points >= 21 else 1

        # Group coordinates into sets of 4 to form polygons
        polygons = []
        for i in range(0, num_points, 21):  # Starting from 0 and with a step of 21
            if i + 41 < num_points:  # Ensure there are enough points to form a polygon
                polygon_points = []
                polygon_points.append((longitudes[i], latitudes[i]))
                polygon_points.append((longitudes[i + 20], latitudes[i + 20]))
                polygon_points.append((longitudes[i + 41], latitudes[i + 41]))
                polygon_points.append((longitudes[i + 21], latitudes[i + 21]))  # First rectangle
                polygons.append(Polygon(polygon_points))

        # Create a GeoDataFrame from the polygons
        gdf = gpd.GeoDataFrame(geometry=polygons)

        # Add a column for polygon numbers
        gdf['Burst'] = range(1, len(polygons) + 1)
        #gdf['Swath'] = int(iw)

        if merged_gdf is None:
            merged_gdf = gdf
        else:
            merged_gdf = merged_gdf.append(gdf, ignore_index=True)
    return merged_gdf

def XMLstoPolys(XMLs):
    GDFs = {}
    for XML in XMLs:
        
        if 'iw1' in XML:
            iw = 1
        elif 'iw2' in XML:
            iw = 2
        elif 'iw3' in XML:
            iw = 3
        
        tree = ET.parse(XML)
        root = tree.getroot()

        # Initialize lists to store latitude and longitude coordinates
        latitudes = []
        longitudes = []

        # Iterate over geolocationGridPoint elements
        for point in root.findall('.//geolocationGridPoint'):
            latitude = float(point.find('latitude').text)
            longitude = float(point.find('longitude').text)
            latitudes.append(latitude)
            longitudes.append(longitude)

        # Determine the number of polygons to create
        num_points = len(latitudes)
        num_polygons = min(num_points // 21, 10) if num_points >= 21 else 1

        # Group coordinates into sets of 4 to form polygons
        polygons = []
        for i in range(0, num_points, 21):  # Starting from 0 and with a step of 21
            if i + 41 < num_points:  # Ensure there are enough points to form a polygon
                polygon_points = []
                polygon_points.append((longitudes[i], latitudes[i]))
                polygon_points.append((longitudes[i + 20], latitudes[i + 20]))
                polygon_points.append((longitudes[i + 41], latitudes[i + 41]))
                polygon_points.append((longitudes[i + 21], latitudes[i + 21]))  # First rectangle
                polygons.append(Polygon(polygon_points))

        # Create a GeoDataFrame from the polygons
        gdf = gpd.GeoDataFrame(geometry=polygons)

        # Add a column for polygon numbers
        gdf['Burst'] = range(1, len(polygons) + 1)
        #gdf['Swath'] = int(iw)

        GDFs[iw] = gdf
    return GDFs


#find_bursts(r"D:\SNAP Scoping SNAPPY\Data\Indonesia\S1A_IW_SLC__1SDV_20180607T214242_20180607T214309_022256_026888_17C7.zip",[119.751663,-0.983915,119.938431,-0.703107],r'E:\TempSAR/')

#x = find_annotations("D:\SNAP Scoping SNAPPY\Data\Indonesia\S1A_IW_SLC__1SDV_20180607T214242_20180607T214309_022256_026888_17C7.zip",r'E:\TempSAR/')
#gdfs = XMLstoPolys(x)
#gdf = XMLstoPoly(x)


"""
# Example usage
zip_file_path = 'example.zip'
output_folder = 'output'
extract_xml_from_zip(zip_file_path, output_folder)
    
    

# Parse the XML file
tree = ET.parse(r'E:/TempSAR/S1A_IW_SLC__1SDV_20181005T214237_20181005T214305_024006_029F71_5227.SAFE/annotation/s1a-iw2-slc-vv-20181005t214238-20181005t214304-024006-029f71-005.xml')
root = tree.getroot()

# Initialize lists to store latitude and longitude coordinates
latitudes = []
longitudes = []

# Iterate over geolocationGridPoint elements
for point in root.findall('.//geolocationGridPoint'):
    latitude = float(point.find('latitude').text)
    longitude = float(point.find('longitude').text)
    latitudes.append(latitude)
    longitudes.append(longitude)

# Determine the number of polygons to create
num_points = len(latitudes)
num_polygons = min(num_points // 21, 10) if num_points >= 21 else 1

# Group coordinates into sets of 4 to form polygons
polygons = []
for i in range(0, num_points, 21):  # Starting from 0 and with a step of 21
    if i + 41 < num_points:  # Ensure there are enough points to form a polygon
        polygon_points = []
        polygon_points.append((longitudes[i], latitudes[i]))
        polygon_points.append((longitudes[i + 20], latitudes[i + 20]))
        polygon_points.append((longitudes[i + 41], latitudes[i + 41]))
        polygon_points.append((longitudes[i + 21], latitudes[i + 21]))  # First rectangle
        polygons.append(Polygon(polygon_points))

# Create a GeoDataFrame from the polygons
gdf = gpd.GeoDataFrame(geometry=polygons)

# Add a column for polygon numbers
gdf['polygon_number'] = range(1, len(polygons) + 1)

# Save the GeoDataFrame to a shapefile
output_shapefile = r'E:\TempSAR\polyddgons.shp'
gdf.to_file(output_shapefile)

print("Shapefile saved successfully!")
"""