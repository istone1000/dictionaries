#Irene Stone
#Nov 2022
#Using a dictionary to count letters in a sentence
#iterating over a string of characters

def histogram(s):
    d = {}         #also a way to set up an empty dictionary
#    d = dict()        #initialise the dictionary 
    for w in s:       #iteration is over characters in a string
        if w not in d:
            d[w] = 1 #if it's the first time to see the letter then the dic is updated. c is not a number or index
        else:
            d[w] += 1 #if it sees the letter again it increments
    return d
h = histogram('How many letters are in this sentence?')
print(h)