# code recipes here: https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html#onecall
# https://pyowm.readthedocs.io/_/downloads/en/develop/pdf/

from pyowm.owm import OWM  #importing the open weather map python library
import matplotlib.pyplot as plt  #import the matplotlib library for plotting 

myOwm = OWM('538b1c74d1e054fc8a69e6b230e175af')  #using your API key to tell OWM who you are

mgr = myOwm.weather_manager()   # command to access the weather using your API


#Task
# given the 9 locations below, find the optimal location in which
# to build a new offshore wind farm. Use data from the OWM API to 
# determine this location 
locations = ['Killybegs, IE', 'Belmullet, IE', 'Clifden, IE', 'Doolin, IE', 'Kilkee, IE', 'Ventry, IE','Portmagee, IE','Bantry, IE','Baltimore, IE']
#

#use OWM to find the optimal site for a new windfarm.
windiness = {}  #an empty dictionary to store key:value pairs (town:windiness pairs)
#list_places = []     #creates an empty list to store the windiness values from the places_temp (optional- for graphing later)

for item in locations:    # iterating through each element in the locations list
    observation = mgr.weather_at_place(item).weather   #for each town the weather information will be obtained
    wind_dictionary = observation.wind()  #the wind information is obtained for each town - this is a dictionary
#    print(wind_dictionary)
#    print(type(wind_dictionary))
    windiness[item] = {}   #key becomes item (the location), value is another empty dictionary
#    print(windiness)    #printing this in each iteration will show above
    windiness[item]['speed'] = wind_dictionary['speed'] 
    windiness[item]['gust'] = wind_dictionary['gust']
    print(item)
print(windiness)

maxwind = 0
maxgust = 0

#lists created for analysis
windlist = []
gustlist = []

for item in windiness:
    windlist.append(windiness[item]['speed'])
    gustlist.append(windiness[item]['gust'])

print(windlist)
print(gustlist)

maxwind = max(windlist)
maxgust = max(gustlist)

gustplace = "0"
windplace = "0"
print(maxwind,maxgust)

for item in windiness:
    if windiness[item]['speed'] == maxwind:
        windplace = item
    if windiness[item]['gust'] == maxgust:
        gustplace = item
        
print(windplace,"is the windiest location. "+str(maxwind)+"m/s")
print(gustplace,"is the gustiest location. "+str(maxgust)+"m/s")

#creates a bar chart of windiness
plt.bar(locations,windlist)
plt.xlabel('towns')
plt.ylabel('windiness m/s')
plt.title('Windiness')
plt.show(block=False)            #Set block=False so you don't need to exit out of the graph window to continue programme


#creates a bar chart of gustiness
#plt.bar(locations,gustlist)
#plt.xlabel('towns')
#plt.ylabel('gustiness m/s')
#plt.title('Gustiness')
#plt.show(block=False)            #Set block=False so you don't need to exit out of the graph window to continue programme

