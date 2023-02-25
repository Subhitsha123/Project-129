import csv
import pandas as pd

file1 = "bright_stars.csv"
file2 = "dwarf_stars.csv"

data1 = []
data2 = []

with open(file1, "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data1.append(i)

with open(file2, "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data2.append(i)

header1 = data1[0]
header2 = data2[0]

star_data1 = data1[1:]
star_data2 = data2[1:]

header = header1+header2

star_data = []

for i in star_data1:
    star_data.append(i)

for j in star_data2:
    star_data.append(j)

with open("final_stars.csv", "w") as f:
    csv_writer = csv.writer(f)    

    csv_writer.writerow(header)
    csv_writer.writerows(star_data)

df = pd.read_csv("final_stars.csv")

print(df.head(5))