from Student import Student
import os
import csv


def csvReader(filePath):
    with open(filePath) as csv_file:
        CSV_Reader = csv.reader(csv_file, delimiter=',')
        lin_cnt = 0
        map = {}
        for row in CSV_Reader:
            if lin_cnt == 0:
                lin_cnt += 1
            else:
                map[lin_cnt] = row
                lin_cnt += 1
    return map


Student_List = csvReader('input/students.csv')
if (not os.path.exists('output')):
    os.makedirs('output')
Report_File = open('output/outputUltimate.txt', 'w')

for value in Student_List.values():
    student = Student(int(value[0]), value[1])
    print(student.reportGenerator())
    Temp_File = open(student.reportGenerator())
    data = Temp_File.read()
    Report_File.write(data)
    Report_File.write('\n\n')
Report_File.close()

# student = Student(2, 'B')
# Second_Student = Student(1, 'A')
# student.reportGenerator()
# Second_Student.reportGenerator()

# print(os.getcwd())

# print(os.path.exists('input'))

# if (not os.path.exists('output')):
#   os.makedirs('output')

# file = open('input/marks.csv')
# data = file.readline().split(',')
# print(data)
# file.close()

# outPutFile = open('output/output.txt', "a")
# outPutFile.write('Old file is appended')
# outPutFile.write('another line')
