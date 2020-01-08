# project name: hysplit_cluster_boundaries
# created by diego aliaga daliaga_at_chacaltaya.edu.bo

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

cc1 = np.array([228, 26, 28 ])  / 256
cc2 = np.array([55, 126, 184])  / 256
cc3 = np.array([77, 175, 74 ])  / 256
cc4 = np.array([152, 78, 163])  / 256
cc5 = np.array([255, 127, 0 ])  / 256
cc6 = np.array([217, 217, 43])  / 256

cc_list = [cc1,cc2,cc3,cc4,cc5,cc6]

ccmap = \
    LinearSegmentedColormap.from_list('ccmap',cc_list,N = len(cc_list))

CHC_LAT = -16.350427
CHC_LON = -68.131335

def r_th_to_lat(r, th, chc_lat=CHC_LAT, chc_lon=CHC_LON):
    lat = r * np.sin(th) + chc_lat
    return lat


def r_th_to_lon(r, th, chc_lat=CHC_LAT, chc_lon=CHC_LON):
    lon = r * np.cos(th) + chc_lon
    return lon

