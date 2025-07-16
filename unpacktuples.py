fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits #unpack the tuple into variables
print(green)
print(yellow)
print(red)

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1 #unpack the tuple into variables, the asterisk is used to collect the remaining values into a list
print(green)
print(yellow)
print(red)

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruits2 #unpack the tuple into variables, the asterisk is used to collect the remaining values into a list
print(green)
print(tropic)
print(red)