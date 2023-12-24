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
    Black	    30
    Red	        31
    Green	    32
    Yellow	    33
    Blue	    34
    Purple	    35
    Cyan	    36
    White	    37
"""

# IF and ELSE 
"""Se usan para especificar condiciones, si la condición del if se cumple se ejecuta lo que este debajo, de lo contrario se ejecuta el else"""
myName = input("What's your name?: ")
if myName == "David":
    print("Welcome Dude!")
    print("You're just the baldest dude I've ever seen")
else:
    print("Who on earth are you?!")

