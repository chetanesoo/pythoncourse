thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #sort the list in ascending order
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist2.sort(reverse=True) #sort the list in descending order
print(thislist2)

thislist3 = [100, 50, 65, 82, 23]
thislist3.sort(reverse=True) #sort the list in descending order
print(thislist3)

def myfunc(n): #define a function to sort the list based on the absolute difference from 50
    return abs(n - 50) #sort the list based on the absolute difference from 50, abs ensures the difference is positive

thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(key=myfunc)
print(thislist4)

thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.sort() #sort the list in ascending order starting with uppercase letters
print(thislist5)

thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort(key=str.lower) #sort the list in ascending order starting with lowercase letters
print(thislist6)

thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.reverse() #reverse the list, sort by starting from the last index
print(thislist7)