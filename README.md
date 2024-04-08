# SAR-ML-Post-Disaster-Damage-Detection
This is a set of tools which was used to test the performs of machine learning to detect damage to buildings from natural disasters using Synthetic Aperture Radar (SAR).

# Tools
This includes:<br>
<b> Create CNN Scene</b>:
this takes functions from Retrieve_S1SLC, SNAP_Graph_Maker, Generate_Coherence_Intensity and Burst_Finder to produce 2 Intensity images (pre-event and post-event) and 2 Coherence images (pre-event and co-event)
<br>
<b> SNAP Graph Maker </b>:
this takes inputs regarding S1SLC inputs and scene attributes and generates a SNAP graph (XML) file for interfacing with and running the SNAP Graph Processing Tool
<b> Clean xBD Labels </b>:
this takes the geojson labels provided in the xview2 dataset and turns them into georeferenced polygons. and input and output folder is the only inputs required.
<br>
<b> Burst Finder: </b>
Finds appropriate swath and subswath given a bounding box and SLC zip.
