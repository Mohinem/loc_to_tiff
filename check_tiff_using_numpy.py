from PIL import Image
import numpy as np

image_location = '/home/rasdaman/loc_to_tiff/output/2022-06-01T00:00:00.000Z.tiff'

image_file = Image.open(image_location)
# image_file.show()

data = np.array(image_file)

print(data.shape)

import tifffile

tif_tags = {}
with tifffile.TiffFile(image_location) as tif:

    for tag in tif.pages[0].tags.values():
        name, value = tag.name, tag.value
        tif_tags[name] = value
        print(name)
    image = tif.pages[0].asarray()


from osgeo import gdal
import matplotlib.pyplot as plt
  
  
dataset = gdal.Open(image_location)

print(dataset.RasterCount)

band1 = dataset.GetRasterBand(1)

print(band1)

b1 = band1.ReadAsArray()
print(type(b1))
# print(np.nonzero(b1))
f = plt.figure()
plt.imshow(b1)
# plt.savefig('Tiff.png')
plt.show()


rows, cols = b1.shape

geotransform = dataset.GetGeoTransform()

final_csv_file_name = 'raster_to_geo.csv'

coordinates = np.zeros((rows, cols, 2))

for row in range(rows):
    for col in range(cols):
        x_geo, y_geo = gdal.ApplyGeoTransform(geotransform, col, row)
        # Store the geotransformed coordinates in the array
        coordinates[row, col, 0] = x_geo
        coordinates[row, col, 1] = y_geo


















# final_csv_file_name = 'tiff_unshifted_4.csv'

# nonzero_x = np.nonzero(b1)[0]
# nonzero_y = np.nonzero(b1)[1]

# final_csv_file = open(final_csv_file_name, 'w')

# for i in range(0,len(nonzero_x)):
#     output_string = str(nonzero_x[i]) + ',' + str(nonzero_y[i]) + '\n'
#     print(output_string)
#     final_csv_file.write(output_string)

# final_csv_file.close()

# dataset_in_gdal = gdal.Open(image_location)

# print(dataset_in_gdal.GetGeoTransform())
# print('hola')

# projection_wkt = dataset_in_gdal.GetProjection()
# print(projection_wkt)

# print(dataset_in_gdal.GetMetadata())
# print(dataset_in_gdal.RasterCount)
# print(dataset_in_gdal.RasterXSize)
# print(dataset_in_gdal.RasterYSize)
# print('Que Tal ?')

# print(dataset_in_gdal.GetGCPs())

# ro