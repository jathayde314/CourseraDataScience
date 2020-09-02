import csv

with open("/Users/joshuaathayde/github/CourseraDataScience/statewide_cases.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(csv_reader)
    for row in csv_reader: pass

print(row)
