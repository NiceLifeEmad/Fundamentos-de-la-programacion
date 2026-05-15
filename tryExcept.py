## Para evitar que se pierdan los datos ingresados
## se puede añadir else y finally, si no se usa except ocure else y finally ocurre siempre
##Tipos de errores:
## ZeroDivisionError
## TypeError 
## ValueError
## FileNotFoundError
## SyntaxError

# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except:
#         print("Solo numeros enteros")

# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV 55 pulgadas $450.000")
#         print("3.- Microondas Mademsa $100.000")
#         print("4.- Salir")
#         print("Seleccione una opcion")
#         op=int(input())
#     except:
#         print("Solo se acceptan numeros enteros")
#         match op:
#             case 1:
#                 print("El total a pagar es ",500000*1.19 )
#                 total+=500000*1.19
#             case 2:
#                 print("El total a pagar es ",450000*1.19 )
#                 total+=450000*1.19
#             case 3:
#                 print("El total a pagar es ",100000*1.19 )
#                 total+=100000*1.19
#             case 4:
#                 print("Saliendo")
#                 print("El total a pagar es", total)
#             case _:
#                 print("Opción inválida")


# explicacion y uso de FOR

# for i in range(5):
#     print(i+1)

# num=int(input("Ingrese un numero"))
# for i in range(1,num+1):
#     print("Repeticion", i)

# for i in range(num):
#     print("Repeticion", i+1)

# pedir un numero al usuario y mostrar
# su tabla de multiplicar

# num=int(input("Ingrese un numero"))

# for i in range(1,11):
#     print(f"{num}x{1}={num*i}")

# Pedir al usuario la cantidad d notas 
# mostrar el premedio de ellas
# determinar si el alumno aprueba o no
# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas: "))
#         break
#     except:
#         print("Solo numeros enteros")
#     suma=0
# for i in range(notas):
#     while True:
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             if 1<=n<=7:
#                 print("Nota fuera de rango, (1.0-7.0)")
#             suma=suma+n
#             # suma+=n
#             break
#         except:
#             print("Ingrese solo numeros enteros")

# prom=suma/notas
# print("El promedio es",round(prom,1) )

# if prom>=4:
#     print("Alumno aprobado")
# else:
#     print("Alumno reprobado")