import csv


data = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_age.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: data.append(row)
print(data[0].keys())
#Average coronavirus cases in county:
sum = 0
totalCounties = 0
for county in data[1:]:
    if county['age_group'] != '':
        sum += float(county['totalpositive'])
        totalCounties += 1
print(sum/totalCounties)
