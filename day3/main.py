"""
Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas
funcionalidades a nuestro programa de registro de usuarios.
Estas funcionalidades son las siguientes.
1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario.
Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos
los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.
Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.
Entrega tu ejercicio aquí
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
def showUsers(usersList):
    for i in range(len(listaUsuarios)):
        print("Hola",listaUsuarios[i]['name'],listaUsuarios[i]['surname'],"con ID",listaUsuarios[i]['id'],"en breve recibirás un correo a", listaUsuarios[i]['email']+".")
def showIDs(usersList):
    for i in range(len(listaUsuarios)):
        print("ID",listaUsuarios[i]['id'])
print("Hola bienvenido al primer reto de Código facilito.")
cantidadUsuarios = int(input('Digite la cantidad de usuarios a registrar: '))
listaUsuarios = saveUser()
bandera = True
while bandera == True:
    option = int(input('¿Quiere ver solo los usuarios <1> o el mensaje predeterminado de todos <2>?: '))
    if option == 1:
        showIDs(listaUsuarios)
        break
    elif option == 2:
        showUsers(listaUsuarios)
        break
    else:
        print('Mala eleccion')
        bandera = False
print("Gracias por usar el programa")