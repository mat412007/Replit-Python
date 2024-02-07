# Auto Save and Auto Load
""" It's easy to access, amend, or remove a piece of data held in a list (in the RAM). Holding data in secondary storage in a file makes this more difficult. Or so you thought."""
import os, time
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
try: # All the code that should work goes inside the try
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
except Exception as err: # We can tell except what type of error(s) to look for. Exception (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is.
  print("ERROR: Unable to load")
  print(err) 
myStuff = []
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
    print('traceback') # Imprime el error en rojo de forma especifica
for row in myStuff:
  print(row)
"""-----------"""
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

pizza = []
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
