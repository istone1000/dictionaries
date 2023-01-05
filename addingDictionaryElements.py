#Irene Stone
#Nov 2022
#A program to demonstrate how to add an element to a dictionary

d = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

# add a new element
print(d)
d['WYD'] = "What are you doing"
print(d)

#adding new elements
d["MUA"] = "Make Up Artist"
d["SWAG"] = "Stuff We All Get"
d["WTP"] = "What's the plan"
print(d)

#adding new value to a dictionary using a key that already exists
d["OMG"] = "new"
print(d)