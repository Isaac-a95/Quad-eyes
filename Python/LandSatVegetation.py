import gdal, ogr, osr, os
import numpy as np
import matplotlib.pyplot as plt





REFLECTANCE_MULT_BAND_1 = 2.0000E-05
REFLECTANCE_MULT_BAND_2 = 2.0000E-05
REFLECTANCE_MULT_BAND_3 = 2.0000E-05
REFLECTANCE_MULT_BAND_4 = 2.0000E-05
REFLECTANCE_MULT_BAND_5 = 2.0000E-05
REFLECTANCE_MULT_BAND_6 = 2.0000E-05
REFLECTANCE_MULT_BAND_7 = 2.0000E-05
REFLECTANCE_MULT_BAND_8 = 2.0000E-05
REFLECTANCE_MULT_BAND_9 = 2.0000E-05
REFLECTANCE_ADD_BAND_1 = -0.100000
REFLECTANCE_ADD_BAND_2 = -0.100000
REFLECTANCE_ADD_BAND_3 = -0.100000
REFLECTANCE_ADD_BAND_4 = -0.100000
REFLECTANCE_ADD_BAND_5 = -0.100000
REFLECTANCE_ADD_BAND_6 = -0.100000
REFLECTANCE_ADD_BAND_7 = -0.100000
REFLECTANCE_ADD_BAND_8 = -0.100000
REFLECTANCE_ADD_BAND_9 = -0.100000

CORNER_UL_LAT_PRODUCT = 29.91127
CORNER_UL_LON_PRODUCT = -17.55620
CORNER_UR_LAT_PRODUCT = 29.93596
CORNER_UR_LON_PRODUCT = -15.16061
CORNER_LL_LAT_PRODUCT = 27.78498
CORNER_LL_LON_PRODUCT = -17.50470
CORNER_LR_LAT_PRODUCT = 27.80760
CORNER_LR_LON_PRODUCT = -15.15737


print "Opening B4..."
# gdalwarp LC82070402017107LGN00_B5.TIF LC82070402017107LGN00_B5_longlat.TIF -t_srs "+proj=longlat +ellps=WGS84"
ds = gdal.Open('../LandsatData/LC82070402017107LGN00/LC82070402017107LGN00_B4_longlat.TIF')


bandR = ds.GetRasterBand(1)
dataR = bandR.ReadAsArray()
dataR = REFLECTANCE_MULT_BAND_4*dataR + REFLECTANCE_ADD_BAND_4

ds = None

print "Opening B5..."
ds = gdal.Open('../LandsatData/LC82070402017107LGN00/LC82070402017107LGN00_B5_longlat.TIF')
bandNIR = ds.GetRasterBand(1)
dataNIR = bandNIR.ReadAsArray()
dataNIR = REFLECTANCE_MULT_BAND_5*dataNIR + REFLECTANCE_ADD_BAND_5



D_LON = CORNER_UL_LON_PRODUCT-CORNER_UR_LON_PRODUCT
D_LAT = CORNER_UL_LAT_PRODUCT-CORNER_LL_LAT_PRODUCT

xoff, a, b, yoff, d, e = ds.GetGeoTransform()

ds = None #Free memory

print "Computing NDVI..."
NDVI = (dataNIR-dataR)/(dataNIR+dataR)

#print "Saving NDVI image..."
#plt.imsave('NDVI.png', NDVI, cmap = 'Greens', vmin=0., vmax=1.)




"""
def pixel2coord(x, y):
  xp = a * x + b * y + xoff
  yp = d * x + e * y + yoff
  return(xp, yp)

mean = np.mean(data)*3.
"""

print "Extracting mask..."
mask = np.zeros(np.shape(NDVI))
for i in range(len(NDVI)):
   for j in range(len(NDVI[0])):
      if NDVI[i,j]>=.4:
        #pixel2coord(i,j)
        #data[i,j]
        mask[i,j] = 1

print mask
#print "Saving mask image..."
#plt.imsave('mask0_0.png', NDVI*mask, cmap='Greys')



def array2raster(rasterfn,newRasterfn,array):
    raster = gdal.Open(rasterfn)
    geotransform = raster.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    cols = raster.RasterXSize
    rows = raster.RasterYSize

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Float32)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromWkt(raster.GetProjectionRef())
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()
 
print "Saving GeoTIF masked NDVI..."
array2raster("../LandsatData/LC82070402017107LGN00/LC82070402017107LGN00_B5_longlat.TIF", "NDVI_mask_0_4.TIF", mask)



# close dataset
#ds = None


