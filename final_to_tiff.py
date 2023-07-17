import numpy as np
from osgeo import gdal
import os

def convert_numpy_to_raster(numpy_array):
    # Extract the relevant columns from the input dataset
    dates = numpy_array[1:, 0]
    latitudes = numpy_array[1:, 1].astype(float)
    longitudes = numpy_array[1:, 2].astype(float)
    counts = numpy_array[1:, 3].astype(int)

    # Determine the unique dates, latitudes, and longitudes
    unique_dates = np.unique(dates)
    unique_latitudes = np.unique(latitudes)
    unique_longitudes = np.unique(longitudes)

    raster_2d_array = []

    output_dir = os.getcwd() + '/output/'
    os.makedirs(output_dir, exist_ok=True)


    print(str(unique_latitudes.min()) + " , " + str(unique_latitudes.max()))
    print(str(unique_longitudes.min()) + " , " + str(unique_longitudes.max()))

    for each_date in unique_dates:
        # Find the indices of the records that match the current date
        indices = np.where(dates == each_date)[0]
        print(np.where(dates == each_date)[0])

        num_latitudes = len(unique_latitudes)
        num_longitudes = len(unique_longitudes)

        # Create a temporary array to store the counts for the current date
        temp_array = np.zeros((num_latitudes, num_longitudes), dtype=int)

        # Loop through the indices and insert the counts into the temporary array
        for index in indices:
            lat_index = np.where(unique_latitudes == latitudes[index])[0][0]
            lon_index = np.where(unique_longitudes == longitudes[index])[0][0]
            temp_array[lat_index, lon_index] = counts[index]

        raster_2d_array.append(temp_array)

        # Create the output directory for the current date

        # Create the output raster for the current date
        output_file_string = output_dir + each_date + '.tiff'
        driver = gdal.GetDriverByName('GTiff')
        output_raster = driver.Create(output_file_string, num_longitudes, num_latitudes, 1, gdal.GDT_Int32)

        # Set the geotransform for the raster
        x_origin = unique_longitudes.min()
        y_origin = unique_latitudes.max()  # Swap the y-origin value
        x_resolution = (unique_longitudes.max() - unique_longitudes.min()) / num_longitudes
        y_resolution = (unique_latitudes.max() - unique_latitudes.min()) / num_latitudes


        x_offset = 20
        y_offset = 0
        output_raster.SetGeoTransform([x_origin + x_offset, x_resolution, 0, y_origin + y_offset, 0, -y_resolution])

        # output_raster.SetGeoTransform((-130, 0.10, 0.0, 91.6, 0.0, -0.1))

        geotransform = output_raster.GetGeoTransform()
        print(geotransform)

        output_raster.SetMetadata({'_Axes': 'Lat Long'})

        output_band = output_raster.GetRasterBand(1)
        output_band.SetNoDataValue(0)  # Set nodata value to 0
        # print("Temp array - ")
        # print(temp_array)
        # # print("Size -")
        # # print(temp_array.size)
        # print("Number of non zero values = " + str(np.count_nonzero(temp_array)))
        # print("Number of zero values = " + str(int(temp_array.size) - int(np.count_nonzero(temp_array))))
        output_band.WriteArray(temp_array)
        output_band.SetDescription("Number of Lightning Strikes")
        output_band.SetMetadata({'_Slice': 'Count'})
        # break



def csv_to_numpy(final_file_name):
    # Load the CSV file into a numpy array
    csv_data = np.genfromtxt(final_file_name, delimiter=',', dtype=str)

    return csv_data


# final_file_name = 'final_file.csv'
# raster_file_name = 'final_tiff_file.tiff'


# convert_numpy_to_raster(csv_to_numpy(final_file_name))
