"""

Are you satisfied with yourself?
Can you do better?
Are you happy with good?

"""

import pandas as pd

df = pd.read_csv('MODULE-06/train.csv')

import folium
from folium import plugins
# plugins is a package

stationArr = df[['Y','X']].values  #x and y represents longitude and latitude respectively
# print(type(stationArr))


m = folium.Map(location=[stationArr[0][0],stationArr[0][1]], zoom_start=18)
#map is a funtion it requires two args
m.add_child(plugins.HeatMap(stationArr[:50000], radius=30))
m.save('MODULE-06/heatmap.html')

