import math
print ("##############################\n#########-CALCULATOR-#########\n##############################")
print("choisissez une opération:")
print("(1) Addition\n(2) subtraction\n(3) multiplication\n(4) division\n(5) exponent\n(6) tan\n(7) sin\n(8) cos\n(9) factorielle\n(10) log")

o = input("votre choix: ")

if o == "1":
    x = int(input("1er chiffre : "))
    y = int(input("2eme chiffre : "))
    print (x,"+",y,"=",x+y)

elif o == "2":
    x = int(input("1er chiffre : "))
    y = int(input("2eme chiffre : "))
    print(x,'-',y,"=",x-y)

elif o == "3":
    x = int(input("1er chiffre : "))
    y = int(input("2eme chiffre : "))
    print(x,"x",y,"=",x*y)

elif o == "4":
    x = int(input("1er chiffre : "))
    y = int(input("2eme chiffre : "))
    print(x,"/",y,"=",x/y)

elif o == "5":
    x = int(input("1er chiffre : "))
    y = int(input("2eme chiffre : "))
    print(x,"e",y,"=",x**y)

elif o == "6":
    x = int(input("Chiffre : "))
    print(x,"tan","=",math.tan(x))

elif o == "7":
    x = int(input("Chiffre : "))
    print(x,"sin","=",math.sin(x))

elif o == "8":
    x = int(input("Chiffre : "))
    print (x,"cos","=",math.cos(x))

elif o == "9":
    x = int(input("Chiffre : "))
    print(x,"fact","=",math.factorial(x))

elif o == "10":
    x = int(input("Chiffre : "))
    print(x,"log","=",math.log(x))
