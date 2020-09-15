import csv
import numpy as np
import scipy as sp


age = np.empty
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_age.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        temp = np.empty
        for val in row.values():
            np.append(temp, val)
        np.append(age, temp)
        print(np.shape(temp))
print(np.shape(age))

statewide = []
with open("/Users/joshuaathayde/github/CourseraDataScience/statewide_cases.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: statewide.append(row)
statewide = np.array(statewide)
print(statewide[0].keys())

gender = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_sex.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: gender.append(row)
gender = np.array(gender)
print(gender[0].keys())

ethnicity = []
with open("/Users/joshuaathayde/github/CourseraDataScience/case_demographics_ethnicity.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: ethnicity.append(row)
ethnicity = np.array(ethnicity)
print(ethnicity[0].keys())
