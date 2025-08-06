thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict) #print the whole dictionary
print(thisdict["brand"]) #print the value of the key "brand"
print(len(thisdict)) #print the length of the dictionary
print(type(thisdict)) #print the type of the dictionary

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict1) #print the whole dictionary and the value of the key "year" is 2020 because it is the last one


thisdict2 = dict(name = "John", age = 36, country = "Norway") #dict is a constructor for creating a dictionary
print(thisdict2) #print the whole dictionary