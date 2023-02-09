'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json

# open json file
with open('eq_data.json') as f:
   dict = json.load(f)

   
# number of earthquakes
num_quakes = dict["metadata"]["count"]
print()
print('The number of earthquakes is: ', num_quakes)
print()

# earth quakes > 6.0 
list_eq = dict["features"]

for dict in list_eq:
   location = dict["properties"]["place"]
   mag = dict["properties"]["mag"]
   longitude = dict["geometry"]["coordinates"][0]
   latitude = dict["geometry"]["coordinates"][1]


   if mag > 6:
      eq_dict =  {'place': location,
               'magnitude': mag, 
               'longitude': longitude, 
               'latitude': latitude}
      print(eq_dict)
      
      
 

#first 3 earthquakes
      first_three = ['Northern Mid-Atlantic Ridge', '166km SSE of Muara Siberut, Indonesia', '14km ENE of Puerto Madero, Mexico']
      if eq_dict['place'] in first_three:
         print()
         print('Location:', eq_dict['place'])
         print('Magnitude:', eq_dict['magnitude'])
         print('Longitude:', eq_dict['longitude'])
         print('Latitude:', eq_dict['latitude'])
         print()
