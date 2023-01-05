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
d1.clear()
del d2['LOL']

print(d1)
print(d2)