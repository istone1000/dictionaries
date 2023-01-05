# Version 1. A dictionary to store a student's result
results = {}

name = input("Enter student name: ")
results['name'] = name
subject = input ("Enter subject name: ")
mark = input ("Enter percentage mark for "+subject+": ")
results[subject] = mark  #the name of the subject inputte by user becomes key for dictionary entry
print(results)