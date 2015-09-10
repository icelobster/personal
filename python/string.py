#!/usr/bin/env python

s = "Hello World!"
print(s)
print(s[0])
print(s[0:2])
print(s[2:])
print(s + "abc" + s)
print(s.replace("Hello", "Thank"))

sentence = "The cat is mine"
q = "cat"

if q == sentence:
    print("equal")
else:
    print("not equal")

if q in sentence:
    print("q is in sentence")
