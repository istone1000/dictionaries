#Irene Stone
#15th Nov 2022
#Using dictionaries with open weather map API

from pyowm.owm import OWM  #import the Open Weather map python library
import matplotlib.pyplot as plt  #import the matplotlib library for plotting 

myOwm = OWM("538b1c74d1e054fc8a69e6b230e175af") #using your API keys to tell OWM who you are

mgr = myOwm.weather_manager() #command to access the weather using your API

#collecting data from different towns and comparing their temperatures
places_temp = {}     #an empty dictioanry to store key:value pairs (town:temperature pairs)
list_temp = []       #creates an empty list to store the temperature values from the places_temp (optional- for graphing later)
towns = ["Waterford, IE", "Galway, IE","Donegal, IE", "Sligo, IE", "Limerick, IE", "Cork, IE", "Paris,FR", "Rome, IT", "Sydney, AU", "Bangkok, TH"]

#this code will populate the places_temp dictionary as follows:
#keys will be the towns from towns list; values will be the temperatures obtained from API
for item in towns:                #iterating through each element in the towns list
    observation = mgr.weather_at_place(item).weather   #for each town the weather information will be obtained
    temp_dictionary = observation.temperature("celsius")  #the temperature information is obtained for each town - this is a dictionary
    places_temp[item] = temp_dictionary["temp"]   #the value associated with the key "temp" is stored in the places_temp dictionary with key = town
    list_temp.append(temp_dictionary["temp"])   #stores the temperature values in a list (optional for graphing)
    
print("Dictionary with places:temperature keys: ",places_temp)   #prints the populated places_temp dictionary
print("List with temperatures only: ",list_temp)     #prints the list_temp list - temperatures only

#creates a bar chart of all temperatures
plt.bar(towns,list_temp)
plt.xlabel('towns')
plt.ylabel('degC')
plt.title('Temperatures')
plt.show()               #you need to exit out of the graph window to continue programme



#Another way to store the temperatures in a list:
# Need to stores the temperature values in a list
#list_temp = []       #creates an empty list to store the temperature values from the places_temp
# print("Display the values")
# for v in places_temp.values():
#     print("Value: %s" %v)
#     list_temp.append(v)
# print(list_temp)
# print("-----------")   



