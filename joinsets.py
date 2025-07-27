set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #joins the two sets
print(set3)

set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set6 = set4 | set5 #joins the two sets
print(set6)

set7 = {"a", "b", "c"}
set8 = {1, 2, 3}
set9 = {"John", "Elena"}
set10 = {"apple", "banana", "cherry"}
set11 = set7.union(set8, set9, set10) #joins the three sets with set7 as the first set
print(set11)

set12 = {"a", "b", "c"}
set13 = {1, 2, 3}
set14 = {"John", "Elena"}
set15 = {"apple", "banana", "cherry"}
set16 = set12 | set13 | set14 | set15 #joins the four sets
print(set16)

#Join a Set and a Tuple
x = {"apple", "banana", "cherry"}
y = (1, 2, 3)
z = x.union(y) #joins the set and the tuple
print(z)

set17 = {"apple", "banana", "cherry"}
set18 = {1, 2, 3}
set17.update(set18) #joins the two sets
print(set17)

set19 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"}
set21 = set19.intersection(set20) #The intersection joins the two sets and return a new set with duplicate values from the sets joined
print(set21)

set22 = {"apple", "banana", "cherry"}
set23 = {"google", "microsoft", "apple"}
set24 = set22 & set23 #The intersection joins the two sets and return a new set with duplicate values from the sets joined
print(set24)

set25 = {"apple", "banana", "cherry"}
set26 = {"google", "microsoft", "apple"}
set25.intersection_update(set26) #TThe intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
print(set25)

set27 = {"apple", 1,  "banana", 0, "cherry"}
set28 = {False, "google", 1, "apple", 2, True}
set29 = set27.intersection(set28) #The values True and 1 are considered the same value. The same goes for False and 0
print(set29)

set30 = {"apple", "banana", "cherry"}
set31 = {"google", "microsoft", "apple"}
set32 = set30.difference(set31) #The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
print(set32)

set33 = {"apple", "banana", "cherry"}
set34 = {"google", "microsoft", "apple"}
set35 = set33 - set34 #The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
print(set35)

set36 = {"apple", "banana", "cherry"}
set37 = {"google", "microsoft", "apple"}
set36.difference_update(set37) #The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
print(set36)

set38 = {"apple", "banana", "cherry"}
set39 = {"google", "microsoft", "apple"}
set40 = set38.symmetric_difference(set39) #The symmetric_difference() method will return a new set that will contain only the items that are not present in both sets.
print(set40)

set41 = {"apple", "banana", "cherry"}
set42 = {"google", "microsoft", "apple"}
set43 = set41 ^ set42 #The symmetric_difference() method will return a new set that will contain only the items that are not present in both sets.
print(set43)

set44 = {"apple", "banana", "cherry"}
set45 = {"google", "microsoft", "apple"}
set44.symmetric_difference_update(set45) #The symmetric_difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
print(set44)