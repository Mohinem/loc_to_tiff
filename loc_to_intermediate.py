
import time
import datetime

input_file_name = 'A20220601.loc'
intermediate_file_name = 'intermediate_file.csv'

def loc_to_intermediate(input_file_name, intermediate_file_name):

    # Step 1. Open input file
    input_file = open(input_file_name, 'r')

    # Step 2. Open intermediate file
    intermediate_file = open(intermediate_file_name, 'w')

    # Step 3. Copy the timestamp, latitude and longitude in the 
    for each_line in input_file:
        elements = each_line.split(',')
        date_value, time_value, lat, lon, _, cnt = [e.strip() for e in elements]

        date_and_time_value = date_value + ':' + time_value
        date_and_time_value = date_and_time_value.split('.')[0]
        date_format = "%Y/%m/%d:%H:%M:%S"

        timestamp_value = str(int(time.mktime(datetime.datetime.strptime(date_and_time_value, date_format).timetuple())))
        lat = str(round(float(lat),1))
        lon = str(round(float(lon),1))

        # print(timestamp_value + ',' + lat + ',' + lon)
        intermediate_file.write(timestamp_value + ',' + lat + ',' + lon+'\n')

    intermediate_file.close()

    input_file.close()

# loc_to_intermediate(input_file_name, intermediate_file_name)
