# Matching all the HADM_IDs
import csv

# First, read all HADM_IDs from admissions.csv into a set
admission_hadm_ids = set()
with open('admissions.csv', 'r') as admissions_file:
    reader = csv.DictReader(admissions_file)
    for row in reader:
        admission_hadm_ids.add(row['HADM_ID'])

# Now read sample10000.csv and write matching rows to a new file
with open('NOTEEVENTS 2.csv', 'r') as sample_file, open('matched_data.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(sample_file)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    matches = 0
    total = 0
    for row in reader:
        total += 1
        if row['HADM_ID'] in admission_hadm_ids:
            writer.writerow(row)
            matches += 1
    
    print(f"Found {matches} matching rows out of {total} rows in sample10000.csv")
    print(f"Data saved to matched_data.csv")
