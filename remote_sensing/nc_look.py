import numpy as np
import netCDF4 as nc
import matplotlib

fid = 'Data/argo-profiles-4901768.nc'
dataset = nc.Dataset(fid,'r')

print(dataset)
