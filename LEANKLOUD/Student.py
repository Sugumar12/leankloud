#Python Code for Part-II

import csv

def findMaxTotalFunction(data):

    topTotal=0
    classTopper=''
    for student,total in data.items():
        if total>topTotal:
            classTopper=student
            topTotal=total
    return classTopper

#Function for reading csv without using Pandas
def csvReaderFunction(csvFileName):

    with open(csvFileName,'r') as studentsCsvFile:
        reader=csv.reader(studentsCsvFile,delimiter=',')
        allData=[]
        headerData={}
        marksData={}
        header=next(reader)
        for item in header:
            name=header[0]
            subjects=header[1:]
            headerData[name]=subjects
        allData.append(headerData)
        for item in reader:
            name=item[0]
            marks=item[1:]
            marksData[name]=marks
        allData.append(marksData)
    return allData

#Function for finding topper of each subject
def findSubjectTopperFunction(studentMarks,subjectIndex):

    subjectTopMark=0
    subjectTopper=''
    for studentName,marks in studentMarks.items():
        if subjectTopMark==int(marks[subjectIndex]):
            subjectTopper=subjectTopper+' & '+studentName
        if subjectTopMark<int(marks[subjectIndex]):
            subjectTopMark=int(marks[subjectIndex])
            subjectTopper=studentName
    return subjectTopper

#Function for finding toppers of class
def findClassTopperFunction(studentMarks):

    studentsTotal={}
    for studentName,marks in studentMarks.items():
        studentTotal=0
        for mark in marks:
            studentTotal+=int(mark)
        studentsTotal[studentName]=studentTotal
    classToppers=[]
    for rank in range(3):
        classTopper=findMaxTotalFunction(studentsTotal)
        classToppers.append(classTopper)
        studentsTotal[classTopper]=-1
    return classToppers

#Main function . calls all other functions
def mainFunction():

    allData=csvReaderFunction('Student_marks_list.csv')
    subjectNames=allData[0]
    studentMarks=allData[1]
    for name,subjects in subjectNames.items():
        for subject in subjects:
            subjectIndex=subjectNames[name].index(subject)
            subjectTopper=findSubjectTopperFunction(studentMarks,subjectIndex)
            if ' & ' not in subjectTopper:
                print('Topper in {} subject is {}'.format(subject,subjectTopper))
            else:
                print('Topper in {} subject are {}'.format(subject,subjectTopper))
    classToppers=findClassTopperFunction(studentMarks)
    print('Toppers in the class are {}, {} & {}'.format(classToppers[0],classToppers[1],classToppers[2]))


print('Starting mainFunction...')

#Calling mainFunction()
mainFunction()

print('Ending mainFunction...')

#Time Complexity:O(n^2)
#Space Complexity:O(n)