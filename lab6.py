from functools import reduce
import time
import math
 
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([2, 3, 4, 5]))

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

count_case("Hello World!")

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam"))


def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

delayed_sqrt(25100, 2123)

def all_true(t):
    return all(t)

print(all_true((True, 1, 3)))
print(all_true((True, 0, 3)))