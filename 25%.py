# print() -
# varialbes -
# input() -
# concatenar -
# if else elif -
# int() float() -
# color de texto ("\033[--m") -
"""
    Color	    Value
    Default	      0
    Black	      30
    Red           31
    Green	      32
    Yellow	      33
    Blue	      34
    Purple	      35
    Cyan	      36
    White	      37
"""
# anidar código -
# and or not
# condiciones numéricas -
"""
    ==
    !=
    > 
    >=
    < 
    <=
"""
# principios matemáticos -
"""
adding = 4 + 3 = 7
subtraction = 8 - 9 = -1
multiplication = 4 * 32 = 128
division = 50 / 5 = 10.0
squared = 5**2 = 25
modulo = 15 % 4 = 3
divisor = 15 // 2 = 7
"""
# round(answer, 2)
# while True 
# continue break exit()
# for
# range() for counter in range(10):
# import
# random.randint(1,1000000)
# subrutinas parametros
# return
# from getpass import getpass as input 

print()
print(("\33[31m"),"Welcome to the summary of the 25% of the course!!!",("\33[0m"))
answer = input("Do you wanna keep going? yes or no: ")
if answer == "no":
    exit()
print()
print("Let's see a program that contains all the contents you have seen until now.")
print()
name = input("What's your name? ")
age = input("How old are you? ")
home = input("Where are you from? ")
print()
print("Okay, so you are", name, ", you are", age, "years old, and you are from", home)
print()
print("Now let's see some simple programs that are easy to understand")
print()
print("First we have a calculator")
print("You choose the method you want to apply and the numbers to go with it")
while True:
    print("First you choose the numbers")
    number1 = float(input("First number: "))
    number2 = float(input("Second number: "))
    print()
    print("Suma, Resta, Multiplicación, División, Potencia, Modulo, Divisor")
    suma = number1 + number2
    resta = number1 - number2
    multiplicacion = number1 * number2
    division = number1 / number2
    modulo = number1 % number2
    divisor = number1 // number2
    
    method = input("Choose the method: ")
    if method == "suma":
        print("The result is", suma)
    elif method == "resta":
        print("The result is", resta)
    elif method == "multiplicacion":
        print("The result is", multiplicacion)
    elif method == "division":
        print("The result is", division)
    elif method == "potencia":
        print("The result is", number1 ** number2)
    elif method == "modulo":
        print("The result is", modulo)
    elif method == "divisor":
        print("The result is", divisor)
    else:
        print("The method is not valid")
        continue
    
    answer = input("Do you wanna go again? yes or no ")
    if answer == "yes":
        continue
    elif answer == "no":
        break
        
