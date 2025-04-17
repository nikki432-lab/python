students = {
    "Alice": 85,
    "Bob": 78,
    "Charlue": 92,
    "Diana": 88,
    "Eve": 76
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks:{students[name]}")
else:
    print(f"student {name} not found in the records.")
