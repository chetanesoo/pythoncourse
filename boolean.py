print(10 > 9) #This is a boolean, it prints True
print(10 == 9) #This is a boolean, it prints False
print(10 < 9) #This is a boolean, it prints False

a = 200
b = 33

if b > a:
    print("b is greater than a") #This is a boolean, it prints False
else:
    print("b is not greater than a") #This is a boolean, it prints False

x = "Hello"
y = 15

print(bool(x)) #This is a boolean, it prints True
print(bool(y)) #This is a boolean, it prints True

class myclass(): #This is a class
    def __len__(self): 
        return 0 #This is a method, it returns 0, if change to 1 it will print True

myobj = myclass()
print(bool(myobj)) #This is a boolean, it prints False

def myFunction():
    return True

print(myFunction()) #This is a boolean, it prints True

def myFunction1():
    return True #This is a function, it returns True, if change to False it will print NO!

if myFunction1():
    print("YES!") #This is a boolean, it prints YES!
else:
    print("NO!") #This is a boolean, it prints NO!
    
z = 200
print(isinstance(z, int)) #This is a boolean, it prints True