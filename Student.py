import csv
import os


class Student:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name

    def getCourses(self):
        return self.csvReader('input/courses.csv')

    def getTests(self):
        return self.csvReader('input/tests.csv')

    def getMarks(self):
        return self.csvReader('input/marks.csv')

    def courseCount(self):
        Course_Set = set()
        Student_Test_List = []
        for value in self.getMarks().values():
            if int(value[1]) == self.ID:
                Student_Test_List.append(value[0])

        for test in self.getTests().values():
            if test[0] in Student_Test_List:
                Course_Set.add(test[1])

        return Course_Set

    def reportGenerator(self):
        if (not os.path.exists('output')):
            os.makedirs('output')
        Report_File = open('output/'+self.Name+'.txt', 'w')
        Report_File.write('Student: ' + str(self.ID) + ', Name: ' + self.Name)
        Report_File.write('\nTotal Average:\t\t' +
                          str(self.calcualteAverage()))
        Student_Course_ID = self.courseCount()

        for value in self.getCourses().values():
            if value[0] in Student_Course_ID:
                Report_File.write('\n\n\t\tCourse: ' +
                                  value[1] + ', Teacher: ' + value[2])
                Report_File.write('\n\t\tFinal Grade: ' +
                                  str(self.calcualteGrade(int(value[0]))))
        Report_File.close()
        return Report_File.name

    def calcualteAverage(self):
        ave = 0

        for value in self.courseCount():
            ave += self.calcualteGrade(int(value))

        return ave/len(self.courseCount())

    def calcualteGrade(self, Course_Id):
        TstId_Weight = {}
        for value in self.getTests().values():
            if int(value[1]) == Course_Id:
                TstId_Weight[value[0]] = value[2]
        sum = 0
        for value in self.getMarks().values():
            if int(value[1]) == self.ID:
                for test, weight in TstId_Weight.items():
                    if value[0] in test:
                        sum += int(value[2]) * int(weight)

        return sum/100

    def csvReader(self, filePath):
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
