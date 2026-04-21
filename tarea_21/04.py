
# clave="SHAZAM"
# code=input("Ingrese la clave: ")
# if clave==code.upper:
#     print("Acceso concedido")
# else:
#     print("Clave invalida")
    
# user=input("Ingrese nombre de usuario: ")
# if len(user)<4:
#     print("Nombre de usuario posee menos de 4 caracteres")
# elif len(user)>10:
#     print("El nombre de usuario tiene mas de 10 caracteres")
# else:
#     print("Usuario creado con exito")

pin=int(input("Ingrese su pin: "))
#incorrecto
if len(pin)==4:
    print("PIN creado con exito")
else:
    print("PIN invalido")
#Forma correcta 1
if 1000<pin <9999:
    print("PIN creado con exito")
else:
    print("PIN invalido")
#Forma correcta 2
if len(str(pin))==4:
    print("PIN creado con exito")
else:
    print("PIN invalido")