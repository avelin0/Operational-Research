# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:42:47 2023

@author: avelino
"""
import math
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's radius in kilometers

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def generate_dist_matrix(points):
    n = len(points)
    distance_matrix = [[0.0] * n for _ in range(n)]
    # Generate distance matrix using Haversine formula
    for i in range(n):
        for j in range(n):
            if i != j:
                lat1, lon1 = points[i]
                lat2, lon2 = points[j]
                distance_matrix[i][j] = haversine(lat1, lon1, lat2, lon2)
    return distance_matrix


points = [
    [-48.540577179137415, -27.671422137162196],
    [-48.56566790514921, -27.675930258082644],
    [-48.52509636671357, -27.615609439201847],
    [-48.53558784624806, -27.60659198856831],
    [-48.55176243236028, -27.593260258436075],
    [-48.50346749120868, -27.578913616488954],
    [-48.45649179749506, -27.636479362331634],
    [-48.4758534389978, -27.610134265333556],
    [-48.42475106534704, -27.677998240992387]
]

dm = np.asarray(generate_dist_matrix(points))
# Print distance matrix
for row in dm:
    print(row)
