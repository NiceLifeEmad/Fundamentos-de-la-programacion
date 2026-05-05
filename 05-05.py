##Loteria

import random
import time

# num1=random.randint(1,9)
# num2=random.randint(1,9)
# num3=random.randint(1,9)
# print(f"{num1} {num2} {num3}")

# numero1=random.randint(1,9)
# numero2=random.randint(1,9)
# numero3=random.randint(1,9)

# turnos=0

# while num1!=numero1 or num2!=numero2 or num3!=numero3:
#     numero1=random.randint(1,9)
#     numero2=random.randint(1,9)
#     numero3=random.randint(1,9)
#     turnos+=1
#     # print(f"{numero1} {numero2} {numero3}")

# if num1==numero1 and num2==numero2 and num3==numero3:
#     print("GANASTE!!!")
#     print(f"Tardaste {turnos} intentos en ganar")


## METODO DEL PROFE

# num1=random.randint(1,9)
# num2=random.randint(1,9)
# num3=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# nums=0
# print(f"Los numeros generados son {num1}, {num2} y {num3}")

# while not t1 or not t2 or not t3:
#     numerito=random.randint(1,9)
#     print("El numero es", numerito)
#     time.sleep(1)
#     if numerito==num1:
#         t1=True
#     if numerito==num2:
#         t2=True
#     if numerito==num3:
#         t3=True
#     nums+=1
# print(f"GANASTE, en {nums} turnos")


# gramos=int(input("Ingrese el peso en gramos del producto: "))
# while gramos<1:
#     print("ERROR,  ingrese solo numeros positivos")
#     gramos=int(input("Ingrese el peso en gramos del producto: "))
# sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
# while sodio<1 or sodio>100:
#     print("ERROR,  ingrese solo numeros posentre 1 y 100")
#     sodio=int(input("Ingrese el porcentaje de sodio del producto: "))
# venta=int(input("El producto se vendera 1.- Nacionalmente  2.- Internacionalmente? "))
# while venta!=1 and venta!=2:
#     print("Opcion invalida")
#     venta=int(input("El producto se vendera 1.- Nacionalmente  2.- Internacionalmente? "))

# l1="lata normal"
# l2="lata mediana"
# l3="lata grande"

# if gramos<500:
#     c1=l1
# elif gramos>=501 and gramos <=1500:
#     c1=l2
# else:
#     c1=l3

# s1="comun"
# s2="especial"
# s3="acorazada"


# if sodio<5:
#     c2=s1
# elif sodio<8 and sodio>5:
#     c2=s2
# else:
#     c2=s3

# v1="Nacional"
# v2="Internacional"

# if venta==1:
#     c3=v1
# else:
#     c3=v2


# print(f"Es una {c1}, con una lata {c2} y de venta {c3}")


pecesc=random.randint(10,20)
print(f"Se capturaron {pecesc}")

peces=pecesc
lata=0
tabla=0

while peces!=0:
    pez=random.randint(100,1600)
    print(f"El pez peso {pez} gramos")
    if pez<801:
        print("Se vendera en lata")
        peces-=1
        lata+=1
    else:
        print("Se vendera a la plancha")
        peces-=1
        tabla+=1

print(f"Se vendieron {lata} peces en lata y {tabla} peces en tabla")





