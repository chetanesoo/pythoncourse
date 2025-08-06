thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] #access the value of the key "model"
print(x) #print the value of the key "model"

y = thisdict.get("model") #access the value of the key "model" using the get() method
print(y)

z = thisdict.keys() #access the keys of the dictionary
print(z) #print the keys of the dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

a = car.keys()
print(a) #before the change

car["color"] = "white" #add a new key-value pair
print(a) #after the change

b = car.values() #access the values of the dictionary
print(b) #before the change

car["year"] = 2020 #overwrite the value of the key "year" from 1964 to 2020
print(b) #after the change

c = car.items() #access the items of the dictionary
print(c) #before the change

car["year"] = 2020 #overwrite the value of the key "year" from 1964 to 2020
print(c) #after the change

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict1: #check if the key "model" is in the dictionary
  print("Yes, 'model' is one of the keys in the thisdict1 dictionary") #print the message if the key "model" is in the dictionary