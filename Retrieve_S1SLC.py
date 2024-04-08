# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:28:34 2024

@author: user
"""

#Reach out to ASF API
import requests
import asf_search
from tqdm import tqdm
def SearchASF(bbox, start, end):
    # Example endpoint URL
    endpoint_url = 'https://api.daac.asf.alaska.edu/services/search/param'

    # Example API request parameters
    request_params = {
        'dataset':'SENTINEL-1',
        'bbox':bbox,
        'start':start,
        'end':end,
        'processingLevel':'SLC',
        'beamMode':'IW',
        'output':'geojson'
        # Add more parameters as needed
    }

    # Make GET request
    response = requests.get(endpoint_url, params=request_params)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        # Do something with the data
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")

import json
from shapely.geometry import shape, box

def find3(FC):
    paths = []
    for feature in FC['features']:
        paths.append(feature['properties']['pathNumber'])
    for feature in FC['features']:
        if paths.count(feature['properties']['pathNumber']) >= 3:
            print(feature['properties']['pathNumber'])
            matching = []
            for mf in FC['features']:
                if mf['properties']['pathNumber'] == feature['properties']['pathNumber']:
                    matching.append(mf)
            return matching
    print('no matching features found')


def download_file(session, url, output_path):
    response = session.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    # Progress bar with tqdm
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)
    with open(output_path, 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            progress_bar.update(len(data))
    progress_bar.close()
    
    
def DownloadFLIST(FC, path, session):
    for feature in FC:
        http = feature['properties']['url']
        filename = feature['properties']['fileName']
        print('Downloading ',filename)
        download_file(session, http, path +filename,)
def read_credentials(filename):
    credentials = {}
    with open(filename, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            credentials[username] = password
    return credentials
# Replace 'YOUR_API_KEY' with your actual API key from ASF
#bboxl = (-73.77,18.18,-73.73,18.20)
#bbox = '-73.77,18.18,-73.73,18.20'
#start = 'August+31+2016'
#end = 'October+20+2016'

#BELOW FOR PALAU
bbox = '119.751663,-0.983915,119.938431,-0.703107'
start= '28+July+2018'
end='28+October+2018'

Data = SearchASF(bbox, start, end)

SLCs = find3(Data)

path = r'D:\SNAP Scoping SNAPPY\Data\Haiti/'

session = asf_search.ASFSession().auth_with_creds('USER',"PASS")
#DownloadFLIST(SLCs, path, session)
