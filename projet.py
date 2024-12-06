import folium
from folium.plugins import HeatMap

import pandas as pd
import numpy as np
import gtfs_functions

feed = gtfs_functions.Feed("gtfs_stm.zip", time_windows=[0, 6, 9, 15, 19, 22, 24])

stops = feed.stops

stops_freq = feed.stops_freq
frequency = stops_freq.loc[:,['ntrips', 'stop_name']].groupby('stop_name').sum()
locations = stops.loc[:, ['stop_name', 'stop_lat', 'stop_lon']]
union = locations.join(frequency, on='stop_name', how='inner')

lats_longs_weigth = union.loc[:, ['stop_lat', 'stop_lon', 'ntrips']]


map_obj = folium.Map(location = [45.508888, -73.561668], zoom_start = 11)
HeatMap(lats_longs_weigth).add_to(map_obj)
map_obj.save(r"D:\Ary\Cegep\Informatique\Session5\Vieille_Tech\Evaluations\projet1-aguila-valitiana\folium_map.html")
