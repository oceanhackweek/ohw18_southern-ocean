import numpy as np
import pandas as pd
import xarray as xr
import os

# Load

# Load sst data in as an xarray
project_pth = '/Users/Brian/Documents/Projects/oceanhackweek/ohw18_southern-ocean/remote_sensing'
data_pth = '/Data'
sst_pth = '/SST'

pth = project_pth+data_pth+sst_pth

# Load .nc files into xarray
file_list = os.listdir(pth)

print(file_list)
