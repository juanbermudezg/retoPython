"""
Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.
Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.
Nombre(s)
Apellidos
Número de teléfono
Correo electrónico.
Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:
Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico .
Envía tu respuesta al primer reto aquí
Resuelto por @juanbermudezg https://github.com/juanbermudezg
"""
import re
from os import system
def formatText(text):
    text = " ".join(text.split())
    text=text.capitalize()
    return text
def isValidEmail(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False
def isValidCellphone(number):
    bandera = True
    for i in number:
        if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 43:
            pass
        else:
           bandera = False
    return bandera   
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
print("Hola bienvenido al primer reto de Código facilito.")
name = input('Escriba su nombre: ')
name= formatText(name)
surname = input('Escriba su apellido: ')
surname= formatText(surname)
cellphone = input('Escriba su número celular indicando el código del pais <+573142796777>: ')
while (not isValidCellphone(cellphone)):
    system("cls")
    print("Lo siento, no es un número celular válido")
    cellphone = input('Escriba su número celular indicando el código del pais <+573142796777>: ')
email = input('Ahora su correo electrónico: ')
while (not isValidEmail(email)):
    system("cls")
    print("Lo siento, no es un correo válido")
    email = input('Ahora su correo electrónico: ')
print("Hola",name,surname,"en breve recibirás un correo a", email,".")