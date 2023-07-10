import csv

filename = 'final_tiff_file.tiff'  # Replace with the actual filename

from PIL import Image

image = Image.open(filename)
print(image.size)