import csv


data = []
with open("/Users/joshuaathayde/github/CourseraDataScience/statewide_cases.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: data.append(row)

#Average coronavirus cases in county:
sum = 0
totalCounties = 0
for county in data[1:]:
    if county['totalcountconfirmed'] != '':
        sum += float(county['totalcountconfirmed'])
        totalCounties += 1
print(sum/totalCounties)
