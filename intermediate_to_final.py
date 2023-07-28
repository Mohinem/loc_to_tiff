
import time
import datetime


intermediate_file_name = 'intermediate_file.csv'
final_file_name = 'final_file.csv'

def intermediate_to_final(intermediate_file_name, final_file_name):
    # Step 1. Open intermediate file
    intermediate_file = open(intermediate_file_name, 'r')

    # Step 2. Open final file
    final_file = open(final_file_name, 'w')

    # Step 3. Copy the timestamp(date), latitude, longitude and count in the dictionary

    count_dict = dict()

    for each_line in intermediate_file:
        elements = each_line.split(',')
        timestamp_value, lat, lon= [e.strip() for e in elements]

        # date_value = datetime.datetime.fromtimestamp(int(timestamp_value)).strftime('%d-%m-%y')
        # Convert timestamp_value to datetime object
        timestamp_dt = datetime.datetime.fromtimestamp(int(timestamp_value))

        # Modify the timestamp to have "00" as the last two digits and add a "Z" sign
        date_value = timestamp_dt.replace(minute=0, second=0, microsecond=0).isoformat() + ".000" + "Z"

        dict_tuple = (date_value, lat, lon)

        if dict_tuple not in count_dict:
            count_dict[dict_tuple]=1
        else:
            count_dict[dict_tuple] = count_dict[dict_tuple]+1    

    intermediate_file.close()

    final_file.write('Date,Lat,Long,Count\n')

    for bc in count_dict:
        final_string = bc[0] + ',' + bc[1] + ',' + bc[2] + ',' + str(count_dict[bc]) + '\n'
        final_file.write(final_string)
        # print(final_string)

    final_file.close()




# intermediate_to_final(intermediate_file_name, final_file_name)