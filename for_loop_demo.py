#!/usr/bin/env	python3

l = [1,2,3,4,5]

for num in l:
	print(num)

for n in l:
	print('something!!')

for num in l:
	if num % 2 == 0:
		print(num)
	else:
		print('odd')

list_sum = 0

for num in l:
	list_sum += num
print(list_sum)

s = 'this is a string'
for letter in s:
	print(letter)

tup = (1,2,3,4,5)
for item in tup:
	print(item)

l = [(2,4), (6,8), (10,12)]
for tup in l:
	print(tup)

for (t1,t2) in l:
	print(t1) 
