Contact_book = {
    "Alice": "9876543210",
    "Bob": "1234567891",
    "Charlie": "7654321098"
}

print("Contact_book: ")
for name, number in Contact_book.items():
    print(f"{name}: {number}")

name = input("\nEnter the name of the Contact: ").capitalize()
phone_number = input("Enter the phone number: ")

if name in Contact_book:
    Contact_book[name] = phone_number
    print(f"\nNew Contact{name} added with number; {phone_number}")

print("\n Updated Contact_book: ")
for name, number in Contact_book.items():
    print(f"{name}: {number}")

