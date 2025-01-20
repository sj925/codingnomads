# Write the file counts to a `.csv` file.
import csv
counts = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

with open ("filecounts.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["folder", "csv", ".md", ".png"])
    writer.writeheader()
    writer.writerows


