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

    # Create a directory 'output' to save output tiff files
    output_dir = os.getcwd() + '/output/'
    os.makedirs(output_dir, exist_ok=True)

    # Create a directory 'output_csv' to save the lat/long values in the tiff files as csv files
    output_csv_dir = os.getcwd() + '/output_csv/'
    os.makedirs(output_csv_dir, exist_ok=True)


    print(str(unique_latitudes.min()) + " , " + str(unique_latitudes.max()))
    print(str(unique_longitudes.min()) + " , " + str(unique_longitudes.max()))

    for each_date in unique_dates:
        # Find the indices of the records that match the current date
        indices = np.where(dates == each_date)[0]
        print(np.where(dates == each_date)[0])

        num_latitudes = len(unique_latitudes)
        num_longitudes = len(unique_longitudes)

        # Create a temporary array to store the counts for the current date
        all_latitudes = 1 + (int((unique_latitudes.max() - unique_latitudes.min())/0.1))
        all_longitudes = 1 + (int((unique_longitudes.max() - unique_longitudes.min())/0.1))

        print("Longitude max = " + str(unique_longitudes.max()))
        print("Longitude min = " + str(unique_longitudes.min()))

        print(str(all_latitudes) + ',' + str(all_longitudes))

        temp_array = np.zeros((all_latitudes, all_longitudes), dtype=int)

        # Create a csv file in the 'output_csv_dir' location, storing lat/long values
        output_csv_file_string = output_csv_dir + each_date + '.csv'
        output_csv_file = open(output_csv_file_string, 'w')

        # Create a csv file in the 'output_csv_dir' location, storing lat/long and time values
        output_csv_file_string_with_count = output_csv_dir + each_date + '_count.csv'
        output_csv_file_with_count = open(output_csv_file_string_with_count, 'w')

        # Set the geotransform for the raster
        x_origin = unique_longitudes.min()
        y_origin = unique_latitudes.min()  # Swap the y-origin value
        x_resolution = (unique_longitudes.max() - unique_longitudes.min()) / num_longitudes
        y_resolution = (unique_latitudes.max() - unique_latitudes.min()) / num_latitudes  


        # Create the output raster for the current date
        output_file_string = output_dir + each_date + '.tiff'
        driver = gdal.GetDriverByName('GTiff')
        output_raster = driver.Create(output_file_string, all_longitudes, all_latitudes, 1, gdal.GDT_Int32)

        x_offset = 0
        y_offset = 0
        output_raster.SetGeoTransform([x_origin + x_offset, 0.1, 0, (y_origin + y_offset), 0, 0.1])   

        transformer = output_raster.GetGeoTransform()           

        calc_lat_index = lambda x: int((x - unique_latitudes.min())/0.1)
        calc_long_index = lambda x: int((x - unique_longitudes.min())/0.1)

        # Loop through the indices and insert the counts into the temporary array
        # Also, write the temporary index latitude
        for index in indices:
            lat_index = np.where(unique_latitudes == latitudes[index])[0][0]
            lon_index = np.where(unique_longitudes == longitudes[index])[0][0]
            temp_array[calc_lat_index(unique_latitudes[lat_index]), calc_long_index(unique_longitudes[lon_index])] = counts[index]
            str_1 = str(unique_latitudes[lat_index]) + ',' + str(unique_longitudes[lon_index]) + '\n'
            output_csv_file.write(str_1)
            str_2 = str(unique_latitudes[lat_index]) + ',' + str(unique_longitudes[lon_index]) + ',' + str(counts[index]) + '\n'
            output_csv_file_with_count.write(str_2)

            # transformed_long, treansformed_lat = transformer.ApplyTransform
            # print('(' + str(unique_latitudes[lat_index]) + ',' + str(unique_longitudes[lon_index]) + '),(' + )
            

        output_csv_file.close()
        output_csv_file_with_count.close()

        raster_2d_array.append(temp_array)

        # Create the output directory for the current date


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


final_file_name = 'final_file.csv'
# raster_file_name = 'final_tiff_file.tiff'


convert_numpy_to_raster(csv_to_numpy(final_file_name))
