# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:16:02 2018

The file to read, plot, process the the netcdf file

@author: jieqiang
"""


from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap # basemap has many compile errors.
from mpl_toolkits import mplot3d


my_file = 'C:/Users/jieqiang/Documents/ocean_data/data/plankton.nc'
fh = Dataset(my_file, mode='r') #file handle

print(fh.file_format)

print(fh.dimensions.keys()) # 
print(fh.variables.keys()) #the varible list

# the coordinate variables
lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
# the time coordination
tmax = fh.variables['time'][:]

#the pollutions variables
diatoms = fh.variables['diatoms']
flage = fh.variables['flagellates']

print(tmax.shape) # 691 X 1
print(lons.shape) # (580, 770)
print(lats.shape) # (580, 770)
print(diatoms.shape) # (691, 580, 770)
print(flage.shape) # (691, 580, 770)


# Get some parameters for the Stereographic Projection
lon_0 = lons.mean()
lat_0 = lats.mean()

# plot the first frame of diatoms

zline = np.nanmax(diatoms[0,:,:])
print(zline)

# plot the 3d map of the value of the polution
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(lons, lats, diatoms[0,:,:], 50, cmap='viridis')

ax.set_xlabel('longtitude')
ax.set_ylabel('latitude')
ax.set_zlabel('value')

plt.show()

fh.close()
