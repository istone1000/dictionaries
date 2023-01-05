#Irene Stone
#Nov 2022
#p258 exercise
#dictionary stores the results of one subject for multiple students

results = { } 										#empty dictionary
subject = input("Enter subject: ")					#asks user to enter subject
results['subject'] = subject						#creates a new key called 'subject'; value will be user input
name = input ("Enter student name: ")
while name != "":
    mark = input ("Enter percentage mark for "+subject+": ")
    results[name] = mark
    name = input ("Enter student name: ")
print(results)
