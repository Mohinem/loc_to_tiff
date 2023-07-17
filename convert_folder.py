
import argparse
import os
import subprocess
# import loc_to_raster_complete


def main(input_folder_name):

    files = os.listdir(input_folder_name)

    for each_file in files:
        # loc_to_raster_complete(each_file)
        file_path = input_folder_name + '/' + each_file

                    # Call the second program as a command-line operation
        subprocess.run(["python3", "loc_to_raster_complete.py", file_path])
        print(file_path)

    print(input_folder_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process LOC file and convert it to a TIFF file.")
    parser.add_argument("input_folder_name", help="Input Folder Name")
    # parser.add_argument("raster_file_name", help="Output TIFF file name")
    args = parser.parse_args()

    main(args.input_folder_name)
