#write a while loop python program that prints only even numbers bettwen 0 and 20

even_numbers = 0

while even_numbers<= 20:
    print(f"even....{even_numbers}")
    even_numbers += 2



count = 0

while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1