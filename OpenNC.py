from scipy.io import netcdf
import matplotlib.pyplot as plt
import numpy as np

#ftp://ftp.nccs.nasa.gov/v2.0/fwiCalcs.GEOS-5/Default/TRMM/2017/
f = netcdf.netcdf_file('20170130.nc', 'r')

risk = f.variables['TRMM_FWI']

lat = f.variables['lat']
lon = f.variables['lon']

time = f.variables['time']

riskNow = risk[0]



meshLon, meshLat = np.meshgrid(lon[:], lat[:])

plt.pcolormesh(meshLon, meshLat, riskNow, vmin=0., vmax=1.)

#Canarias cerca
plt.xlim(-16.01, -17.12)
plt.ylim(27.93, 28.64)

#Canarias extensa
#plt.xlim(-40, 0)
#plt.ylim(15, 40)

plt.show()

