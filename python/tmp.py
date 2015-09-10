#!/usr/bin/env python
from random import *

print("Loop")

items = ["a", "b", "c"]
for item in items:
    print(item)

for i in range(1, 10):
    print(i)

s = "abc"
print(s + str(3))

i = 5
while i < 10:
    print(i)
    i = i + 1

print("random")
print(random())
print(randint(1, 100))
print(uniform(1, 10))
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items)
shuffle(items)
print(items)
x = sample(items, 1)
print(x)
y = sample(items, 2)
print(y)

def f(x):
    x = 2

    print(x)

f(3)


print("class")
class User:
    m_name = ""
    __number = 0

    def __init__(self, name):
        self.m_name = name

    def SayHello(self):
        print("My name is " + self.m_name + "and number is " + str(self.__number))

    def SetNumber(self, number):
        self.__number = number

james = User("james")
david = User("david")
james.SayHello()
david.SayHello()
james.__number = 3
james.SetNumber(4)
james.SayHello()

#ok
