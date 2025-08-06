thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #change the value of the key "year" from 1964 to 2018
print(thisdict) #print the whole dictionary

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.update({"year": 2020}) #update the value of the key "year" from 1964 to 2020
print(thisdict1) #print the whole dictionary