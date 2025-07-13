age = 36
txt = f"My name is John, I am {age}" #This is a formatted string, it inserts the value of the variable age into the string
print(txt)

price = 59
txt1 = f"The price is {price} dollars" #This is a formatted string, it inserts the value of the variable price into the string
print(txt1)

price1 = 59
txt2 = f"The price is {price1:.2f} dollars" #This is a formatted string, it inserts the value of the variable price into the string with 2 decimal places
print(txt2)

txt3 = f"The price is {20 * 59} dollars" 
print(txt3)
""" This is a formatted string, it inserts the value of 
the variable price into the string with 2 decimal places 
while performing the multiplication """