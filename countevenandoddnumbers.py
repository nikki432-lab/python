def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 ==0:
            even_count += 1
        else:
            odd_count += 1
    return even_count,odd_count
numbers = [1,2,3,4,5,6]
even_count,odd_count = count_even_odd(numbers)
print(f"Even numbers: {even_count},oddnumbers: {odd_count}")
            
