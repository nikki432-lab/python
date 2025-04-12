def find_largest_and_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

my_list = [1,8,12,25,-5,0,18]
largest,smallest = find_largest_and_smallest(my_list)
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
