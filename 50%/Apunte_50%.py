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

print(f"        {title:^35}")# left <, right >, center ^
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

# Lists
"""Arrays are a place to store more than one thing with the same variable name. However, Python uses lists instead. Lists are literally lists of items. We can extract, remove, or change lists."""
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)
  
# Dynamic Lists
"""Estas son listas a las que uno puede añadir o eliminar elementos. Para añadir usamos .append() y para eliminar usamos .remove()"""
def printList():
  print()
  for item in toDoList:
    print(item)
  print()

toDoList = []
while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or remove the to do list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
  answer = ("Wanna go again? yes or no")
  if answer == "no":
    break
  
"""When we have a list of data, being able to print out that data in pretty ways is something we need to be able to do. So "pretty printing" is actually a thing."""
import os, time, random
listOfEmail = []

def prettyPrint():                                # Alternate
  os.system("clear")                          # def prettyPrint():
  print("listofEmail")                           # os.system("clear") 
  print()                                        # print("listofEmail") 
  counter = 1                                    # print()
  for email in listOfEmail:                      # for index in range(len(listOfEmail)): ""len() muestra la cantidad de elementos de una lista""
    color = random.randint(31,37)                #   print(f"{index}: {listOfEmail[index]}") 
    print(f"\033[{color}m{counter}- {email}")    # time.sleep(1)
    counter += 1 
  print("\033[00m")
  time.sleep(1)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail: # Comprobamos que el elemento este en la lista
      listOfEmail.remove(email)
  elif menu == "3": 
    prettyPrint()
  time.sleep(1)
  os.system("clear")
  answer = input("Wanna go again? ")
  if answer == "yes":
    break
  
# To do List
import os, time

def printList():
  print()
  for items in toDoList:
    print(items)
  print()

toDoList = []
while True:
  menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n").title() 
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in toDoList:
        toDoList.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=new
  elif menu=="delete":
    toDoList = []
  time.sleep(1)
  os.system('clear')
  answer = input("Wanna go? ")
  if answer == "yes":
    break

# String Manipulation
"""Estas manipulaciones se insertan luego de la variable y se ejecutan en el orden en que se insertan"""
"""
.lower() = all letters are lower case
.upper() = all letters are upper case
.title() = capital letter for the first letter of every word
.capitalize() = capital letter for the first letter of only the first word
.strip() removes any spaces on either side of the word.
"""
def printList():
  print()
  for i in myList:
    print(i)
  print()

myList = []
while True:
  first = input("First Name: ").strip().capitalize()
  last = input("Last Name: ").strip().capitalize()
  name = f"{first} {last}"
  if name not in myList:
    myList.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
  break
  
# String Slicing
"""Esto nos permite tomar carácteres de un string, ya sea uno o más"""
myString = "Hello there my friend."
print(myString[0]) # H
print(myString[6:11]) # there
print(myString[:11]) # Hello there
print(myString[12:]) # my friend
print(myString[0:6:2]) # Hlo
print(myString[::-1]) # dneirf ym ereht olleH
print(myString.split()) # split() divide un string en palabras usando los espacios como separador ['Hello', 'there', 'my', 'friend.']

print("STAR WARS NAME GENERATOR")
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()
first = all[0].strip()  # Estas son las partes del input
last = all[1].strip() # Estas son las partes del input
maiden = all[2].strip() # Estas son las partes del input
city = all[3].strip() # Estas son las partes del input
name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"
print(f"Your Star Wars name is {name}")

# Strings and Loops
"""Como un string es una lista con otro estilo, lo podemos recorrer con un loop for, y a partir de eso trabajamos con sus caracteres uno por uno"""
vowels = ["a","e","i","o","u"]
myString = "Will my vowels now be yellow?"

for letter in myString:
  if letter.lower() in vowels:
    print('\033[33m', end='') #yellow
  print(letter, end="")
  print('\033[0m', end='') #back to default
  
# Hangman
import random, os, time

listOfWords = ["apple", "orange", "grapes", "pear"]
word = random.choice(listOfWords) # random.choice() picks a random item from a list
letterPicked = []
lives = 6

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()
  
  if letter in letterPicked:
    print("You've tried that before")
    continue
    
  letterPicked.append(letter)
  
  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1
  
  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")

# Dictionaries
"""Dictionaries are a slightly different type of list that access data by giving each item a key. This creates what we call key:value pairs."""
myUser = {"name": "David", "age": 128}
myUser["name"] = "The legendary David"
print(myUser["name"])
print(f"Your name is {myUser['name']} and your age is {myUser['age']}") # No se repiten las mismas comillas

name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}
print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")

# Dictionaries with Loops
"""Dictionaries and loops are a bit trickier. This is because each dictionary item is made up of two parts - the name of the key and the actual value of that key."""
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for value in myDictionary.values(): # .values() method can be run on a data type. We still only get the value, and not the key.
  print(value)
print()
for name,value in myDictionary.items(): # The .items() function returns the key name and value. 
  print(f"{name}:{value}")
  
website = {"name": None, "url": None, "desc": None, "rating": None}
for name in website.keys():
  website[name] = input(f"{name}: ")
print()
for name, value in website.items():
  print(f"{name}: {value}")
  
# MokeBeast
mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}
print("MokéBeast")
print()
for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()
if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")
for name, value in mokedex.items():
  print(f"{name:<15}: {value}")
  
# 2D Lists
"""To add the second dimension, we put lists inside the first list."""
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]
my2DList[1][2] = "Linux"
my2DList[0] = ["Juan", 30, "PC"] 
print(my2DList[0])
print(my2DList[1][2])

import random
def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

bingo = []
numbers = []
for i in range(8):
  numbers.append(ran())
numbers.sort() # ordena la lista en orden ascendente

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
prettyPrint()

# 2D Dynamic Lists
listOfShame = [] 

while True: 
  menu = input("Add or Remove?") 
  if(menu.strip().lower()[0]=="a"): # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.

    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    row = [name, age, pref] 
    listOfShame.append(row) 

  else: 
    name = input("What is the name of the record to delete?") 
    for row in listOfShame: # Use a loop to extract one row at a time
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it
    
  answer = input("Wanna go again?")
  if answer == "n" or answer == "no":
      break
  

import random, os, time
def ran():
  number = random.randint(1, 9)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingo  # permite declarar la variable dentro de la función
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(num)
  numbers.sort()

  bingo = [[numbers[0], numbers[1], numbers[2]],
           [numbers[3], "BINGO", numbers[4]],
           [numbers[5], numbers[6], numbers[7]]]

bingo = []
createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item == "X":
        exes += 1
  if exes == 8:
    print("You have won")
    break
  time.sleep(1)
  os.system("clear")
  
# To Do List
print("Managment To Do List")
print()
toDoList = []
while True:
  action = input("Do you want to view, add, edit, or   remove an item from the to do list?\n")  
  if action == "add":
    action = input("What do you want to add?\n")
    due = input("When is it due by?\n")
    priority = input("What is the priority?\n")
    toDo = [action, due, priority]
    if toDo in toDoList:
      print("This is already in the list")
    else:
      toDoList.append(toDo)
      print("Added")
  elif action == "view":
    view = input("Do you want to view all or view by priority?\n")
    if view == "all":
      print(toDoList)
    elif view == "priority":
      priority = input("What priority?\n")
      for row in toDoList:
        if priority in row:
          print(row)
  elif action == "edit":
    edit = input("What do you want to edit?\n")
    for row in toDoList:
      if edit in row:
        toDoList.remove(row)
        action = input("What do you want to add?\n")
        due = input("When is it due by?\n")
        priority = input("What is the priority?\n")
        toDo = [action, due, priority]
        if toDo in toDoList:
          print("This is already in the list")
        else:
          toDoList.append(toDo)
          print("Added")
  elif action == "remove":
    remove = input("What do you want to remove?\n")
    for row in toDoList:
      if remove in row:
        toDoList.remove(row)
        print("Removed")

  answer = input("Do you want to see the menu again?\n")
  if answer == "yes":
    continue
  else:
    break

# 2D Dictionaries
"""Remember that dictionaries are very similar to lists, except that they store data as key:value pairs. The value is what it's worth and the key is what it is called. The key is used to access the value, and keys are more meaningful than index numbers."""
"""The key is the name of the beast, but the value is a whole new dictionary that contains the details of the beast.
Each key:value pair in the dictionary is now a key that accesses a related dictionary."""
def prettyPrint():
  print()
  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()
    
clue = {}
while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")
  clue[name] = {"location": location, "weapon":weapon} 
  prettyPrint()
  answer = input("Wanna go again?")
  if answer == "no":
    break
  
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}
courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress)
print()
print(courseProgress["Erica"])
print()
print(courseProgress["Erica"]["daysCompleted"])
  
mokedex = {}
def prettyPrint():
  print("Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"{key:^12}|{value['type']:^10}|{value['hp']:^6}|{value['mp']:^6}")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "name": name,"type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
  answer = input("Wanna add another beast? ")
  if answer == "yes":
    continue
  else:
    break
  
# Top Trumps
trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick your character\n> ")
  comp = random.choice(list(trumps.keys())) # random.choice() elige al azar en una lista, y list() convierte el diccionario en una lista
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ")

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")
    
  answer = input("Wanna add another beast? ")
  if answer == "yes":
    continue
  else:
    break
    
    
# Writting into a File
"""We can write data to other files for longer term storage, then access it when we need it.

When we use variables, lists, dictionaries and other data structures in our code, the data inside them are stored in the computer's RAM.

RAM is temporary storage (usually called memory). It's used to hold data and instructions for programs that your computer currently has open.

The problem is, that when a program finishes, or is closed, its data and instructions are removed from the RAM to free up space.

This is why you had to re-input all of your test data for your dynamic list & dictionary programs every time you ran them. The contents of those lists/dictionaries were removed from RAM when the program finished executing."""

f = open("savedFile.txt", "w") # Así es como se abre un archivo
"""The variable (f): This is needed to allow your program to communicate to the file. Normally this would have a lovely meaningful name. However, you will need to type this variable name lots, and lots, and lots. So short is good. 'f' is short for 'file'.

The file name (the first item in brackets, "savedFile.txt"): You MUST code this to match the filename EXACTLY and include the file extension.

The 'w' (second item in brackets): This sets the permissions for the file. 'w' means 'write'. This means that if the file doesn't already exist, the program will create a new blank file with that file name. However, if it does already exist it will be overwritten with a blank file."""

f = open("savedFile.txt", "w")
f.write("Hello there") # .write() command will write the piece of data in brackets into the file. You can use as many of these as you want
f.close() # Nothing gets saved until we close the file using the .close() command

f = open("savedFile.txt", "a+") # 'a+' means 'add to the end of the file, or create a new one if it doesn't exist'
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("clear")
  answer = input("Wanna add another beast? ")
  if answer == "yes":
    continue
  else:
    break
  
# Reading from a File
"""Once we've got data into a file, wouldn't it be just splendid to load it back into our program to use again?"""
f = open("filenames.list", "r") # 'r' de 'read'
contents = f.read() # .read() loads the contents of the file into a variable 
contents = contents.split() # This splits the string into a list of individual elements.
print(contents)
contents = f.readline().strip() # Esto translada una línea de código a la vez, y el strip() remueve la nueva línea predeterminada del print()
print(contents)
f.close()

f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  if contents == "":
    break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank
  print(contents)
  # Moved the print after the break so it won't output the final blank line.
f.close()

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None
for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]
print("The winner is", name, "with", highscore)

# Idea Storage
"""Do you have brilliant ideas at inconvenient times? Do you need a handy way of storing those ideas? Have you never heard of smartphone voice note apps? Or pens and paper? """
def add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  else:
    show()
