def validate_password(password):
    if len(password) < 8:
        return "Invalid: password must be atleast 8 characters long."
    if not any(char.isupper() for char in password):
        return "Inavild: password must contain at least 1 uppercase letter."
    if not any(char.islower() for char in password):
        return"Invalid: password must contain atleast 1 lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Invalid: password must contain atleast 1 digit."

    return "valid: password meets all criteria."

user_password = input("Enter your password: ")
print(validate_password(user_password))
