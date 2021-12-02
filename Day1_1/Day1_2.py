import csv

higher = -1
highest = 0
checked_1 = checked_2 = checked_3 = 0
sum_prev = 0
with open('measurements.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    for row in csv_reader:
        checked_3 = checked_2
        checked_2 = checked_1
        checked_1 = int(row[0])

        if checked_1 == 0 or checked_2 == 0 or checked_3 == 0:
            continue;

        sum_new = checked_3 + checked_2 + checked_1
        if sum_new > sum_prev:
            higher += 1
        sum_prev = sum_new
        print(checked_1, checked_2, checked_3, sum_prev, sum_new)

print(higher)
