print("Hello")
print('Hello')
# Both are same just different quotes

a = "Hello"
print(a)

print("It's alright") # This is a single quote inside a double quote string
print("He is called 'Johnny'") # This is a double quote inside a single quote string
print('He is called "Johnny"') # This is a single quote inside a single quote string

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b) #This is a multi-line string with double quotes

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c) #This is a multi-line string with single quotes

d = "Hello, World!"
print(d[1]) #This is a string slicing, it prints the character at index 1

for x in "banana":
    print(x) #This is a for loop, it prints each character in the string "banana"
    
e = "Hello, World!"
print(len(e)) #This is a function, it prints the length of the string

txt = "The best things in life are free!"
print("free" in txt) #This is a boolean operator, it prints True if "free" is in the string, otherwise it prints False

txt1 = "The best things in life are free!"
if "free" in txt1:
    print("Yes, 'free' is present.")

txt2 = "The best things in life are free!"
if "expensive" not in txt2:
    print("No, 'expensive' is NOT present.")