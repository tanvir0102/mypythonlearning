#!/usr/bin/env python3


x = 0

while x < 10:
	print('x is currently: ', x) 
	x += 1
else:
	print("All done!!")

x = 0
while x < 10:
	print('x is currently: ', x)
	print('x is still less than 10, adding 1 to x')
	x += 1

	if x == 3:
		print('Hey x is equals 3 !')
		break
	else:
		print('continuning....')
		continue
		
