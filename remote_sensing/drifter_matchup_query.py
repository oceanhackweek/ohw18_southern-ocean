import os
import numpy as np
import matplotlib
import xarray as xr
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt
import netCDF4 as nc
import pandas as pd
import subset_data_MUR_prg

import tkinter as tk
from tkinter import filedialog as fd


# Import a trajectory

# Set up data pathways
root = tk.Tk()
root.withdraw() # close out of Tk dialog box
fid = fd.askopenfilename(title = "select an ARGO trajectory *.nc file", filetypes = (("netCDF","*.nc"),("all files","*.*")))
root.update() # close the file selection window


#
ds_ARGO = xr.open_dataset(fid)
trk_ARGO = ds_ARGO[['JULD','LATITUDE','LONGITUDE']].to_dataframe()

# Query Options
date_min = trk_ARGO['JULD'].min()
date_max = trk_ARGO['JULD'].max()

max_lat = trk_ARGO['LATITUDE'].max()
min_lat = trk_ARGO['LATITUDE'].min()
max_lon = trk_ARGO['LONGITUDE'].max()
min_lon = trk_ARGO['LONGITUDE'].min()

box = [min_lon,max_lon,min_lat,max_lat]

date0 = date_min.strftime('%Y%m%d')
date1 = date_max.strftime('%Y%m%d')

shortname = 'MUR-JPL-L4-GLOB-v4.1'

## DEVELOP an SST QUERY
subset_data_MUR_prg.standalone_main(shortname, date0, date1, box)
