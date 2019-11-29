from Student import Student
import os
import csv

if __name__ == "__main__":

    Student_List = Student.csvReader('input/students.csv')
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
