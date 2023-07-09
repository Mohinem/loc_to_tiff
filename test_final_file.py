import csv

filename = 'final_file.csv'  # Replace with the actual filename

# Create an empty set to store unique dates
unique_dates = set()

# Open the CSV file
with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = row['Date']
        unique_dates.add(date)

# Count the number of unique dates
count = len(unique_dates)

print(f"Number of unique dates: {count}")
