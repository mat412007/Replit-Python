# Auto Save and Auto Load
""" It's easy to access, amend, or remove a piece of data held in a list (in the RAM). Holding data in secondary storage in a file makes this more difficult. Or so you thought."""
import os, time, random
todo = []
# Auto Load
f = open("to.do", "r")
todo = eval(f.read()) # The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
f.close()

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()
  time.sleep(1)
  os.system("clear")
  # Auto Save
  f = open("to.do", "w")
  f.write(str(todo)) # El argumento de write() debe ser un string, no una lista
  f.close()
  answer = input("Wanna go again?\n")
  if answer.strip().lower() == "y":
      break

# Try...Except
"""Sometimes, we just can't code around a crash. It's coming anyway, and all you can do is brace for impact. Until now!"""
myStuff = []
try: # All the code that should work goes inside the try
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
except Exception as err: # We can tell except what type of error(s) to look for. Exception (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is.
  print("ERROR: Unable to load")
  print(err) 
for row in myStuff:
  print(row)
"""--------------"""
debugMode = True
myStuff = []
try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
except Exception:
  print("ERROR: Unable to load")
  if debugMode:
    print('traceback') # print(traceback) Imprime el error en rojo de forma especifica
for row in myStuff:
  print(row)
"""-----------"""
pizza = []
try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza list, using a blank list")

def viewPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  for row in pizza:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  time.sleep(2)

def addPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  toppings = input("Toppings: ")
  size = input("Size (s/m/l): ").lower()
  while True:
    try:
      qty = int(input("Quantity: "))
      break
    except:
      print("Error: Quanity must be a whole number")
  cost = 0
  if size=="s":
    cost = 5.99
  elif size=="m":
    cost = 9.99
  else:
    cost = 14.99
  total = cost * qty
  total = round(total, 2)
  row = [name, toppings, size, qty, total]
  pizza.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("Rominos Pizza")
  print()
  menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  if menu == "1":
    addPizza()
  else:
    viewPizza()
  f = open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()
  answer = input("Wanna go again? ")
  if answer.strip().lower() == "y":
    break

# RPG Inventory
import os, time
inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def addItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").capitalize()
  inventory.append(item)
  print("Added")

def viewItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}") # count() cuenta la cantidad de veces que un elemento está en una lista
      seen.append(item)
  time.sleep(2)

def removeItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print("Removed")
  else:
    print("You don't have that item")

while True:
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu=="1":
    addItem()
  elif menu=="2":
    viewItem()
  else:
    removeItem()
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
  answer = input("Wanna go again? ")
  if answer.strip().lower() == "y":
    break
  

# CSV Files (Comma-Separated Values)
"""CSV files are a way of storing a spreadsheet as a text file. Every value in the file is separated by a comma."""
import csv # Imports the csv library

with open("January.csv") as file: # Opens the csv file
  reader = csv.reader(file) # reads the contents of the csv file into the 'reader' variable
  line = 0
  for row in reader: # loop to output each row in the 'reader' variable one at a time.
    print (row)

"""-------------------"""
with open("January.csv") as file: 
  reader = csv.reader(file) 
  line = 0
  for row in reader: 
    print (", ".join(row)) # join() adds a comma and space and then joins data, you could try joining with tabs too with `\t`

"""----------------------"""
with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  line = 0
  for row in reader: 
    print (row["Net Total"])

"""-----------------------"""
with open("January.csv") as file: 
  reader = csv.DictReader(file) 
  total = 0
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"]) # Keeps a running total
print(f"Total: {total}") #Outputs

# The os Library
print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.
files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.") # Chequea si el archivo está en la carpeta presente
os.mkdir("Hello") # Creates a folder called 'Hello'
os.rename("myname.txt", "NEW.o") # Renames 'myname.txt' to 'NEW.o'
"""-------------------"""
todo = []
fileExists = True
try:
  f = open("to.do", "r")
  todo = eval(f.read())
  f.close()
except:
  fileExists = False

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()
    
  time.sleep(1)
  os.system("clear")
  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
    name = f"backup{random.randint(1,1000000000)}.txt"
    os.popen(f"cp to.do backups/{name}")
  
  f = open("to.do", "w")
  f.write(str(todo))
  f.close()
  answer = input("Wanna go again? ")
  if answer.strip().lower() == "y":
    break

# Music Streaming Service
import csv, os

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  
  for row in reader:
    dir = os.listdir()
    artist = row["Artist(s)"].title()
    print(artist)
    if artist not in dir:
      os.mkdir(artist)
    song = row["Song"]
    print(row["Song"])
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()

# Recursion
"""Recursion is a type of program where you get a subroutine to call itself. Recursion lets us solve problems in a more human way. Some mathematical problems can just be solved better using recursion."""
def reverse(value):
  if value <= 0:
    print("Done!")
    return
  # This `if` provides the 'stop' condition for the program. Otherwise it would run forever.
  else: # if we're not at the stop condition.
    for i in range(value):
      print("💯", end="") # Outputs 'value' emojis
    print() # New line
    reverse(value - 2) # takes 2 off the value and calls the subroutine again with this new number. Eg if value was 7 it would call 'reverse(value)' again with value as 5.
reverse(7)
"""--------------"""
def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)
print(factorial(5))

# Debugger
"""The debugger helps us keep track of what's going on without having to print all the time. We can slow down the execution of the program, keep track of what's stored in variables and lists at any given point, and set breakpoints on any lines that need special attention."""

# Palindromes
"""Estas son palabras simétricas, se leen igual en ambos sentidos""" #string.reverse() 
def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[::-1])
print(palindrome("racecar"))
"""--------------------"""
def palindrome(word):
  if len(word)<=1:
    return True
  elif word[0] != word[-1]:
    return False
  reverse = ""
  for i in range(len(word)):
    reverse = word[i] + reverse
  return reverse

word = input("Enter a word: ")
reverse = palindrome(word)
if reverse == word:
  print("This is a palindrome")
else:
  print("Not a palindrome")
  
# The Magic of Time
"""Your computer (and all of the other ones) uses something called the Unix epoch to measure time. It counts the amount of seconds elapsed since Jan 1st, 1970 (even when the power's off - there's a small battery on your motherboard that keeps this function running)."""
import datetime
myDate = datetime.date(year=2022, month=12, day= 7)
myDate = datetime.date(2022, 12, 21)
timestamp = datetime.datetime.now()
today = datetime.date.today()
difference = datetime.timedelta(days=14) # The difference I want
newDate = today + difference 

holiday = datetime.date(year = 2022, month = 10, day = 30) 
if holiday > today: 
  print("Coming soon")
elif holiday < today: 
  print("Hope you enjoyed it")
else: 
  print("HOLIDAY TIME!")
"""--------------------"""
today = datetime.date.today()
print("EVENT COUNTDOWN")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)
difference = event - today
difference = difference.days

if difference>0:
  print(f"{difference} days to go")
elif difference<0:
  print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
else:
  print("🥳🥳🥳🥳🥳🥳🥳 Today!")
  
# Replit DB
"""Replit DB (Database) is a Replit specific feature that allows you to store data directly in a repl using a built-in database."""
from replit import db
db["test"] = "Hello there" # Storing information
keys = db.keys() # List all keys
print(keys)
value = db["test"] # Getting a keys value
print(value)
del db["test"] # Deleting a key
db["login1"] = "david"
db["login2"] = "pamela"
db["login3"] = "sian"
db["login4"] = "ian"
matches = db.prefix("login") # Finding all matching keys
print(matches)
"""------------------"""
db["david"] = {"username": "dmorgan", "password":"baldy1"} # Storing a dictionary
keys = db.keys()
print(keys)
value = db["david"]
print(value["password"])
"""-----------------"""
keys = db.keys()
for key in keys:
  print(f"{key}: {db[key]}") # Acessing all the keys and values
"""------------------"""
try:
  value = db["key"]
except:
  pass
"""--------------------"""
def addTweet():
  tweet = input("🐥 > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")

while True:
  print("Tweeter")
  menu = input("1: Add Tweet\n2: View Tweets\n> ")
  if menu == "1":
    addTweet()
  else:
    viewTweet()
  answer = input("Wanna go again? ")
  if answer.strip().lower()[0] == "y":
    continue
  else:
    break

# Private Diary
def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}: {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.strip().lower()[0]=="e"):
      break

password = input("Password: ")
if password != "baldy1":
  print("Incorrect")
  exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
  answer = input("Wanna go again? ")
  if answer.strip().lower()[0] == "y":
    continue
  else:
    break
    
# Multiple Files
"""By now, you have written some pretty big programs with lots of lines of code. This can get pretty cumbersome to deal with. Lots of scrolling to find the right bit... One of the ways to overcome this is to split the code into multiple files."""
import test as tt 
print("Countdown")
tt.countdown() # Test refers to the file, countdown to the subroutine in that file.

# OOP
"""Object Oriented Programming (OOP) is a programming paradigm (a way of thinking about how to solve a problem) that is based on classes and objects, which store all of their data and behaviors inside them.
You can think of a class like a cookie cutter, or template. It has pre-defined characteristics (shape, size etc).
Instantiation means 'use the template to create an object'. Like pressing the cutter into the dough to make a cookie."""
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics
  # El nombre __init__ significa que esté código será recorrido tan pronto la clase esté incluida

  def __init__(self, name, species, sound):# self está siempre porque se refiere al objeto en sí, no a una variable
    self.name = name
    self.species = species
    self.sound = sound
  # Constructor used to set the object parameters
  def talk(self):
    print((f"{self.name} says {self.sound}")) 
  # 'self' means 'use the identifier given to the object that is accessing this method'. So If I use it with dog it will become 'dog.talk()' etc.

class bird(animal):
  def __init__(self, color):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class

    # This automatically sets the information for each bird when it is created.
polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk() # polly uses the `talk()` method from the animal class
print(polly.color) # Prints polly's color
dog = animal("Brian", "Canine", "Woof")
print(dog.name)
cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
"""Subrutinas dentro de objetos se llaman métodos"""
dog = animal("Brian", "Canine", "Woof")
dog.talk()
cow = animal("Ermintrude", "Bo Taurus", "Moo")
cow.talk()
"""------------------------------"""
class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    self.name = "Teacher"
    self.hoursWorked = hoursWorked
    self.salary = salary
    self.subject = subject
    self.position = position
  
  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()
doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()
teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()

# Character Creation
class character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

ian = player("Ian the mighty")
ian.print()
print(ian.isAlive())

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

eric = vampire(False)
eric.print()

# GUI (Graphical User Interface)
"""tkinter is one of the most popular Python GUI libraries."""
import tkinter as tk

def updateLabel():
  global label # Uses the values in the label variable
  label += 1 # Adds one to the value in the label
  hello["text"] = label 
  # Subroutine that updates the text in the label.

window = tk.Tk()
window.title("Hello World") # Sets the name of the window in the border
window.geometry("300x300") # Sets the size of the window in pixels

label = "Hey there world"
hello = tk.Label(text = label) # Creates a text box
hello.pack() # 'pack' places the element on the screen

label = 0
button = tk.Button(text = "Click me!", command = updateLabel) # Calls the updateLabel subroutine when the button is clicked
button.pack()

text = tk.Text(window ,height=1, width = 40)
# Three arguments, name of the window to place the text box in, height & width.
text.pack()
tk.mainloop()
"""----------------------------------"""
window = tk.Tk()
window.title("Calculator")
window.geometry("400x200")

answer = 0
lastNumber = 0
operator = None

def typeAnswer(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer

def calcAnswer(thisOp):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if thisOp == "+":
    operator = "+"
  elif thisOp == "-":
    operator = "-"
  elif thisOp == "*":
    operator = "*"
  elif thisOp == "/":
    operator = "/"
  hello["text"] = answer

def calc():
  global answer, lastNumber, operator
  print(f"{lastNumber}\t{answer}\t{operator}")
  if operator =="+":
    total = lastNumber + answer
  elif operator =="-":
    total = lastNumber - answer
  elif operator =="*":
    total = lastNumber * answer
  elif operator =="/":
    total = lastNumber / answer
  answer = total
  hello["text"] = answer

hello = tk.Label(text=answer)
hello.grid(row=0, column=1)

one = tk.Button(text="1", command= lambda: typeAnswer(1))
one.grid(row=1,column=0)

two = tk.Button(text="2", command= lambda: typeAnswer(2))
two.grid(row=1,column=1)

three = tk.Button(text="3", command= lambda: typeAnswer(3))
three.grid(row=1,column=2)

four = tk.Button(text="4", command= lambda: typeAnswer(4))
four.grid(row=2,column=0)

five = tk.Button(text="5", command= lambda: typeAnswer(5))
five.grid(row=2,column=1)

six = tk.Button(text="6", command= lambda: typeAnswer(6))
six.grid(row=2,column=2)

seven = tk.Button(text="7", command= lambda: typeAnswer(7))
seven.grid(row=3,column=0)

eight = tk.Button(text="8", command= lambda: typeAnswer(8))
eight.grid(row=3,column=1)

nine = tk.Button(text="9", command= lambda: typeAnswer(9))
nine.grid(row=3,column=2)

zero = tk.Button(text="0", command= lambda: typeAnswer(0))
zero.grid(row=4,column=1)

add = tk.Button(text="+", command= lambda: calcAnswer("+"))
add.grid(row=1,column=4)

minus = tk.Button(text="-", command= lambda: calcAnswer("-"))
minus.grid(row=1,column=5)

multiply = tk.Button(text="*", command= lambda: calcAnswer("*"))
multiply.grid(row=2,column=4)

divide = tk.Button(text="/", command= lambda: calcAnswer("/"))
divide.grid(row=2,column=5)

equals = tk.Button(text="=", command=calc)
equals.grid(row=4,column=4)
tk.mainloop()
