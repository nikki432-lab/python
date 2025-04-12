def find_duplicates(numbers):
    duplicates = []
    seen = set()
    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates

my_list = [1.5,5,7,3,1,9,3]
duplicates = find_duplicates(my_list)
print(f"Duplicate values: {duplicates}")
