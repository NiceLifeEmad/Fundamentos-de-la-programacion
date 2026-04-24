#Uso y explicacion de match(Menu)

# print("1.- Opcion 1")
# print("2.- Opcion 2")
# print("3.- Opcion 3")
# op=int(input("Selecione una opcion: "))
# match op:
#     case 1:
#         print("Selecciono la opcion 1")
#     case 2:
#         print("Selecciono la opcion 2")
#     case 3:
#         print("Selecciono la opcion 3")
#     case _:
#         print("Opcion invalida")
    
# op=0
# total=0
# while op!=4:
#     print("1.- Xbox Series S $250.000")
#     print("2.- Sony PS5 $500.000")
#     print("3.- LGTV 60 Pulgadas $600.000")
#     print("4.- Salir")
#     op=int(input("Selecione una opcion: "))
#     match op:
#         case 1:
#             print ("El valor a pagar es ", 250000*1.19)
#             total+=250000*1.19
#         case 2:
#             print ("El valor a pagar es ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print ("El valor a pagar es ", 600000*1.19)
#             total+=600000*1.19
#         case 4:
#             print ("Saliendo")
#             print(f"El total a pagar es {total}")
#         case _:
#             print ("Opcion invalida")



##Calculadora (+ - * /)


def suma():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1+num2}")   

def resta():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1-num2}")  

def multiplicacion():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1*num2}")    

def division():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    print(f"El resultado es {num1/num2}")   

# op=0

# while op!=5:
#     print("Que operacion desea realizar?")
#     print("1.- Suma")
#     print("2.- Resta")
#     print("3.- Multiplicacion")
#     print("4.- Division")
#     print("5.- Salir")
#     op=int(input("Selecione una opcion: "))
#     match op:
#         case 1:
#             suma()  
#         case 2:
#             resta()  
#         case 3:
#             multiplicacion()  
#         case 4:
#             division()
#         case 5:
#             print ("Saliendo")
#         case _:
#             print ("Opcion invalida")


#Buscar 3 programas en python
#y crearlos como funcion
#llamarlos como funcion

def votatoon():
    can1=(input("Ingrese el candidato numero 1: "))
    can2=(input("Ingrese el candidato numero 2: "))
    votantes=int(input("Ingrese el numero de votantes: "))
    vcan1=0
    vcan2=0

    for i in range (votantes):
        voto=int(input(f"Por quien desea votar, 1. el candidato {can1} 2. el candidato {can2}? "))
    if voto==1:
        vcan1=vcan1+1
    elif voto==2:
        vcan2=vcan2+1
    else:
        print("Voto nulo")

    if vcan1>vcan2:
        print(f"Tras contar los votos, el ganador es: {can1} con {vcan1} votos")
    elif vcan2>vcan1:
        print(f"Tras contar los votos, el ganador es: {can2} con {vcan2} votos")
    else:
        print(f"Ha habido un empate entre ambos candidatos con un total de {vcan1} para {can1} y {vcan2} para {can2}")

# votatoon()

def PIN():
    pin=3232
    baka=int(input("Ingrese su pin"))
    while pin!=baka:
        print("Pin Incorrecto")
    baka=int(input("Ingrese su pin"))
    print("PIN correcto")

# PIN()

def promedio():
    notas=int(input("Cuantas notas son?: "))
    prom=0
    for i in range(notas):
       print("Ingrese una nota: ")
       sumN=float(input())
       prom=sumN+prom
    #    print(prom)

    print("El promedio es:", round((prom/notas),1))

# promedio()