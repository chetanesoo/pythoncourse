thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #access the second item in the tuple

thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[-1]) #access the last item in the tuple

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5]) #access the items from the third to the fifth item

thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[:4]) #access the items from the start to the fourth item

thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[2:]) #access the items from the third item to the end

thistuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple5[-4:-1]) #access the items from the fourth last item to the second last item

thistuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple6[-4:]) #access the items from the fourth last item to the end

thistuple7 = ("apple", "banana", "cherry")
if "apple" in thistuple7: #check if "apple" is in the tuple
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("No, 'apple' is not in the fruits tuple")

thistuple8 = ("apple", "banana", "cherry")
if "pineapple" not in thistuple8: #check if "pineapple" is not in the tuple
    print("No, 'pineapple' is not in the fruits tuple")