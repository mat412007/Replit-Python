# Replit.com Curso de 100 días de Python

# Comienzos
"""Para imprimr una línea en la consola de python se usa el término de """ 
print("")

"""Para guardar un valor en un string simplemente se hace así"""
variable_1 = "Esta es la primera variable" 
print(variable_1)
variable_2 = input("¿Cual es la variable? :")
print(variable_2)

"""Para concatenar variables junto a texto predeterminado hacemos"""
name = input("¿Cual es tu nombre? :")
age = input("¿Cuantos años tenes? :")
print()
print("Tu nombre es", name, "y tengo", age)

# Colores de texto
"""Para cambiar el color del texto que aparece en la consola usamos"""
print("\033[31m")
print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
"""Hay muchos colores"""
"""
    Color	    Value
    Default	    0
    Black	      30
    Red	        31
    Green	      32
    Yellow	    33
    Blue	      34
    Purple	    35
    Cyan	      36
    White	      37
"""

# IF and ELSE 
"""Se usan para especificar condiciones, si la condición del if se cumple se ejecuta lo que este debajo, de lo contrario se ejecuta el else"""
myName = input("What's your name?: ")
if myName == "David":
    print("Welcome Dude!")
    print("You're just the baldest dude I've ever seen")
else:
    print("Who on earth are you?!")
    
# ELIF
"""El elif es un extra en las condiciones de if y else, se usa para poner condiciones extra"""
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!")
 
# Nesting Code
"""Con esto nos referimos por ejemplo a insertar un if dentro de otro if"""
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")

# AND, OR , NOT
"""Estas palabras se usan para aclarar condiciones"""
if username == "mark" and password == "password":
    print("Welcome Mark!")
    
if name == "Dave" or name == "dave":
  print("Hi Dave")
  
if not name == "Dave":
  print("Hi Dave")
  
# Condicines con números
"""En los if también se apoyan otros símbolos para especificar otras cosas que no sean igualidades"""
5 == 5
3 != 5
5 > 3
5 >= 3
3 < 5
3 <= 5

myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
  
# INT y FLOAT
"""Hay dos tipos de números en la computadora para que reconozca, enteros y con coma. Para cambiar un INPUT a un valor numérico se usan de la siguiente manera"""
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
  
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
  
# Math Principles
"""Ahora introducimos unas operaciones matemáticas en el código"""
adding = 4 + 3 # = 7
print(adding)

subtraction = 8 - 9 # = -1
print(subtraction)

multiplication = 4 * 32 # = 128
print(multiplication)

division = 50 / 5 # = 10.0
print(division)

squared = 5**2 # = 25
print(squared)

modulo = 15 % 4 # = 3
print(modulo)

divisor = 15 // 2 # = 7
print(divisor)

answer = 98.52 / 3
answer = round(answer, 2) # round reduce los decimales del número según lo que insertes, en este caso daría = 32.84

# Debugging Code
"""Cuando hablamos de un bug, nos referimos a un error en el código, debug es la acción de corregir esos errores"""

# Rock, Paper, Scissor game!
from getpass import getpass as input #Esta línea se asegura de que los input no sean visibles
print("Welcome to the Rock, Paper, Scissors game!")
print("Please choose R, P or S")
print()
user_1 = input("Player 1: ")
print()
user_2 = input("Player 2: ")
print()
if user_1 == "R" and user_2 == "S":
  print("Player 1 wins!")
elif user_2 == "R" and user_1 == "S":
  print("Player 2 wins!")
elif user_1 == "S" and user_2 == "P":
  print("Player 1 wins!")
elif user_2 == "S" and user_1 == "P":
  print("Player 2 wins!")
elif user_1 == "P" and user_2 == "R":
  print("Player 1 wins!")
elif user_2 == "P" and user_1 == "R":
  print("Player 2 wins!")
elif user_1 == user_2:
  print("Es un empate!")
else:
  print("Please choose R, P or S")

# Loops
"""Un while loop le permite a tu código repetirse a sí mismo según una condición que vos seteas"""
exit = ""
while exit != "yes":
  animal = input("What animal do you want to hear? ")
  print()
  if animal == "cow":
    print("Mooohhh")
  elif animal == "lion":
    print("Roarrrr")
  elif animal == "snake":
    print("Hisssss")
  elif animal == "dog":
    print("Woof woof")
  elif animal == "cat":
    print("Miow miow")
  elif animal == "duck":
    print("Quack quack")
  else:
    print("Sorry, I don't know that animal sound. Try again!")
  print()
  exit = input("Do you want to exit? ")

# While True Loop
"""Con tan solo poner el comando True como condición de un loop, se ejecutará hasta que se encuentre con el comando break"""
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break #Esto hace que salgas del while
print("Bye!")

# Continue and exit() command
"""El comando continue reinica un loop desde el principio, y el exit() command hace que vos salgas de del programa completo"""
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")

# For Loop
"""For cumple la misma función que un while loop, la única diferencia es que este sirve mejor cuando tenemos una idea de cuantas veces queremos que el loop se repita, todo esta información en una sola línea de código"""
for counter in range(10): # range() es una función que crea una lista de números dentro del rango que creas. En el caso de un solo número, escala de uno en uno hasta llegar al número anterior al del rango
  print(counter) # La variable que se inserta en el lugar de counter siempre comienza en 0, a menos de que haya dos números en la funcion range()

# Range() command
"""Este comando define un rango, pero según la cantidad de valores que insertes, del uno al tres, su comportamiento cambia"""
for counter in range(10):
  print(counter)
  
for i in range(1, 13):
  print(i, "x 13 =", i * 13)

for i in range(10, -1, -1):
  print(i)

# Libraries and random.randint() command
"""Las librerías son colecciones de código que fueron escritas por otras personas, un ejemplo de estas librerías son los game engines"""
import random
print("WELCOME TO THE GAME")
print()
print("Guess a number from 1 to 1,000,000!")
print()
tries = 1
number = random.randint(1,1000000)
while True:
  guess = int(input("What is your guess? "))
  if guess < number:
    print("Too low")
    tries += 1
  elif guess > number:
    print("Too high")
    tries += 1
  elif guess == number:
    print("Correct!")
    break
  else:
    print("That is not a number I recognize.")
print("It took you", tries, "guesses to get the number correct.")

# Subroutine
"""Una subrutina le dice a la compitadora que una pieza de código existe y que la corra una y otra vez, su estructura el comando def(), con el nombre de la subrutiba, los argumentos que recibe, y el código que tiene dentro"""
def login():
  while True:
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if name == "admin" and password == "admin":
      print("Login successful")
      break
    else:
      print("Login failed")
      continue
print("Log into the server")
login()

# Parameters
"""Parametros son adiciones para subrutinas para que puedan recibir información que después usan en su programa"""
def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)

# Return command
"""El comando return le permite a las subrutinas enviar información devuelta al programa principal, la función llamada se reemplaza con el valor retornado"""
import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("Character stats generator")
haveACharacter = "yes"
while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")

