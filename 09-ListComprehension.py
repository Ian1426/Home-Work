even_numbers = (0, 2, 4, 6, 8, 10)
print(even_numbers)
squares_of_even_numbers = [x **2 for x in (even_numbers) if x % 2 == 0] 
print(squares_of_even_numbers)
## Using a list comprehension to analyze the even numbers given in the list to square it and print the new list