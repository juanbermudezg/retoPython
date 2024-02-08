"""
Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer.
Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema.
Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.
Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores:
Nombre, apellidos, número de teléfono y correo electrónico.
Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.
Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.
Así mismo el número de teléfono será a 10 dígitos.
Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que
se ingresen datos correctos.
Resuelto por @juanbermudezg https://github.com/juanbermudezg
"""
import re
from os import system

def formatText(text):
    text = " ".join(text.split())
    text=text.capitalize()
    return text
def isValidEmail(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
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
    if (len(number)>=10):
        pass
    else:
        bandera=False
    return bandera   
def isValidText(txt):
    text=formatText(txt)
    if (len(text)>=5 and len(text)<=50):
        return True
    else:
        return False
def saveUser():
    usuariosLista = []
    contador=0
    for i in range(cantidadUsuarios):
        name = input('Escriba su nombre: ')
        name = formatText(name)
        while(not isValidText(name)):
            system("cls")
            print("Lo siento, no cumple con los requisitos minimos")
            name = input('Escriba su nombre: ')
        surname = input('Escriba su apellido: ')
        surname = formatText(surname)
        while(not isValidText(surname)):
            system("cls")
            print("Lo siento, no cumple con los requisitos minimos")
            name = input('Escriba su apellido: ')
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
        usuario={
            'id':contador+1,
            'name': name,
            'surname': surname,
            'cellphone': cellphone,
            'email': email
        }
        usuariosLista.append(usuario)
        contador+=1
    return usuariosLista
print("Hola bienvenido al primer reto de Código facilito.")
cantidadUsuarios = int(input('Digite la cantidad de usuarios a registrar: '))
listaUsuarios = saveUser()
for i in range(len(listaUsuarios)):
    print("Hola",listaUsuarios[i]['name'],listaUsuarios[i]['surname'],"con ID",listaUsuarios[i]['id'],"en breve recibirás un correo a", listaUsuarios[i]['email']+".")
