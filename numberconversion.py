x = 1 # int
y = 2.8 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(type(x))
print(type(y))
print(type(z))

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1,10))