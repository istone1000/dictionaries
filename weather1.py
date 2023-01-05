#Irene Stone
#14th Nov 2022
#Using dictionaries with open weather map API

from pyowm.owm import OWM  #import the Open Weather map python library

myOwm = OWM("538b1c74d1e054fc8a69e6b230e175af") #using your API keys to tell OWM who you are

mgr = myOwm.weather_manager() #command to access the weather using your API

observation = mgr.weather_at_place("Tallaght, IE").weather #accessing the weather at a given location
#.weather is a ??? required for the command to run

#we will now get the wind information for our location
wind_dictionary = observation.wind()
temp_dictionary = observation.temperature("celsius")
pressure_dictionary = observation.barometric_pressure()
rain_dictionary = observation.rain

print(wind_dictionary)
print(wind_dictionary["speed"])
print(temp_dictionary)
print(pressure_dictionary)
print(rain_dictionary)





