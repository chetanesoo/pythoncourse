fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x) #append the item to the new list if it contains "a"

print(newlist)

fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits1 if "a" in x] #append the item to the new list if it contains "a"
print(newlist1)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits2 if x != "apple"] #append the item to the new list if it is not "apple"
print(newlist2)

newlist3 = [x for x in fruits if x != "apple"] #append the item to the new list if it is not "apple"
print(newlist3)

newlist4 = [x for x in fruits if x == "apple"] #append the item to the new list if it is "apple"
print(newlist4)

newlist5 = [x for x in fruits if x == "apple" or x == "banana"] #append the item to the new list if it is "apple" or "banana"
print(newlist5)

thislist6 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist6 = [x.upper() for x in thislist6] #convert the item to uppercase
print(newlist6)

thislist7 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist7 = [x.lower() for x in thislist7] #convert the item to lowercase
print(newlist7)

thislist8 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist8 = [x.upper() for x in thislist8 if x != "apple"] #convert the item to uppercase if it is not "apple"
print(newlist8)

thislist9 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist9 = [x if x != "apple" else "orange" for x in thislist9] #replace "apple" with "orange"
print(newlist9)