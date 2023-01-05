# Purpose: A program to demonstrate how to build a dictionary

# Version 2a. A dictionary to store multiple results for a student
results = {}
# 
# name = input("Enter student name: ")
# results['name'] = name
# while True:
#     subject = input ("Enter subject name: (press enter to end) ")
#     if subject == "":
#         break
#     mark = input ("Enter percentage mark for "+subject+": ")
#     results[subject] = mark
# 
# print(results)

# other version with while loop
name = input("Enter student name: ")
results['name'] = name
subject = input ("Enter subject name: ")
while subject != "":
    mark = input ("Enter percentage mark for "+subject+": ")
    results[subject] = mark
    subject = input ("Enter subject name: ")
print(results)

#for loop
# name = input("Enter student name: ")
# noOfSubjects = int(input("Enter the number of subjects you want to enter: "))
# results['name'] = name
# for i in range(noOfSubjects):
#     subject = input ("Enter subject name: ")
#     mark = input ("Enter percentage mark for "+subject+": ")
#     results[subject] = mark
# 
# print(results)