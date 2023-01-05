# Irene Stone
# Nov 2022
# demonstrate dictionary 'pop' method and use of 'in'

grades = {
    "Irish" : "H3",
    "English" : "O3",
    "Maths" : "H4",             
    "Computer Science" : "H1",
}

subject = input ("Enter subject name: ")
if subject in grades:
    result = grades.pop(subject)
    print("Result for %s was %s" %(subject, result))
else:
    print("Result for %s does not exist. %s not found" %(subject, subject))
    
print(grades)