# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.
from pathlib import Path
import csv

script_dir = Path(__file__).parent

scan_dir = script_dir
csv_file = script_dir / "file-counter/filecounts.csv"
file_types_to_track = [".py", ".txt", ".csv", ".jpg", ".png", ".md"]
file_counts = {file_type: 0 for file_type in file_types_to_track}


for file in scan_dir.glob("**/*"):
    if file.is_file() and file.suffix in file_types_to_track:
        file_counts[file.suffix] += 1

output_data = [[file_type, count] for file_type, count in file_counts.items()]

with csv_file.open("w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["File Type", "Count"])
    writer.writerows(output_data)

print("\nUpdated CSV contents:")
with csv_file.open("r") as infile:
    reader = csv.reader(infile)
    for row in reader:
        print(row)
