## Uso y explicacion de random
import random
import time
# num=random.randint(1,10)
# time.sleep(1)
# print(num)

# for i in range (num):
#     print("Hola Vicente")

# for i in range(10):
#     print(f"{num}x{i}={num*i}")

# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la distancia varia entre 60 y 190 metros
# Mostrar al final, el golpe mas fuerte

# d1=random.randint(60,190)
# d2=random.randint(60,190)
# d3=random.randint(60,190)
# print(f"El jugador 1 golpea la pelota y llega a los {d1}")
# print(f"El jugador 2 golpea la pelota y llega a los {d2}")
# print(f"El jugador 3 golpea la pelota y llega a los {d3}")

# if d1>d2 and d1>d3:
#     print("El jugador 1 golpeo mas fuerte")
# elif d2>d1 and d2>d3:
#     print("El jugador 2 golpeo mas fuerte")
# elif d3>d1 and d3>d2:
#     print("El jugador 3 golpeo mas fuerte")
# else:
#     print("Todos los jugadores golpearon igual de fuerte")


# Tirar 2 dados

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"El dado dio {dado1}")
# print(f"El dado dio {dado2}")

# # Si los dados dan el mismo numero
# # El jugador va a la carcel

# if dado1==dado2:
#     print("El jugador va a la carcel")
# else:
#     print("Continue avanzando")

# PELEA

# F1=100
# F2=100


# while F1>0 and F2>0:
#     for i in range(1):
#         golpe=random.randint(7,18)
#         print(f"El jugador 1 tiene {F1} de HP y El jugador 2 tiene {F2} de HP")
#         print(f"El peleador 1 hace {golpe} de daño al jugador 2")
#         F2=F2-golpe
#         print(f"El jugador 1 tiene {F1} de HP y El jugador 2 tiene {F2} de HP")
#         print("Vida del jugador 1", "/"*F1, "Vida del jugador 2", '''
#         "/"*F2''')
#         golpe=random.randint(7,18)
#         time.sleep(3)
#         print(f"El jugador 1 tiene {F1} de HP y El jugador 2 tiene {F2} de HP")
#         print(f"El peleador 2 hace {golpe} de daño al jugador 1")
#         F1=F1-golpe
#         print(f"El jugador 1 tiene {F1} de HP y El jugador 2 tiene {F2} de HP")
#         time.sleep(3)

# if F1>F2:
#     print("El jugador 1 Gana")
# else:
#     print("El jugador 2 Gana")

# LUDO

# avance=0
# turnos=1
# while avance <=50:
#     dado1=random.randint(1,6)
#     dado2=random.randint(1,6)
#     avance=avance+(dado1+dado2)
#     print(f"El dado 1 dio {dado1}")
#     print(f"El dado 2 dio {dado2}")
#     print(f"El jugador avanza {dado1+dado2} casillas y se encuentra en la casilla {avance}")
#     turnos=turnos+1

# print(f"Tras {turnos} turnos, el jugador llega a la meta")

# Adivina el numero
# Crea un numero al azar entre el 1 y el 100
# Pide al usuario que adivine el numero
# Si el usuario ingresa un numero mayor al generado
# Colocar, te pasaste, en caso contrario
# El numero a adivinar es mayor
# Solo hay 5 oportunidades

num=random.randint(1,100)
intentos=5
while intentos>0:
    adivina=int(input("Ingrese un numero entre 1 y 100: "))
    if adivina<num:
        print("Te pasaste, intentos restantes: ", intentos-1)
        intentos-=1
    elif adivina>num:
        print("El numero es menor, intentos restantes: ", intentos-1)
        intentos-=1
    else:
        print("Has adivinado el numero")
        break
       

print("Se te acabaron los intentos, el numero era: ", num)



