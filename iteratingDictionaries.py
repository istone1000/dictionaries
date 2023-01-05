# Purpose: A program to demonstrate how to iterate over dictionaries

#A dictionary to store results for multiple students
results = dict({
    'Joe': 67,
    'Mary' : 76,
    'Alex' : 72,
    'Sarah' : 82,
    'Fred': 64,
    'Pat' : 91,
})

print(results)

# Display the keys
print("Display the keys")
for k in results.keys():
    print("Name: %s" %k)
print("-----------")

# A simpler way to display the keys
print("A simpler way to display the keys")
for k in results:
    print("Name: %s" %k)
print("-----------")

# Display the keys - sorted
print("Display the keys - sorted")
for k in sorted(results):
    print("Name: %s" %k)
print("-----------")

# Display the values
print("Display the values")
for v in results.values():
    print("Value: %s" %v)
print("-----------")   

print(results)
print(results.keys())
print(results.values())
print(results.items())

print("-----------")
# Display the items of the dictionary as Python stores them
for k,v in results.items():
    print("Name: %s Result: %d" %(k,v))

print("-----------")
# Display the items of the dictionary in a sorted order
for k,v in sorted(results.items()):
    print("Name: %s Result: %d" %(k,v))

print("-----------")
# A more advanced sort - this time by values
import operator
for k, v in sorted(results.items(), key=operator.itemgetter(1)):
    print("Name: %s Result: %d" %(k,v))

