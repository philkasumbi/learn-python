#write a python program that prints even numbers between 1 and 100

#a number is even if it can be divided by 2 and its remainder is 0

for i in range(100):
   if i%2 == 0:
    print(i)
#to avoid the use of if
for i in range(0,100,2):
    print(i)