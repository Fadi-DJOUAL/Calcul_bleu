import math

print("(1) Addition, (2) subtraction, (3) multiplication, (4) division, (5) exponent, (6) tan, (7) sin, (8) cos, (9) factorielle (10) log, (11) racine, (12) puissance de 10, (13) puissance carrée, (14) Modulo ")

o = input("Entrez le numéro de l'opération: ") 
if (o >=0 and o<=14):
	if o == "1": 
    		x = int(input("Donnez un 1er chiffre : ")) 
    		y = int(input("Donnez un 2eme chiffre : ")) 
    		print (x,"+",y,"=",x+y)

	elif o == "2": 
    		x = int(input("Donnez un 1er chiffre : ")) 
    		y = int(input("Donnez un 2eme chiffre : ")) 
    		print(x,"-",y,"=",x-y) 

	elif o == "3": 
	    	x = int(input("Donnez un 1er chiffre : ")) 
  	  	y = int(input("Donnez un 2eme chiffre : ")) 
  	 	 print(x,"*",y,"=",x*y) 

	elif o == "4": 
    		x = int(input("Donnez un 1er chiffre : ")) 
    		y = int(input("Donnez un 2eme chiffre : "))
    		print(x,"/",y,"=",x/y) 

	elif o == "5": 
    		x = int(input("Donnez un 1er chiffre : ")) 
    		y = int(input("Donnez un 2eme chiffre : "))
  		print(x,"^",y,"=",x**y) 

	elif o == "6": 
   		 x = int(input("Donnez un chiffre : ")) 
   		 print("tan =",math.tan(x)) 

	elif o == "7": 
    		x = int(input("Donnez un chiffre : "))  
   		print("sin = ",math.sin(x)) 

	elif o == "8": 
    		x = int(input("Donnez un chiffre : ")) 
    		print ("cos = ",math.cos(x))  

	elif o == "9": 
    		x = int(input("Donnez un chiffre : "))
    		print("fact = ",math.fact(x))

	elif o == "10":
    		x = int(input("Donnez un chiffre : "))
    		print("log = ",math.log(x))

	elif o == "11":
    		x=int(input(" Donnez un nombre : "))
    		print("racine de ",x," = ",math.sqrt(x))

	elif o == "12":
   		 x=int(input(" Donnez un nombre : "))
    		print("10 ^ ",x," = ",10**x)

	elif o == "13":
    		x=int(input( " Donnez un nombre : "))
		print("Le carré de",x,"est ",x**2)

	elif o == "14":
    		x=int(input(" Donnez un nombre : "))
		print("Modulo de ",x," = ",x%2)

else :
    print("Erreur , veuillez choisir une opération entre 1 et 14")
