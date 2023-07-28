import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt


csv_location = '/home/rasdaman/loc_to_tiff/output_csv/2022-01-15T08:00:00.000Z.csv'

df = pd.read_csv(csv_location, delimiter=',', skiprows=0, low_memory=False)

print(df.head)

latitude = df.iloc[:, 0]
longitude = df.iloc[:, 1]

geometry = [Point(xy) for xy in zip(longitude, latitude)]
gdf = GeoDataFrame(df, geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

plt.savefig('plot.png', dpi=300, bbox_inches='tight')