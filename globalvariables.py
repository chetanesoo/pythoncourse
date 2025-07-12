x = "awesome"

def myfunc():
    print("Python is " + x) # This function prints a message using the global variable x

myfunc()  # Call the function to see the output



def myfunc2():
    x = "fantastic"  # This creates a local variable x
    print("Python is " + x)  # This will print the local variable x

myfunc2()  # Call the second function to see the output
# The first function uses the global variable x, while the second function uses a local variable x

print("Python is " + x)  # This will print the global variable x
# The output will show the difference between the global and local variable usage



def myfunc3():
    global x  # This allows us to modify the global variable x
    x = "incredible"  # Change the global variable x

myfunc3()  # Call the function to modify the global variable

print("Python is " + x)  # This will now print the modified global variable x

print(x)  # This will print the current value of the global variable x