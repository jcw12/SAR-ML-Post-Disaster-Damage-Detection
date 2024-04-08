# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:15:12 2024

@author: user
"""

from Retrieve_S1SLC_PRIVATE import returnSession, SearchASF, DownloadFLIST, find3
from Generate_Coherence_Intensity import Generate_CohInt, align_raster


def Find_Scene(bbox, dates):
    sbbox = str(bbox[0]) +','+ str(bbox[1]) +','+  str(bbox[2]) +','+ str(bbox[3])
    session = returnSession()
    
    #Check if outfolder is made, and if not, make it.
    """
    TBC
    """
    start, end = dates
    #Download Scene Data
    Data = SearchASF(sbbox, start, end)
    """
    Filtering by SLCs might not be ideal - changing the search from scratch might b the better way. could find better scenes for a certain event. anyway
    """
    SLCs = find3(Data)
    print('Data with Matching Orbit Found for Your Dates:')
    for feature in SLCs:
        print(feature['properties']['startTime'])
    return SLCs, session

        
def Make_Scene(bbox,outfolder, SLCs, session):
    #Outpaths will be in order of date
    outpaths = DownloadFLIST(SLCs, outfolder, session)
    
    print('Generating Coherence and Intensity')
    #rearrange to be right order (Mid, Latest, Earliest)
    SLCs = [outpaths[1], outpaths[0], outpaths[2]]
    tempfolder=outfolder
    Generate_CohInt(SLCs, bbox, outfolder, tempfolder)
    Outlist = ['IntPostEvent.tif', 'IntPreEvent.tif']
    
    for input_raster in Outlist:
        align_raster(outfolder+input_raster, outfolder + 'Coh_CoEvent.tif', outfolder+'aligned'+input_raster)
    print('Scene made :)')
    
    
    
    
bbox = [36.075668,36.157835,36.229477,36.254241]
stbbox = str(bbox[0]) +','+ str(bbox[1]) +','+  str(bbox[2]) +','+ str(bbox[3])
#bbox = '-85.781937,30.070112,-85.599289,30.336706'
start= 'January+21+2023'
end='February+16+2023'
outfolder = r'D:\SNAP Scoping SNAPPY\Data\ARIA Comparison - Turkey/'
dates = [start, end]
SLCs, session = Find_Scene(bbox, dates)
Make_Scene(bbox,outfolder,SLCs,session)

print('searched')