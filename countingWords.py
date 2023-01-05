#Irene Stone
#Nov 2022
#Counting the number of words in a sentence
#iterating over a list of words 

def histWords(s):
    wl = s.split(" ")  #makes a list of words from sentence
    d = {} 
    for w in wl:      #iteration is over a list of words
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return d

wordsString = 'she sells sea shells by the sea shore the shells she sells are sea shore shells to be sure'
wordsList = wordsString.split(" ")
print("-----------------------")
print (wordsString)
print(type(wordsString))
print("-----------------------")
print(wordsList)
print(type(wordsList))
print("-----------------------")
dict=histWords(wordsString)
print(dict)
