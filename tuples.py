mytuple = ("apple", "banana", "cherry") #create a tuple
print(mytuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") #Tuple allows duplicate values
print(thistuple)

thetuple = ("apple", "banana", "cherry")
print(len(thetuple)) #print the length of the tuple

#create a tuple with one item
thistuple1 = ("apple",)
print(type(thistuple1)) #print the type of the tuple, an one item tuple needs a comma

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2)) #print the type of the tuple, this is a string

thistuple3 = ("abc", 34, True, 40, "male") #Tuple can contain different data types
print(thistuple3) 

#Tuple constructor
thistuple4 = tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple4)