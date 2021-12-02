import csv

horizontal = 0
depth = 0
aim = 0
with open('input.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        command = row[0]
        direction = int(row[1])
        if command == 'up':
            aim -= direction
        elif command == 'down':
            aim += direction
        else:
            horizontal += direction

        print(row[0], row[1])
print(horizontal, depth, horizontal*depth)