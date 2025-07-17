# set is a collection of unique elements, it is unordered and unindexed and does not allow duplicates
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset1 = {"apple", "banana", "cherry", "apple"} # duplicate elements are not allowed, "apple" will be printed only once
print(thisset1)

thisset2 = {"apple", "banana", "cherry", True, 1, 2} # True and 1 are considered the same, so only one of them will be printed
print(thisset2)

thisset3 = {"apple", "banana", "cherry", False, True,0} # False and 0 are considered the same, so only one of them will be printed
print(thisset3)

thisset4 = {"apple", "banana", "cherry"}
print(len(thisset4)) #Prints the number of elements in the set

thisset5 = {"apple", "banana", "cherry", 34, True, 40, "male"} #Set can contain different data types
print(type(thisset5)) #Prints the type of the set

thisset6 = set(("apple", "banana", "cherry")) #Set can be created using the set() constructor
print(thisset6)