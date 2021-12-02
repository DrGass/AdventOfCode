import csv


higher = -1
highest = 0
with open('measurements.txt', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\n')
    for row in csv_reader:
        checked = int(row[0])
        if checked > highest:
            higher += 1
            # print(checked, highest, higher)
        highest = checked

print(higher)