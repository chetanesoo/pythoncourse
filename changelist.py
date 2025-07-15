thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # This will replace the second item with "blackcurrant"
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"] # This will replace the second and third item with "blackcurrant" and "watermelon"
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["blackcurrant", "watermelon"] # This will replace the second item with "blackcurrant"
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"] # This will replace the second and third item with "watermelon"
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
thislist4.insert(2, "watermelon") # This will insert "watermelon" at the third position
print(thislist4)