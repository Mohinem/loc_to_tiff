# loc_to_tiff
Converts loc file to TIFF file

This set of python programs can convert a Loc file to a TIFF file, for the lightning datasets.

Explanation of each python file-

1. loc_to_intermediate.py -> Takes the loc file name and converts it to an intermediate csv file.

2. intermediate_to_final.py -> Takes a file-name (actually, the file-name generated in the previous step) and converts to a final csv file.

3. final_to_tiff.py -> Takes the final name of the file generated by the previous python program, and file name of output raster file.

4. 4. loc_to_raster_complete.py -> Takes input file name and final tiff file name as command line arguments and runs all the three python programs to produce final tiff file. Deletes the intermediate and final csv files.

The best way is to run loc_to_raster_complete.py is by command line.
  Command that worked on my pc-

   python3 loc_to_raster_complete.py '/home/mohinem/Downloads/Loc to Rasdaman/A20220601.loc' '/home/mohinem/Downloads/Loc to Rasdaman/final_tiff_file.tiff'

Format of command-

python3 loc_to_raster_complete.py <input file name> <tiff file name>


Please ask if any questions !
