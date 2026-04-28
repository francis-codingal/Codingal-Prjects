battle_pass = input("Do you have the Premium Battle Pass? (Y/N): ").strip().upper()

if battle_pass == 'Y':
    print("Access Granted: Welcome to the Ranked Lobby!")
else:
    level = int(input("What is your current Player Level? "))

    if level >= 20:
        print("Access Granted: Level requirement met. Good luck!")
    else:
        print("Access Denied: You need to be Level 20 or have a Battle Pass.")