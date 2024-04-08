# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:17:55 2024

@author: user
"""


"""
NEXT STEP IS TO INTEGRATE BURST_FINDER INTO THIS, and the writing of the XMLs :)
only manual remaining part is choice of images?
"""


import sys
import os
#sys.path.append(r'D:\SNAP Scoping SNAPPY\Py/')

from osgeo import gdal
from osgeo import osr
import itertools
import threading
import time
#import sys
from SNAP_Graph_Maker import Coherence, Intensity, Stacks, SttoCoh
from Run_GPT import run_snap_gpt
from Burst_Finder import find_bursts



def Generate_CohInt(SLCs, bbox,  OutFolder, TempFolder = ''):
    start_time = time.time() 
    #Create filepaths for temporary graphs
    IXML = TempFolder + 'TempInt.xml'
    SXML = TempFolder + 'TempStack.xml'
    SCXML = TempFolder + 'TempSTtoCoh.xml'
    
    #Create locations of temporary files
    Temp_Stacks = [TempFolder + 'TempStack_Preevent.dim',
                  TempFolder + "TempStack_Coevent.dim"
                  ]
    #tempstack2 was coevent
    #Therefore Coh2 was event
    Outputs = [OutFolder + "Coh_PreEvent.tif",
               OutFolder + "Coh_CoEvent.tif",
               OutFolder + "IntPostEvent.tif",
               OutFolder + "IntPreEvent.tif"
        
        ]
    
    
    #Identify the appropriate swaths for each SLC Image
    Swaths = [find_bursts(SLCs[0], bbox, TempFolder),
              find_bursts(SLCs[1], bbox, TempFolder),
              find_bursts(SLCs[2], bbox, TempFolder)]
    
    #Call xml makers from Snap Graph Maker
    Intensity(SLCs[0:2],Outputs[2:4], Swaths[0:2], IXML)
    #Coherence(SLCs,Outputs[0:2], Swaths, CXML)
    Stacks(SLCs, Temp_Stacks, Swaths, SXML)
    SttoCoh(Temp_Stacks, Outputs[0:2], SCXML)
    
    print('Running Intensity GPT...')
    try:
        #Think I might need to split this into 2 to save memory :(
        run_snap_gpt(IXML)
        
    except ValueError as e:
        print('proces failed', e)
    end_time = time.time()  # Record the end time
    duration = end_time - start_time  # Calculate the duration

    print(f"The Intensity processing took {duration:.2f} seconds.")
    
    print('Running Coherence GPT Step 1 - Stack Creation...')
    try:
        run_snap_gpt(SXML)       
    except ValueError as e:
        print('proces failed', e)
    end_time = time.time()  # Record the end time
    duration = end_time - start_time  # Calculate the duration
    print(f"The Total processing so far is {duration:.2f} seconds.")

    print('Running Coherence GPT Step 2 - Coherence Calculation...')
    try:
        #Think I might need to split this into 2 to save memory :(
        #this took ~15 minutes
        run_snap_gpt(SCXML)
        #run_snap_gpt(SXML)
        #gpt(CXML, tmpdir=r'D:\SNAP Scoping SNAPPY\Data\Haiti\tempDIR')
        
    except ValueError as e:
        print('proces failed', e)
    end_time = time.time()  # Record the end time
    duration = end_time - start_time  # Calculate the duration


    print(f"The Total processing took {duration:.2f} seconds.")

def align_raster(input_raster, reference_raster, output_raster):
    """
    Aligns the input raster to the reference raster using GDAL's Warp function.
    
    Parameters:
        input_raster (str): Path to the input raster file.
        reference_raster (str): Path to the reference raster file.
        output_raster (str): Path to save the aligned output raster file.
    """
    # Open input raster
    input_ds = gdal.Open(input_raster)
    if input_ds is None:
        print("Error: Could not open input raster file")
        return
    
    # Open reference raster
    reference_ds = gdal.Open(reference_raster)
    if reference_ds is None:
        print("Error: Could not open reference raster file")
        return
    
    # Get projection and geotransform of reference raster
    reference_proj = reference_ds.GetProjection()
    reference_geotrans = reference_ds.GetGeoTransform()
    
    # Warp input raster to align with reference raster
    warped_ds = gdal.Warp(output_raster, input_ds, dstSRS=reference_proj, 
                           outputBounds=(reference_geotrans[0], reference_geotrans[3] + reference_geotrans[5] * input_ds.RasterYSize,
                                         reference_geotrans[0] + reference_geotrans[1] * input_ds.RasterXSize, reference_geotrans[3]),
                           resampleAlg=gdal.GRA_Lanczos)
    
    # Close datasets
    input_ds = None
    reference_ds = None
    warped_ds = None
    
    print("Raster alignment complete. Aligned raster saved as:", output_raster)

"""
SLCs = [r'D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20160924T230106_20160924T230136_013201_014FFD_C367.zip',
        r'D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20160831T230105_20160831T230135_012851_014491_81F2.zip',
        r'D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20161018T230106_20161018T230136_013551_015B0D_CF53.zip']
Outputs = [r'D:\SNAP Scoping SNAPPY\Data\Generated\Coh1_Orb_Stack_Coh_Deb_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Coh2_Orb_Stack_Coh_Deb_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Int1_Orb_Cal_Deb_ML_dB_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Int2_Orb_Cal_Deb_ML_dB_TC.tif']

Temp_Stacks=[r'D:\SNAP Scoping SNAPPY\Data\Generated\AutoStack1.dim',
             r'D:\SNAP Scoping SNAPPY\Data\Generated\AutoStack2.dim']
"""
#Indonesia
"""
SLCs = [r'D:\SNAP Scoping SNAPPY\Data\Indonesia/S1A_IW_SLC__1SDV_20180607T214242_20180607T214309_022256_026888_17C7.zip',
        r'D:\SNAP Scoping SNAPPY\Data\Indonesia/S1A_IW_SLC__1SDV_20181005T214237_20181005T214305_024006_029F71_5227.zip',
        r'D:\SNAP Scoping SNAPPY\Data\Indonesia/S1A_IW_SLC__1SDV_20180526T214241_20180526T214308_022081_026308_CE8E.zip']
Outputs = [r'D:\SNAP Scoping SNAPPY\Data\Generated\Ind_Coh1_Orb_Stack_Coh_Deb_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Ind_Coh2_Orb_Stack_Coh_Deb_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Ind_Int1_Orb_Cal_Deb_ML_dB_TC.tif',
           r'D:\SNAP Scoping SNAPPY\Data\Generated\Ind_Int2_Orb_Cal_Deb_ML_dB_TC.tif']
Temp_Stacks=[r'D:\SNAP Scoping SNAPPY\Data\Generated\IAutoStack1.dim',
             r'D:\SNAP Scoping SNAPPY\Data\Generated\IAutoStack2.dim']
#Swaths = ['2','7']
"""

"""
SLCs = [r"D:\SNAP Scoping SNAPPY\Data\Pinery\S1A_IW_SLC__1SDV_20151121T200447_20151121T200514_008707_00C64A_B69F.zip",
        r"D:\SNAP Scoping SNAPPY\Data\Pinery\S1A_IW_SLC__1SDV_20151203T200447_20151203T200515_008882_00CB35_816B.zip",
        r"D:\SNAP Scoping SNAPPY\Data\Pinery\S1A_IW_SLC__1SDV_20151109T200453_20151109T200520_008532_00C156_4FED.zip"]

SLCs = [r"D:\SNAP Scoping SNAPPY\Data\Michael\S1A_IW_SLC__1SDV_20180927T234535_20180927T234604_023891_029B92_D133.zip",
        r"D:\SNAP Scoping SNAPPY\Data\Michael\S1A_IW_SLC__1SDV_20181021T234535_20181021T234605_024241_02A705_9779.zip",
        r"D:\SNAP Scoping SNAPPY\Data\Michael\S1A_IW_SLC__1SDV_20180903T234534_20180903T234604_023541_029049_5AC2.zip"]
"""
#temp_folder = r'D:\SNAP Scoping SNAPPY\Data\Temp/'
#bbox = [-85.781937,30.070112,-85.599289,30.336706]
#OutFolder = r'D:\SNAP Scoping SNAPPY\Data\Michael/'

#Generate_CohInt(SLCs, bbox,  OutFolder, TempFolder = temp_folder)









#Orbit file download doesn't work - need to use external orbit file download package to operate.

#if this runs successfully it will run for some time with no prompts. Maybe add a time tracker or something just to prove python is still running?


"""
BELOW - IF THIS STILL DONT WORK SPLIT OUT INTO COREGISTRATION FIRST, SAVED AS BEAM-DIMAP, THEN COHERENCE ESTIMATION?

THIS TIME STARTED AT AROUND 12:15-20
"""

#time.sleep(3)



#Take intensity and resample to coherence



