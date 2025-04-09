def sum_of_evens(start,end):
    total = 0
    for num in range (start,end+1):
        
            if num % 2 == 0:
                total += num
    return total
start = 1
end = 10
result = sum_of_evens(start,end)
print(f"the sum of even numbers from {start} to {end} is :{result}")
