print(ord('M'))     
print(ord('m'))     

print(chr(75))      
print(chr(107))     

original = 'G'
code = ord(original)
recovered = chr(code)
print(f"Original: {original}, Code: {code}, Recovered: {recovered}")

data = input("Type something: ")
if type(data) is str and len(data) == 1:
    print("One character confirmed.")
    
    val = ord(data)
    if 65 <= val <= 90:
        print("This is Uppercase.")
    elif 97 <= val <= 122:
        print("This is Lowercase.")
    elif 48 <= val <= 57:
        print("This is a Number.")
    else:
        print("This is a Symbol.")
else:
    print("Invalid entry.")