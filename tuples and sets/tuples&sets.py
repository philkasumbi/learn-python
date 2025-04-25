#tuple is unordered and immutable collection of items
#we use parenthesis not square brackets 
#tuples are fast and immutables,can only be used by fixed elements eg coordinates,id
#can be used as key in dictionaries while list can be as a value
my_tuple = (1,2,3)

print(my_tuple[0])
print(my_tuple[1:])
print(type(my_tuple))

#tuple unpacking
x,y,z =my_tuple
print(x,y,z)
#tuples with one item need trailing comma
one_item = ("name",)

#sets 
my_set = {1,2,3,5}
my_set.add(4)#adding an element to a set
my_set.remove(2)#removing an element from a set 
print(my_set)
print(type(my_set))
#set constructor
your_set = set({1,2,5})
print(your_set)
print(type(your_set))
#why do we use sets
""""
in a set it automatically removes duplicates
great for membership checking 
supports set theory eg union- joining two sets

"""
your_set = set({1,2,2,5,5,6})
print(your_set)

print(my_set.union(your_set))#union of sets 
print(my_set.intersection(your_set))#shows element that are in the diffrent sets 
"""
There is no indexing and slicing in sets unlike lists and tuples
sets are unordered
"""

"""
do this task
create a program that takes a list of items with duplicates and returns:
    1. a Tuple of the first 3 unique items
    2. a set of all unique items 
"""

items = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

unique_items = []
for i in items:
    if i not in unique_items:
        unique_items.append(i)

first_three = tuple(unique_items[:3])
all_unique = set(unique_items)

print(f"The first three unique items are: {first_three}")
print(f"The all unique items are: {all_unique}")

