#!/usr/bin/env python3

#Creating lists
my_list1 = [1, 2, 3]
print(my_list1)
my_list2 = ['string', 23, 1.0, 'o']
print(my_list2)

#Indexing and slicing lists
print(my_list1[0])
print(my_list1[1:])
print(my_list2[:3])
my_list3 = my_list1 + ['new item']
print(my_list3)
print(my_list1 * 2)

#Basic List Methods
print(len(my_list1))
print(my_list1.append(4))
print(my_list1)
print(my_list1.pop())
print(my_list1.pop(0))
print(my_list1)
new_list = ['a', 'e', 'i', 'o', 'u']
print(new_list.reverse())
print(new_list)
print(new_list.sort())
print(new_list)

#Nesting Lists
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1, l_2, l_3]
print(matrix)
print(matrix[0][0])

#Introduction to list Comprehension
first_column = [row[0] for row in matrix]
print(first_column)
