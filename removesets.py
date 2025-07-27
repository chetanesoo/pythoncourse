thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #removes the element "banana" from the thisset set
print(thisset)

thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana") #removes the element "banana" from the thisset set
print(thisset1)

thisset2 = {"apple", "banana", "cherry"}
thisset2.pop() #removes a random element from the thisset set
print(thisset2)

thisset3 = {"apple", "banana", "cherry"}
thisset3.clear() #clears the set
print(thisset3)

thisset4 = {"apple", "banana", "cherry"}
del thisset4 #deletes the set

thisset5 = {"apple", "banana", "cherry"}
x = thisset5.pop() #removes a random element from the thisset set
print(x) #prints the removed element
print(thisset5) #prints the set after the element is removed