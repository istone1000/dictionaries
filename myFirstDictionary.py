#Irene Stone
#Nov 2022
#Dictionary

capitals = {
    "Ireland" : "Dublin",
    "Scotland" : "Edinburgh",
    "England" : "London",             
    "Wales" : "Cardiff",
    "France" : "Paris",
    "Italy" : "Rome"
}

# Display the dictionary
print(capitals)

country = input("Enter one of the six nations : ")
print("The capital of "+country+" is "+capitals[country])
print("*******************************")

numbers = {
    1 : "aon",
    2 : "dó",
    3 : "trí",             
    4 : "ceathair",
    5 : "cúig",
    6 : "sé",
    7 : "seacht",
    8 : "ocht",
    9 : "naoi",
    10: "deich"
}
print(numbers)
for i in range(1, 11):
    print(numbers[i])