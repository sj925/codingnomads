# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
import csv

script_dir = Path(__file__).parent
csv_file = script_dir / "file-counter/filecounts.csv"

if csv_file.exists():
    with open (csv_file, "r") as infile:
        reader = csv.reader(infile)
        for row in reader: 
            print(row)
else:
    print("the csv file you are trying to open does not exist")
    
data_to_write = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

with open (csv_file, "a") as outfile: 
    writer = csv.writer(outfile)
    writer.writerows(list(data_to_write.items()))
    print("data written successfully")
    


