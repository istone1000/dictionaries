#Irene Stone
#Nov 2022
#use of get and pop

grades = {
    "Irish" : "H3",
    "English" : "O3",
    "Maths" : "H4",             
    "Computer Science" : "H1",
}

# subject = input ("Enter subject name: ")
# result = grades.get(subject)
# print("Result for %s was %s" %(subject, result))
# print(grades)

subject = input ("Enter subject name: ")
result = grades.pop(subject)
print("Result for %s was %s" %(subject, result))
print(grades)