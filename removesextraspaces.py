def remove_extra_spaces():
    user_input = input("Enter your message: ")
    cleaned_message = " ".join(user_input.split())

    print("cleaned_message:",cleaned_message)

remove_extra_spaces()
