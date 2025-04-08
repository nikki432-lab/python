def Check_login(username, password):
    if username == "admin" and password == "1234":
        return "login successful"
    else:
        return "invalid credentials"
username = input("Enter your username: ")
password = input("Enter your password: ")
print(Check_login(username, password))
    
    
