# Purpose: A program to demonstrate how to delete a dictionary element

d = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

print(d)
del d['LOL']
print(d)
#del d          #deletes the dictionary completly
#print(d)       #error as d not defined

d.clear()
print(d)