# os Library, time Library
"""La librería os nos permite hablarle a la consola, con esta librería podemos limpiar la consola, y esta es solo una de sus funciones. Luego, la librería time nos permite pausar la ejecución del programa por un periodo determinado de tiempo"""
import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")

# Secrets of print
"""El comando print te permite imprimir cosas en la consola, pero tiene variantes para que el contenido se despliegue o tenga una apariencia diferente"""
for i in range(0, 100):
  print(i, end=", ") # comma and space

for i in range(0, 100):
  print(i, end="\n") # new line

for i in range(0, 100):
  print(i, end="\t") # tab indent


for i in range(0, 100):
  print(i, end="\v") # vertical tab

print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="") # sep (separator) especifica lo que separa cada sección de la concatenación de un print

import os, time
print('\033[?25l', end="") # Esto nos permite apagar el cursor de la consola
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")
print('\033[?25h', end="") # Esto nos permite reactivar el  cursor de la consola

def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")

# Format Strings
"""Format Strings o f-strings, son la mejor manera de combinar variables y texto juntas, una mejor alternativa a la concatenación"""
name = "Katie"
age = "28"
pronouns = "she/her"
print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)
print(response)

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"
print(response)

def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"        {title:^35}")# left = <, right = >, center = ^
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")

print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>35}")
text = "Honest."
print(f"{colorChange('red')}{text:^35}")
text = "Username: "
username = input(f"{colorChange('white')}{text:^35}")
text = "Password: "
username = input(f"{colorChange('white')}{text:^35}") 

