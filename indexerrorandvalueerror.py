my_list = ["apple", "banana", "cherry", "date", "elderberry"]

try:
    index = int(input("Enter an index: "))
    print(f"value at index {index}: {my_list[index]}")

except IndexError:
    print("Error: Index out of range! please enter a valid index within the list.")
except ValueError:
    print("Error:invalid input! please enter a number.")
