import random
import sys

#python HOME

print("Hello World!")

#python Get started

print(sys.version)

#python Syntax

if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello World!"

#This is a comment
print("Hello world!")

#python Comments

print("Hello world!")#This is a comment

#print("Hello world!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line

"""
This is a comment
written in
more than just one line
"""

#python variables
x = 5
y = 'John'
print(x)
print(y)

x = 4
x = 'Sally'
print(x)

x = str(3) # '3'
y = int(3) # 3
z = float(3) # 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

a = 4
A = 'Sally'
#a != A

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "python is amazing"
print(x)

x = "pytohn"
y = "is"
z = "amazing"
print(x, y, z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#python global variables
x = "awesome"
def my_func():
    print("python is " + x)
my_func()

x = "awesome"
def my_func2():
    x = 'fantastic'
    print("python is " + x)
my_func2()
print("python is " + x)

del x
def my_func3():
    global x
    x = "fantastic"

my_func3()
print("python is" + x)

#python numbers
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print(random.randrange(1, 10))

x = int(1)
y = int(2.8)
z = int("3")


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

x = str("s1")
y = str(2)
z = str(3.0)

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a)

a = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a)

b = "Hello, world!"
print(b[2:5])

b = "Hello, world!"
print(b[:5])

print(b[2:])

print(b[-5:-2])

a = "Hello, world!"
print(a.upper())

print(a.lower())

a = " Hello, World!"
print(a.strip())

print(a.replace("H","J"))

print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

age = 36
txt = f"My name is John and I'm {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"

txt = "We are so called \"Vikings\" from the North"


