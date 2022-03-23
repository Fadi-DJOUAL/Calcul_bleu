import math

print("(1) Addition, (2) subtraction, (3) multiplication, (4) division, (5) exponent, (6) tan, (7) sin, (8) cos, (9) factorielle (10) log")

o = input("Entrez le nombre: ") 

if o == "1": 
    x = int(input("1er chiffre : ")) 
    y = int(input("2eme chiffre : ")) 
    print (x+y)

elif o == "2": 
    x = int(input("1er chiffre : ")) 
    y = int(input("2eme chiffre : ")) 
    print(x-y) 

elif o == "3": 
    x = int(input("1er chiffre : ")) 
    y = int(input("2eme chiffre : ")) 
    print(x*y) 

elif o == "4": 
    x = int(input("1er chiffre : ")) 
    y = int(input("2eme chiffre : "))
    print(x/y) 

elif o == "5": 
    x = int(input("1er chiffre : ")) 
    y = int(input("2eme chiffre : "))
    print(x**y) 

elif o == "6": 
    x = int(input("Chiffre : ")) 
    print(math.tan(x)) 

elif o == "7": 
    x = int(input("Chiffre : "))  
    print(math.sin(x)) 

elif o == "8": 
    x = int(input("Chiffre : ")) 
    print (math.cos(x))  

elif o == "9": 
    x = int(input("Chiffre : "))
    print(math.factorial(x)) 

elif o == "10": 
    x = int(input("Chiffre : "))  
    print(math.log(x)) 
