import argparse
import os
import loc_to_intermediate as l_to_i
import intermediate_to_final as i_to_f
import final_to_tiff as f_to_tiff

def main(input_file_name):
    intermediate_file_name = 'intermediate_file.csv'
    final_file_name = 'final_file.csv'

    l_to_i.loc_to_intermediate(input_file_name, intermediate_file_name)
    i_to_f.intermediate_to_final(intermediate_file_name, final_file_name)
    f_to_tiff.convert_numpy_to_raster(f_to_tiff.csv_to_numpy(final_file_name))

    os.remove(intermediate_file_name)
    os.remove(final_file_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process LOC file and convert it to a TIFF file.")
    parser.add_argument("input_file_name", help="Input LOC file name")
    # parser.add_argument("raster_file_name", help="Output TIFF file name")
    args = parser.parse_args()

    main(args.input_file_name)
