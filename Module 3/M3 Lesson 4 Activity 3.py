is_finished = False
while not is_finished:
    try:
        x = int(input("Enter an integer: "))
        
        while x > 100:
            print("Value too high!")
            break 
            
        is_finished = True
    except ValueError:
        print("Error: Please enter a numeric value")