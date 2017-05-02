import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

url = 'http://ies-ows.jrc.ec.europa.eu/gwis?LAYERS=ecmwf.danger_index&FORMAT=image%2Fpng&TRANSPARENT=TRUE&SINGLETILE=false&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&TIME=2017-04-29&SRS=EPSG%3A900913&DAY=2017-04-29&BBOX=-20037508.34,0,0,20037508.34&WIDTH=1024&HEIGHT=1024'


riskMap = misc.imread('ejemplo_fire.png')


plt.imshow(riskMap)


plt.show()

