# libraries random, os, time -
# random.randint() random.choice() -
# os.system("clear") -
# time.sleep(2) -
# print(, end="" sep="") -
# format strings -
# (f"{title:^35}") left <, right >, center ^ -
# lists -
# in  not in
# len() .append() .remove() .sort()
# .lower() .upper() .title() .capitalize() .strip() -
# myString[0:6:2]
# split() -
# '\033[?25l' '\033[?25h'
"""
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()
first = all[0].strip()  
last = all[1].strip() 
maiden = all[2].strip() 
city = all[3].strip() 
"""
# dictionaries
# .values() .keys() .items() 
# list()
# 2D Lists
# global
# 2D Dictionaries
# Files
"""
for key, value in clue.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
"""
"""
open("savedFile.txt", "w")
f.write("Hello there")
"""
"""
f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
"""
"""
f = open("filenames.list", "r")
contents = f.read()
contents = contents.split()
print(contents)
contents = f.readline().strip()
print(contents)
f.close()
"""

import random, os, time
while True:
  print("Welcome to the summary of the 50% of the course!!!\n")
  go = input("Do you wanna access it? (y / n)\n")
  if go[0].strip().lower() != "y":
    break
  time.sleep(1)
  print()
  name = input("What's your name? ")
  age = input("How old are you? ")
  home = input("Where are you from? ")
  print(f"\nOk, so you are {name}, you are {age} years old, and you live in {home}", end="")
  time.sleep(1)
  print("\n")
  while True:
    print(f"{'Lotto!':>30}")
    print("Let's test your luck\nWe are gonna play Lotto!\n")
    lottery = ["Regular", "Good", "Very Good", "Excellent"]
    lottery1 = lottery[random.randint(0,3)]
    lottery2 = random.choice(lottery)
    lottery3 = random.choice("Regular Good Very Good Excellent".split())
    print(f"{lottery1}\t{lottery2}\t{lottery3}\n")
    if lottery1 == lottery2 and lottery2 == lottery3:
      print("Looks like luck is on your side")
    elif lottery1 == lottery2 and lottery2 != lottery3 or lottery2 == lottery3 and lottery1 != lottery2 or lottery1 == lottery3 and lottery2 != lottery3:
      print("Not bad, not bad at all")
    else:
      print("What a terrible luck you have")
    answer = input("Wanna add another beast? ")
    if answer == "yes":
      continue
    else:
      break
  print()
  print("Now let's try with a To Do List")
  while True:
    print(f"{'ToDoList':>30}")
    ToDoList = []
    procedure = input("Would you like to add, remove, edit or delete the list? ")
    if procedure.strip().lower() == "a":
      toDo = input("What would you like to add?\n")
      if toDo not in ToDoList:
        ToDoList.append(toDo)
        print("Added")
      elif toDo in ToDoList:
        print("This is already on the list")
    elif procedure.strip().lower() == "r":
      toDo = input("What would you like to remove?\n")
      if toDo not in ToDoList:
        print("Unfortunately this is not on the list")
      elif toDo in ToDoList:
        ToDoList.remove(toDo)
        print("Removed")
    elif procedure.strip().lower() == "d":
        ToDoList = []
        print("All cleared")
    elif procedure.strip().lower() == "e":
      toDo = input("What would you like to change?\n")
      print()
      change = input("What would you like to insert instead?\n")
      for edit in ToDoList:
        if edit == toDo:
          edit = change
      print("All done")
    answer = input("Wanna add another beast? ")
    if answer == "yes":
      continue
    else:
      break



  again = input("Do you wanna go again? (y / n)\n")
  if again[0].strip().lower() == "y":
    os.system("clear")
    continue
