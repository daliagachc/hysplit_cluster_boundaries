# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: ''
#     name: ''
# ---

# %% [markdown]
# project name: hysplit_cluster_boundaries
# created by diego aliaga daliaga_at_chacaltaya.edu.bo


# %%
try: from useful_scit.imps import *
except: pass
import pandas as pd
import os
import sys
import xarray as xr
import matplotlib.pyplot as plt

try: import hysplit_cluster_boundaries.util as util
except: sys.path.extend(['../../'])
try: import hysplit_cluster_boundaries.util as util
except: raise ModuleNotFoundError('install hysplit_cluster_boundaries')




# %%
source_path = '/Users/diego/hysplit_cluster_boundaries' \
              '/hysplit_cluster_boundaries'
data_path = os.path.join(source_path, 'data')

clus_name = 'cluster_simple_6_v01.csv'
radi_name = 'long_range_radials.csv'
ring_name = 'long_range_rings.csv'

# %%
df_clus = pd.read_csv(os.path.join(data_path, clus_name))
df_radi = pd.read_csv(os.path.join(data_path, radi_name))
df_ring = pd.read_csv(os.path.join(data_path, ring_name))

df_clus = df_clus.sort_values(['th_in', 'r_in'])
df_clus = df_clus.set_index(['th_in', 'r_in'])
dfu = df_clus.unstack('th_in')['lab']
dfu.columns = df_radi['radials']
dfu.index = df_ring['rings']

da_clus = df_clus.to_xarray()
rad = da_clus['th_in']*0 + df_radi['radials']
rad.name = 'radials'
da_clus=da_clus.assign_coords(radials=rad)

ring = da_clus['r_in']*0 + df_ring['rings']
ring.name = 'rings'
da_clus=da_clus.assign_coords(rings=ring)

da_clus

# %%
da_clus['lab'].plot(x='th_in', y='r_in',
                    cmap=util.ccmap, vmin=.5, vmax=6.5)
plt.show()
# %%
da_clus['w'].plot(x='th_in', y='r_in')
plt.show()
# %%



# %%
lat = util.r_th_to_lat(da_clus['rings'], da_clus['radials'])
lon = util.r_th_to_lon(da_clus['rings'], da_clus['radials'])

da_clus = da_clus.assign_coords(lat=lat)
da_clus = da_clus.assign_coords(lon=lon)
# %%
# %%
da_clus['lab'].plot(
    x='radials', y='rings',
    cmap=util.ccmap, vmin=.5, vmax=6.5,
    yscale='log', ylim=(.1, 20)
)
plt.show()
da_clus = da_clus.swap_dims({'r_in':'rings'})
da_clus = da_clus.loc[{'rings':slice(.05,20)}]
da_clus = da_clus.swap_dims({'rings':'r_in'})

# %%
ll_range = 21
lo_min = util.CHC_LON - ll_range
lo_max = util.CHC_LON + ll_range
la_min = util.CHC_LAT - ll_range
la_max = util.CHC_LAT + ll_range

da_clus['lab'].plot(
    x='lon', y='lat',
    cmap=util.ccmap, vmin=.5, vmax=6.5,
    xlim=(lo_min, lo_max),
    ylim=(la_min, la_max),
)
plt.show()

# %%
df_out = da_clus.to_dataframe()
# %%
df_out
# %%
data_out = os.path.join(source_path,'data_out')

da_clus.to_netcdf(os.path.join(data_out,'lab_weight_lat_lon_info.nc'))

labs_out = ['radials','rings','lat','lon','w','lab']
for l in labs_out:
    df_lab = df_out[l].unstack('th_in')
    df_lab.index.name = 'r|th'
    df_lab.to_csv(os.path.join(data_out,l+'.csv'))
# %%



# %%
