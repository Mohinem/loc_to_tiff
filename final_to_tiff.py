import numpy as np
from osgeo import gdal

def convert_numpy_to_raster(numpy_array, output_file):
    # Extract the relevant columns from the input dataset
    dates = numpy_array[1:, 0]
    latitudes = numpy_array[1:, 1].astype(float)
    longitudes = numpy_array[1:, 2].astype(float)
    counts = numpy_array[1:, 3].astype(int)

    # Determine the unique dates, latitudes, and longitudes
    unique_dates = np.unique(dates)
    unique_latitudes = np.unique(latitudes)
    unique_longitudes = np.unique(longitudes)

    # Create a raster data array with appropriate dimensions
    num_dates = len(unique_dates)
    num_latitudes = len(unique_latitudes)
    num_longitudes = len(unique_longitudes)
    raster_data = np.zeros((num_dates, num_latitudes, num_longitudes), dtype=int)

    # Convert the date, latitude, and longitude values to indices
    date_indices = np.searchsorted(unique_dates, dates)
    latitude_indices = np.searchsorted(unique_latitudes, latitudes)
    longitude_indices = np.searchsorted(unique_longitudes, longitudes)

    # Populate the raster data array with count values
    for i in range(len(counts)):
        date_index = date_indices[i]
        latitude_index = latitude_indices[i]
        longitude_index = longitude_indices[i]
        count = counts[i]
        raster_data[date_index, latitude_index, longitude_index] = count

    # Write the raster data to a raster file using GDAL
    driver = gdal.GetDriverByName('GTiff')
    output_raster = driver.Create(output_file, num_longitudes, num_latitudes, num_dates, gdal.GDT_Int32)

    # Set axis names
    output_raster.SetMetadata({'_Axes': 'Date Lat Long'})

    # Write data to raster bands
    for i in range(num_dates):
        output_band = output_raster.GetRasterBand(i + 1)
        output_band.WriteArray(raster_data[i])
        output_band.SetDescription("Number of Lightning Strikes")
        output_band.SetMetadata({'_Slice': 'Count'})
    output_raster.FlushCache()


def csv_to_numpy(final_file_name):
    # Load the CSV file into a numpy array
    csv_data = np.genfromtxt(final_file_name, delimiter=',', dtype=str)

    return csv_data


# final_file_name = 'final_file.csv'
# raster_file_name = 'current_raster_file.tiff'


# convert_numpy_to_raster(csv_to_numpy(final_file_name), raster_file_name)
