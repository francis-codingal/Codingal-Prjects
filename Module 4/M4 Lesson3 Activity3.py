country_code = {'England' : '0044',
                'Japan' : '0081',
                'Nepal' : '00977'}

print("Country code for England -")
print(country_code.get('England', 'Not Found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))