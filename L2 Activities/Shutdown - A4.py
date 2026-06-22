def shutdown(command):
    if command == "yes":
        return "Shutting down"
    elif command == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

user_input = input("Enter yes or no: ")

print(shutdown(user_input))