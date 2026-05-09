import os

def shutdown_computer(choice):
    if choice.lower() == "yes":
        print("Shutting down...")
        os.system("shutdown /s /t 1") 
    elif choice.lower() == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry, I didn't understand that.")

user_input = input("Would you like to shut down the computer? (yes/no): ")
shutdown_computer(user_input)