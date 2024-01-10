# from getpass import getpass as input 
# print() -
# varialbes -
# input() -
# concatenar -
# if elif else -
# int() float() str() -
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
# round(answer, 2) -
# while True -
# continue break exit() -
# import -
# and or not -
# random.randint(1,1000000) -
# for -
# range() for counter in range(10): -
# subrutinas parametros
# return

import random
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
    suma = round(number1 + number2, 3)
    resta = round(number1 - number2, 3)
    multiplicacion = round(number1 * number2, 3)
    division = round(number1 / number2, 3)
    modulo = round(number1 % number2, 3)
    divisor = round(number1 // number2, 3)
    
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
        
print()
print("Now we are gonna see Rock, Paper, Scissors Game")
print("You are gonna play against the machine")
print()
points_user = 0
points_machine = 0
while True:
    print("The user has", points_user, "and the machine has", points_machine)
    eleccion = random.randint(1,3)
    if eleccion == 1:
        machine = "rock"
    elif eleccion == 2:
        machine = "paper"
    elif eleccion == 3:
        machine = "scissors"
    print("The machine already chose, now you choose")
    print("Rock, Paper or Scissors")
    user = input()
    if user == machine:
        print("Empate")
        print()
        continue
    elif user == "rock" and machine == "scissors" or user == "scissors" and machine == "paper" or user == "paper" and machine == "rock":
        print("Punto para el usuario")
        points_user += 1
        print()
    elif machine == "rock" and user == "scissors" or machine == "scissors" and user == "paper" or machine == "paper" and user == "rock":
       print("Punto para la máquina")
       points_machine += 1
       print()
    
    if not points_user == 3 and not points_machine == 3:
        continue
    elif points_user == 3:
        print("The user wins!!")
    elif points_machine == 3:
        print("The machine wins!!")
    print()
    
    answer = input("Do you wanna go again? yes or no ")
    if answer == "yes":
        points_user = 0
        points_machine = 0
        continue
    elif answer == "no":
        break
    
print()
print("Now we have the guess the number game!!")
print("The machine chooses a number between 1 and 100 and you have 10 shots at guessing it")
while True:
    print()
    number = random.randint(1,100)
    print("The machine has chosen the number")
    for counter in range(10):
        guess = int(input("What's your guess? "))
        if guess == number:
            print("Congratulations, you have won!!")
            break
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
    print()
    print("The number was", number)
    answer = input("Do you wanna go again? yes or no ")
    if answer == "yes":
        continue
    elif answer == "no":
        break
                