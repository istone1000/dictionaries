
from pyowm.owm import OWM  

myOwm = OWM("538b1c74d1e054fc8a69e6b230e175af") 

mgr = myOwm.weather_manager() 
     
places_temp = {}      

towns = ["Waterford, IE", "Galway, IE","Donegal, IE", "Sligo, IE", "Limerick, IE", "Cork, IE", "Bangkok, TH"]

for item in towns:
    observation = mgr.weather_at_place(item).weather
    temp_dictionary = observation.temperature("celsius")
    places_temp[item] = temp_dictionary["temp"] 

print("Dictionary with places:temperature keys: ",places_temp)  

 
   
    

