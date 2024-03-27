# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 01:16:26 2023

@author: user
"""

import pandas as pd
import geopandas as gpd
import os
from shapely.wkt import loads


outpath = r"D:\xBD Labels\Processed/"
json_file_path = r"D:\xBD Labels\Unprocessed\Hold/"
files = os.listdir(json_file_path)

for file in files:
    
    if 'post' in file:
        df = pd.read_json(json_file_path + file)
        data = df['features']['lng_lat']
        building_gdf = gpd.GeoDataFrame(columns=['feature_type', 'subtype', 'uid','geometry'])
        i = 0   


        for building in data:
            geometry = loads(building['wkt'])
            building_gdf.loc[i] = [building['properties']['feature_type'],building['properties']['subtype'],building['properties']['uid'],geometry]

            i = i+1
            #print(building['properties']['feature_type'])
            #print()
            
        building_gdf.set_geometry('geometry', inplace=True)
        try:
            if len(df['features']['lng_lat']) != 0:
                #print('The following one should not be empty!')
                building_gdf.to_file(outpath + file[:-5]+'.geojson', driver='GeoJSON') 

                print('DONNEE', file)
            
            else:
                print('empty one here!')
        except Exception as e:
            print('failed:', file, 'Error:',e)
            
    else:
        file='File is pre disaster'
    
    
        
    
    
