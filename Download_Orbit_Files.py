# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:37:26 2024

@author: user
"""
#https://github.com/scottstanie/sentineleof
#conda install -c conda-forge sentineleof

import eof
from eof.download import download_eofs

def download_from_list(orbList, Folder):
    for file in orbList:
        #Need some logic here to figure out where to save each orbit file
        save_dir= 
        download_eofs(sentinel_file=file, save_dir='')
#download_eofs([datetime.datetime(2018, 5, 3, 0, 0, 0)])
#download_eofs(sentinel_file = "D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20160831T230105_20160831T230135_012851_014491_81F2.zip")
#download_eofs(sentinel_file = "D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20160924T230106_20160924T230136_013201_014FFD_C367.zip")
#download_eofs(sentinel_file = "D:\SNAP Scoping SNAPPY\Data\Haiti\S1A_IW_SLC__1SSV_20161018T230106_20161018T230136_013551_015B0D_CF53.zip")