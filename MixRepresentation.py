from scipy.io import netcdf
import gdal, ogr, osr, os
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






ds = gdal.Open('NDVI_mask.TIF')
bandNDVI = ds.GetRasterBand(1)
NDVI = bandNDVI.ReadAsArray()
xoff, a, b, yoff, d, e = ds.GetGeoTransform()

def pixel2coord(x, y):
  xp = a * x + b * y + xoff
  yp = d * x + e * y + yoff
  return np.array([xp, yp])

"""
latNDVI = []
lonNDVI = []
cropNDVI = []
for i in range(len(NDVI)):
  for j in range(len(NDVI[0])):
     pixels = pixel2coord(i,j)
     x = pixels[0]
     y = pixels[1]
     if x<-16.01 and x>-17.12:
       if y>27.93 and y<28.64:
          latNDVI.append(y)
          lonNDVI.append(x)
          cropNDVI.append(NDVI[x][y])
"""


print "Representando FWI"
plt.pcolormesh(meshLon, meshLat, riskNow, vmin=0., vmax=1.)

"""
print "Calculando coordenadas"
latNDVI = []
for i in range(len(NDVI)):
  latNDVI.append(pixel2coord(i,0)[0]) 

lonNDVI = []
for i in range(len(NDVI[0])):
  lonNDVI.append(pixel2coord(0,i)[0]) 

X,Y = np.meshgrid(lonNDVI, latNDVI)


print "Representando NDVI"
mask = NDVI==1

#plt.pcolormesh(X[100:200, 100:200], Y[100:200, 100:200], NDVI[100:200, 100:200], vmin=0., vmax=1.)
"""
#plt.xlim(-40, 0)
#plt.ylim(15, 40)

lonNDVI = []
latNDVI = []
NDVI = NDVI.T
for i in range(len(NDVI)):
   for j in range(len(NDVI[0])):
      if NDVI[i,j]==1:
        coord = pixel2coord(i,j)
        lonNDVI.append(coord[1]) 
        latNDVI.append(coord[0])  


plt.plot(latNDVI, lonNDVI, ".")
print "Guardando.."




plt.xlim(-17.1, -16.)
plt.ylim(27.75, 28.75)
plt.savefig('Mix2.png')
#cropNDVI
