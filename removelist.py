thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #remove "banana" from the list
print(thislist)

thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana") #remove first "banana" from the list and keep the rest of the list
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(1) #remove the second occurrence of the value
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(0) #remove the first occurrence of the value
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
thislist4.pop() #remove the last occurrence of the value
print(thislist4)

thislist5 = ["apple", "banana", "cherry"]
del thislist5[0] #remove the first occurrence of the value
print(thislist5)

thislist6 = ["apple", "banana", "cherry"]
del thislist6 #delete the entire list
# print(thislist6)

thislist7 = ["apple", "banana", "cherry"]
thislist7.clear() #clear the list
print(thislist7)