import csv


age = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_age.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: age.append(row)
print(age[0].keys())

statewide = []
with open("/Users/joshuaathayde/github/CourseraDataScience/statewide_cases.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: statewide.append(row)
print(statewide[0].keys())

gender = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_sex.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: gender.append(row)
print(gender[0].keys())

ethnicity = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_ethnicity.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: ethnicity.append(row)
print(ethnicity[0].keys())

#Average coronavirus cases in county:
sum = 0
totalCounties = 0
for county in age[1:]:
    if county['age_group'] != '':
        sum += float(county['totalpositive'])
        totalCounties += 1
print(sum/totalCounties)
