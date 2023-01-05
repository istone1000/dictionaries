#Irene Stone
#Nov 2022
#Predict

d1 = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

d2 = {
     "LOL" : "League of Legends",
}

print(d1)
print(d2)
d1.update(IMHO = "In My Honest Opinion")  
d1.update(d2)
print(d1)