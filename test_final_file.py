import csv
import folium
import os

filename = 'final_file.csv'

filename_2 = 'lat_long_list.txt'

file = open(filename, 'r')

file_2 = open(filename_2, 'w')

map = folium.Map()


for each_line in file:
    time, lat, lon, bcs = each_line.split(',')
    print(str(lat) + "," + str(lon))
    if lat=='Lat':
        print("Skip")
    else:
        folium.Marker([float(lat),float(lon)]).add_to(map)
        file_2.write(lat + ',' + lon + '\n')


# map.save("map.html")

