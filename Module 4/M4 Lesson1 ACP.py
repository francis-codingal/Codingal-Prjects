def square_and_separate(start, end):
    squares = []
    for i in range(start, end + 1):
        squares.append(i**2)
    
    even_squares = []
    odd_squares = []
    
    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)
            
    print(f"Squares between {start} and {end}: {squares}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

square_and_separate(start_range, end_range)