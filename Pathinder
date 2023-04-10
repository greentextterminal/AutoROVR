import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
from shapely.geometry import LineString, Point

# import overpass  # maybe
# import folium # maybe

ox.config(log_console=True, use_cache=True)

# COORDINATES
# # Zach Lat / Long (START)
# zach_lat, zach_lon = 30.621289494918237, -96.34037747550609  # N, W
# # Kyle Field Lat / Long (END)
# kyle_lat, kyle_lon = 30.61034118687136, -96.34009337550648  # S, E
# #n, w, s, e = zach_lat, zach_lon, kyle_lat, kyle_lon
# bbox = [n, s, e, w]

# CREATE MAP BOUNDARY ENVELOPING KNOWN TEST AREAS #########################################
# use a centroid between test areas and create all encompassing map from that
# # centroid is Lot 15 30.61769691944788, -96.33631384989796
# centroid_lat, centroid_lon = 30.61769691944788, -96.33631384989796

#ENGINEERING ACTIVITIES BUILDING A
centroid_lat, centroid_lon = 30.61588, -96.33713

centroid_lat_adjustment = 0.002
centroid_lat += centroid_lat_adjustment

centroid_lon_adjustment = 0.0025
centroid_lon += centroid_lon_adjustment

adjustment = 0.01  # degrees which correspond to km
lat_max = centroid_lat + adjustment  # N
lat_min = centroid_lat - adjustment  # S
lon_max = centroid_lon + adjustment  # E
lon_min = centroid_lon - adjustment  # W

lon_adjustment = 0.002
lon_max -= lon_adjustment  # move left by making more negative
lon_min += lon_adjustment  # move right by making less negative


n, s, e, w = lat_max, lat_min, lon_max, lon_min
bbox = [n, s, e, w]
#bbox = [38.7969489, 38.6919296, -9.088, -9.2296891] # test data


# QUERY GRAPH ########################################################################
"""get walkable paths"""
graph = ox.graph_from_bbox(*bbox,
                           network_type='walk',
                           retain_all=True,
                           simplify=False)


# PROJECT GRAPH AND GET GDFS EDGES ###################################################
graph_projection = ox.project_graph(graph, to_crs='crs')  # project crs coordinates of nodes/edges on graph map
edges = ox.graph_to_gdfs(graph_projection, nodes=False)  # get connections; edges are the node connections


# FIND GEOMETRIES #####################################################################
"""Find grass and parks"""
# maybe filter
tags1 = {'leisure': 'park', 'landuse': 'grass'}  # Key val pairs for parks and grass
green_area = ox.geometries_from_bbox(*bbox, tags1)  # gets park/grass nodes

# """Find parking lots"""
tags2 = {'parking': 'surface'}
parking_area = ox.geometries_from_bbox(*bbox, tags2)  # get parking lot nodes

# """Find footpaths""" MAYBE REDUNDANT
# tags3 = {'highway': 'footway'}
# footway_area = ox.geometries_from_bbox(*bbox, tags3)


# INPUTTING COORDINATES ###############################################################
"""Input start and target destination"""
# current position of rover = start location, and user inputs target destination
# Zach Lat / Long (START)
zach_lat, zach_lon = 30.621289494918237, -96.34037747550609
# Kyle Field Lat / Long (END)
kyle_lat, kyle_lon = 30.61034118687136, -96.34009337550648



# PLOTTING ############################################################################
# areas deemed legal for traversal
"""Get plot of walkable pathways, green areas, and parking lots"""
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(11, 11))
green_area.plot(ax=ax, color='green', zorder=0)
parking_area.plot(ax=ax, color='#4C4E52', zorder=1)
edges.plot(ax=ax, color='gray', linewidth=0.5, alpha=1, zorder=2)
plt.show()
