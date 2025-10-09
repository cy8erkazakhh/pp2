import json
import math
from datetime import date, timedelta, datetime


def square_number(N: int):
    ans = []
    for i in range(N + 1):
        yield i ** 2

n = int(input("N = "))
for square in square_number(n):
    print(square, end=" ")

def even_numbers(n: int):
    ans = []
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input("N = "))
print(",".join(str(x) for x in even_numbers(n)))

def divisible_by_3_4(n : int):
    ans = []
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("N = "))
for num in divisible_by_3_4(n):
    print(num, end=" ")

def squares(a, b: int):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("a = "))
b = int(input("b = "))
for square in squares(a, b):
    print(square, end=" ")

def countdown(n: int):
    while n >= 0:
        yield n
        n-=1

n = int(input("n = "))
for i in countdown(n):
    print(i, end=" ")


current = date.today()

new_date = current - timedelta(days=5)
print(new_date)

print("Yesterday:", date.today() - timedelta(days=1))
print("Today:", date.today())
print("Tomorrow:", date.today() + timedelta(days=1))

now = datetime.now()
now = now.replace(microsecond=0)
print(now)

def diff_in_sec(a, b: date):
    return (a - b).total_seconds()

print(diff_in_sec(date.today(), date.today() - timedelta(days=1)))

degree = float(input("degree = "))
radian = degree * (math.pi / 180.0)
print(radian)

height = float(input("height = "))
base1 = float(input("base1 = "))
base2 = float(input("base2 = "))
area = ((base1 + base2) / 2) * height

print(area)

n = int(input("n = "))
s = float(input("s = "))

area = (n * s ** 2) / (4 * math.tan(math.pi/n))

print(area)

a = float(input("a = "))
b = float(input("b = "))
area = a * b
print(area)

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50, "-" * 20, " ------  ------")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("description", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")