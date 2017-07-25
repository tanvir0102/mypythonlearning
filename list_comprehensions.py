#!/usr/bin/env python3

l = []
for letter in 'word':
	l.append(letter)
print(l)

##List comprehensions

lst = [letter for letter in 'word']

print(lst)

lst = [x**2 for x in range(1,11)]

print(lst)

lst = [number for number in range(11) if number % 2 == 0]
print(lst)

lst = []
for number in range(11):
	if number % 2 == 0:
		lst.append(number)

print(lst)

celsius = [0, 10, 20.1, 34.5]
farh = [temp * (9/5.0) + 32 for temp in celsius]
print(farh)



