# a = 9
# if a % 2 == 0:
#     print("even")
# else:
#     print("Odd")

a = 10
b = 20
print('Hello world')


for i in range(1, 6):
    print(i)
    
# if else     
number = 5
if number >= 5:
    print('True')
else:
    print('False')
    
    
# for loop 
for i in range(5, 11):
    print(i, end = " ")
    print()
    
# Match case
day = 4
match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid day')
        

# Find the type like int or str or bool or float
num = 2.4
print(type(num))

# Adding two numbers
a = 3
b = 10
print(a + b)

# Subtracting two numbers
print(a - b)

# Multiple two numbers
print(a * b)

# Division two numbers use / operator this code output is like 3.333 float values
print(a / b)

# Division two numbers use // operator this code output is round number like 3
print(a // b)

# Modules two numbers use % operator 
print(a % b)

# Two numbers find power use **
print(a ** b) 


# Use 'and' operator
num1 = 10
num2 = 20

if num1 > 5 and num2 < 21:
    print('Both condition are true')
else:
    print('Both condition are false')
    
    
# Use 'or' operator
if num1 > 5 or num2 > 20:
    print('or operator true')
else:
    print('or operator false')
    
# Use 'not operator
if not(num1 < 5):
    print('not operator true')
else:
    print('not operator false')
    
    
# Use len()
s = 'Hello world'
print(len(s))

name = 'Karthikeyan'
print(len(name))

# Use upper()
print(s.upper())

print(name.upper())

# Use lower()
print(s.lower())

print(name.lower())

# Use replace()
print(s.replace("world", "Python"))

print(name.replace("Karthikeyan", "Gokulavasan"))

# Find the first character 
print(s[0])

# Find the last character
print(s[-1])

# Print 'Hello'
print(s[0:5]) # output is 'Hello'

# print 'Hello'
print(s[:6])

# print 'world'
print(s[6:])  # output is 'world'

# print reverse
print(s[::-1])


# string formatting
name = "Karthikeyan"
age = 18
print(f"My name is {name} and my age {age}")

# .format()
print("My name is {} and my age is {}.".format(name, age))


# for loop reverse print
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)
    
# Use join()
text = "Hello world!"
words = " ".join(text)  # output is 'H e l l o  w o r l d'
print(words)

letters = "H", "e", "l", "l", "o"
result = "".join(letters)
print(result)

text = "H e l l o"
result = text.replace(" ", "")
print(result)

result = "".join(text.split())
print(result)

# While loop 
count = 1
while count < 5:
    print("count is: " ,count)
    count += 1


print("Hello world")