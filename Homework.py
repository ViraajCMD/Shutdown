def shutdown(user_input):

    cleaned_input = user_input.strip().lower()
    
    if cleaned_input == "yes":
        print("shutting down")
    elif cleaned_input == "no":
        print("abort shut down")
    else:
        print("sorry")


user_choice = input("Do you want to switch off the system? ")
shutdown(user_choice)
