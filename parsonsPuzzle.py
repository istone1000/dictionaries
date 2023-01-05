#Irene Stone
#Dec 2022
#Obtaining Temperature Data from OWM API

from pyowm.owm import OWM  #import the Open Weather map python library

myOwm = OWM("538b1c74d1e054fc8a69e6b230e175af") #using your API keys to tell OWM who you are

mgr = myOwm.weather_manager() #command to access the weather using your API

places_temp = {}      #an empty dictionary to store key:value pairs (town:temperature pairs)

towns = ["Waterford, IE", "Galway, IE","Donegal, IE", "Sligo, IE", "Limerick, IE", "Cork, IE", "Bangkok, TH"]

for item in towns:   #iterating through each item in towns list
    observation = mgr.weather_at_place(item).weather    #for each town the weather information will be obtaine
    temp_dictionary = observation.temperature("celsius")  #the temperature information is obtained for each town - this is a dictionary
    places_temp[item] = temp_dictionary["temp"] #the value associated with the key "temp" is stored in the places_temp dictionary with key = town

print("Dictionary with places:temperature keys: ",places_temp)   #prints the populated places_temp dictionary   
    

