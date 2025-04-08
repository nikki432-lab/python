def get_ticket_price(age):
    if age < 5:
        return "Free"
    elif 5<=age<=18:
        return "100"
    elif 19 <= age <= 60:
        return "200"
    else:
        return "150"
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print ("age cannot be negative.")
    else:
            print(f"ypur ticket price is:{get_ticket_price(age)}")
except ValueError:
     print("invalid input.please enter a valid age.")


              
