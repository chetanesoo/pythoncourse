thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #copy the list using copy() method
print(mylist)

thislist1 = ["apple", "banana", "cherry"]
mylist1 = list(thislist1) #copy the list using list() constructor
print(mylist1)

thislist2 = ["apple", "banana", "cherry"]
mylist2 = thislist2[:] #copy the list using slice operator
print(mylist2)

thislist3 = ["apple", "banana", "cherry"]
mylist3 = thislist3[:2] #copy the list using slice operator, only copy the first 2 items
print(mylist3)

thislist4 = ["apple", "banana", "cherry"]
mylist4 = thislist4[1:] #copy the list using slice operator, only copy the second and third items
print(mylist4)

thislist5 = ["apple", "banana", "cherry"]
mylist5 = thislist5[-1:] #copy the list using slice operator, only copy the last item
print(mylist5)

thislist6 = ["apple", "banana", "cherry"]
mylist6 = thislist6[-3:-1] #copy the list using slice operator, only copy the last 2 items
print(mylist6)