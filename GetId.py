import numpy as np
import urllib, json


url = "http://gwis.jrc.ec.europa.eu/rest/current/grid_data/?format=json&offset=0"
url = "http://gwis.jrc.ec.europa.eu/rest/current/grid_data/?format=json&limit=1000&offset=38000"
response = urllib.urlopen(url)
data = json.loads(response.read())


ids = []
urls = []
lats = []
lons = []

for j in range(668):
  print url, len(ids)
  response = urllib.urlopen(url)
  data = json.loads(response.read())

  url = data['next']

  for i in range(1000):
    idGrid = data['results'][i]['id']
    coord = data['results'][i]['centroid']['coordinates']
  
    if coord[0] > 27.9308 and coord[0] < 28.6274:
      if coord[1] > -17.1263 and coord[1] < -16.9532:
        ids.append(idGrid)
        urls.append(url)
        lats.append(coord[0])
        lon.append(coord[1])
    
  
print ids, urls, lats, lons
