
#LIST is a collection of items
fruits = ["apple", "mango", "cherry"]
print(fruits)
print(fruits[-1])#indexing in lists
print(fruits[1:3]) #slicing in list 
print(fruits[:2])
print(fruits[1:])
print(fruits[:2])
print(fruits[-3:-1])


#list methods 
fruits.append("elderberry")#add to the end 
print(fruits)
fruits.insert(1, "BlueBerry")#Inserts at a desired position
print(fruits)
fruits.remove("elderberry")#removes the sprcific 
print(fruits)
fruits.pop()#removes the last element in the list
print(fruits)

del fruits[0]#delete at specific index


numbers = [5,8,6,0,3]
numbers.sort()#from the smallest
numbers.reverse()#from the largest
print(numbers)
print(numbers.count(8))#counting the available





