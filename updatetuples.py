x = ("apple", "banana", "cherry")
y = list(x) #convert the tuple to a list
y[1] = "kiwi" #update the second item in the tuple
x = tuple(y) #convert the list back to a tuple
print(x)

thistuple = ("apple", "banana", "cherry")
z = list(thistuple) #convert the tuple to a list
z.append("orange") #append "orange" to the tuple
thistuple = tuple(z) #convert the list back to a tuple
print(thistuple)

thistuple2 = ("apple", "banana", "cherry")
a = ("orange",) #create a tuple
thistuple2 += a #add the tuple to the original tuple
print(thistuple2)

thistuple3 = ("apple", "banana", "cherry")
b = list(thistuple3) #convert the tuple to a list
b.remove("apple") #remove "apple" from the tuple
thistuple3 = tuple(b) #convert the list back to a tuple
print(thistuple3)

thistuple4 = ("apple", "banana", "cherry")
c = list(thistuple4) #convert the tuple to a list
c.pop() #remove the last item in the tuple
thistuple4 = tuple(c) #convert the list back to a tuple
print(thistuple4)

thistuple5 = ("apple", "banana", "cherry")
del thistuple5 #delete the tuple