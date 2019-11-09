from getClass import getClass
teacherList = {}

#using class.txt as example of class list, could be a user interface later.
with open("class.txt", "r") as inputFile:
    allClass = inputFile.read().split("\n")


#Using the className, get information and add to teacherList
for Aclass in allClass:
    teacherList.update(getClass(Aclass))


for course in teacherList:
    teacher, time = teacherList[course]
    print("Section:", course)
    print("Teacher:", teacher)
    print("Time:", time)
    print()
