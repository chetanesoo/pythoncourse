thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # This will add "orange" to the end of the list
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(1, "orange") # This will add "orange" at the second position
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical) # This will add the items of the tropical list to the end of the thislist2 list
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist3.extend(thistuple) # This will add the items of the thistuple list to the end of the thislist3 list
print(thislist3)