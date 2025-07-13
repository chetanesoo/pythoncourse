#Note: The first character has index 0

b = "Hello, World!" 
print(b[2:5]) #This is a string slicing, it prints the characters from index 2 to 5 (not including 5)

c = "Hello, World!"
print(c[:5]) #This is a string slicing, it prints the characters from index 0 to 5 (not including 5)

d = "Hello, World!"
print(d[2:]) #This is a string slicing, it prints the characters from index 2 to the end of the string

e = "Hello, World!"
print(e[-5:-2]) #This is a string slicing, it prints the characters from index -5 to -2 (not including -2)

#Note: the last character has index -1