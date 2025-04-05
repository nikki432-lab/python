even_squares = [num**2 for num in range (1,21) if num%2==0]

sum_of_squares = sum(even_squares)

print("List of squares of even numbers:",even_squares)
print("Sum of squares of even numbers:",sum_of_squares)
