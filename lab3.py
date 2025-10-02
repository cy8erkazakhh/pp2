import math
import random
import os
import json
from itertools import permutations

class Pyth:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Put your string: ")
    def printString(self):
        print(self.string)


class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have enough money!")

a = Account("", 100)
a.deposit(100)
a.withdraw(200)
a.withdraw(300)

def is_prime(a):
    if a < 2:
        return False
    return all(a % i != 0 for i in range(2, int(math.sqrt(a))+1))

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numb = list(filter(lambda x: is_prime(x), numb))
print(prime_numb)

def ounceToGrams(ounces):
    grams = ounces / 28.3495231
    return grams

def FahrenheitToCelcius(fahrenheit):
    celcius = (5/9) * (fahrenheit - 32)
    return celcius

def solve(numheads, numlegs):
    for pigs in range(1, numheads + 1):
        chickens = numheads - pigs
        if 2 * chickens + 4 * pigs == numlegs:
            print(f"chickens: {chickens}\npigs: {pigs}")

solve(35, 94)

def filter_prime(a):
    b = []
    for i in a:
        if is_prime(i):
            b.append(i)
    return b

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums = filter_prime(nums)
print(nums)

def print_permutations():
    s = input("Enter a string: ")
    perms = permutations(s)
    for p in perms:
        print("".join(p))

print_permutations()

def writefromtheend():
    s = input("Enter a string: ")
    new_s = ""
    for i in range(len(s) - 1, -1, -1):
        new_s += s[i]
    print(new_s)

writefromtheend()

def contains3(a):
    ch = False
    for i in a:
        if i == 3:
            if ch:
                return True
            else:
                ch = True
        else:
            ch = False
    return False
print(contains3([3, 3, 3]))
print(contains3([1, 3, 3]))
print(contains3([1, 2, 3]))
print(contains3([1, 2, 2]))

def spy_game(a):
    code = [0, 0, 7]
    for i in a:
        if i == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print()
print(spy_game([1, 2, 3, 0, 0, 7]))
print(spy_game([1, 0, 0, 7, 2, 3]))
print(spy_game([1, 0, 2, 0, 3, 7]))

def sphereVolume(radius):
    volume = 4/3 * math.pi * radius**3
    return volume

print(sphereVolume(2))
print(sphereVolume(3))
print(sphereVolume(4))

def uniquePos(a):
    unique = []
    used = set()
    for i in a:
        if i not in used:
            used.add(i)
            unique.append(i)
    return unique
print(uniquePos([1, 2, 3]))
print(uniquePos([3, 3, 3]))
print(uniquePos([2, 4, 5, 3, 4, 5, 6]))

def isPalindrome(a):
    return a == a[::-1]
print(isPalindrome("madam"))
print(isPalindrome("qq"))
print(isPalindrome("qqq"))
print(isPalindrome("runnur"))

def histogram(a):
    for i in a:
        for j in range(i):
            print("*", end="")
        print()

histogram([4, 9, 7])

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
hidden = random.randint(1, 20)
cnt = 0
while True:
    a = int(input())
    if a == hidden:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    elif a > hidden:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    cnt += 1

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def HighAvgImdb(a):
    if a["imdb"] >= 5.5:
        return True
    else:
        return False

def HighAvgImdbList(a):
    output = []
    for i in a:
        if i["imdb"] >= 5.5:
            output.append(i["name"])
    return output

print(HighAvgImdbList(movies))

def NameByCategory(a, cat):
    output = []
    for i in a:
        if i["category"] == cat:
            output.append(i["name"])
    return output
print(NameByCategory(movies, "Comedy"))

def AvgRating(a):
    avg = 0
    for i in a:
        avg += i["imdb"]
    avg /= len(a)
    return avg
print(AvgRating(movies))

def AvgRatingByCategory(a, cat):
    find = NameByCategory(a, cat)
    avg = 0
    for i in a:
        for j in find:
            if i["name"] == j:
                avg += i["imdb"]
    return avg / len(find)

print(AvgRatingByCategory(movies, "Comedy"))