#!/usr/bin/env python3

f = open('test.txt')
print(f.read())
print(f.read())
f.seek(0)
print(f.read())
print(f.readlines())

for line in open('test.txt'):
	print(line)

