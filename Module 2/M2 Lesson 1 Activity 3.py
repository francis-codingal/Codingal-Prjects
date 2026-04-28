print("What's the vibe? \n1. Action \n2. Comedy")
vibe = int(input("Pick a vibe: "))

if vibe == 1:
    print("Nice! \n1. Superheroes \n2. John Wick style")
    sub_choice = int(input("Pick a sub-genre: "))
    
    if sub_choice == 1:
        print("Let's watch Spider-Man! 🕸️")
    else:
        print("Time for some high-octane stunts! 🔫")

elif vibe == 2:
    print("Need a laugh? \n1. Animated \n2. Stand-up")
    sub_choice = int(input("Pick a sub-genre: "))
    
    if sub_choice == 1:
        print("Shrek it is! 🧅")
    else:
        print("Pulling up a Netflix special... 😂")

else:
    print("Invalid mood. Go touch some grass! 🌱")