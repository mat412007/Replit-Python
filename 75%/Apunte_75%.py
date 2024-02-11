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
  
# 
