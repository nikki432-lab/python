def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers = [10,20,5,8,25,3]
print(find_largest(numbers))
        
        
        
