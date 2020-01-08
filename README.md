<!--project name: hysplit_cluster_boundaries-->
<!--created by diego aliaga daliaga_at_chacaltaya.edu.bo-->
<!--date: 1/8/20-->

This repo specifies the cluster boundaries for the 2012-2016 hysplit cluster analysis performed on Chacaltaya
- input data is contained in 3 files [here](./hysplit_cluster_boundaries/data):
    - cluster_simple_6_v01.csv  
    cluster group assignment
    - long_range_radials.csv  
    description for the radial grid
    - long_range_rings.csv  
    description for the ring grid

- More info and examples in the [notebooks](./hysplit_cluster_boundaries/notebooks).

    - Specifically [here](./hysplit_cluster_boundaries/notebooks/01_data_in_to_data_out.md)
for procedure from data in to data out (plus some useful plots).

- Output data (useful for plotting in other programs)
is contained [here](./hysplit_cluster_boundaries/data_out):
    - lab.csv : labels of each cell
    - lat.csv : center lat for each cell
    - lon.csv : center lon for each cell
    - radials.csv : center radial for each cell
    - rings.csv : center agle for each cell
    - w.csv : weigh aka normalized influence for each cell
    - lab_weight_lat_lon_info.nc : all of the above info is contained here. 

