list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #join the two lists
print(list3)

list4 = ["a", "b", "c"]
list5 = [1, 2, 3]

for x in list5:
    list4.append(x) #append the items of list5 to list4

print(list4)

list6 = ["a", "b", "c"]
list7 = [1, 2, 3]

list6.extend(list7) #extend the list with the items of list7
print(list6)