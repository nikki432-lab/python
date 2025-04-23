data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Engineer"
}

key = input("Enter a key: ")

try:
    value = data[key]
    print(f"The value for '{key}' is: {value}")
except KeyError:
    print(f"Error: The key '{key}' does not exist in the dictionary.")
