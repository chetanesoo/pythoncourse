thistuple = ("apple", "banana", "cherry")
for x in thistuple: #loop through the tuple and print each item
    print(x) #print the item

thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)): #loop through the tuple and print each item
    print(thistuple1[i]) #print the item at the current index

thistuple2 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple2):
    print(thistuple2[i]) #loop through the tuple and print each item
    i += 1 #increment the index

thistuple3 = ("apple", "banana", "cherry")
[print(x) for x in thistuple3] #loop through the tuple and print each item