# Explicacion y uso de "for"

# for i in range(7):
#     print("hola")

# num=int(input("Ingrese un numero: "))

# for i in range(num):
#      print(i+1, "repeticion")
# print("segunda forma")
# for i in range(1,num+1):
#      print(i, "repeticion")


# Pedir un numero al usuario y mostrar su tabla de multiplicar

# num=int(input("Ingrese un numero: "))

# #primera forma
# for i in range(10):
#       print(num, "x", i, "=", num*i)

# #con manipulacion de limites
# num=int(input("Ingrese un numero: "))

# for i in range(1,11):
#       print(num, "x", i, "=", num*i)

# #usando f string
# num=int(input("Ingrese un numero: "))

# for i in range(1,11):
#       print(f"{num}x{i}={num*i})

# titulo="clima de hoy" #string letras
# diaDelMes=17  #int numeros enteros
# mes=4 #int numeros enteros
# tem=25.7  #float numeros decimales
# llueve=True  #boolean verdadero o falso
# print(titulo, "temperatura: ", tem,diaDelMes,"/",mes)
# print(f"{titulo} temperatura: {tem} {diaDelMes}/{mes}")

# EJ
# tem>28 ------->False
# mes==4 ------>True

# if llueve:
#     print("Saca el paraguas")
# else:
#     print("Puede andar en polera") 



#Preguntar cuantas notas son y
#sacar el promedio de ellas

# notas=int(input("Cuantas notas son?: "))
# prom=0
# for i in range(notas):
#        print("Ingrese una nota: ")
#        sumN=float(input())
#        prom=sumN+prom
#     #    print(prom)

# print("El promedio es:", round((prom/notas),1))

#sumatoria
# sumatoria=int(input("Ingreas un numero: "))
# total=0
# for i in range(sumatoria):
#        total=total+i+1
# print("La sumatoria es: ", total)


#Factorial

# sumatoria=int(input("Ingreas un numero: "))
# total=1
# for i in range(sumatoria):
#        total=total*(i+1)
# print("La sumatoria es: ", total)

#Usando string en vez de numeros
# for i in "Vicente":
#     print(i)

# letras=0
# nombre=input("Ingrese su nombre: ")
# for i in nombre:
#     print(i)
#     letras=letras+1
# print(f"El total de letras es {letras}")


#Contador de vocales y consonantes
# vocales=0
# conso=0
# nombre=input("Ingrese su nombre: ")
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#     elif i ==" ":
#         ''''''
#     else:
#         conso+=1

# print(f"El total de vocales es {vocales}")
# print(f"El total de consonantes es {conso}")

#Cada letra desde la izquierda a la derecha partiendo desde 0 tiene un indice con valor numerico, 
#esto mismo se aplica con numeros negativos pero desde la derecha a la izquierda
# n=" Calonia"
# name= "Alonso Robles"
# print(name[0])
# print(len(name)) #Muestra la cantdad de letras
# print(n.strip()) #Ignora los espacios al inicio y final
# print(name.upper()) #Solo visuyaliza
# name=name.upper() #Cambia las leltras a mayuscula
# print(name.lower()) #Solo visualiza
# name=name.lower() #Cambia las letras a minuscula
# print(name.replace("Robles", "Parra")) #Solo visualiza
# name=name.replace("Robles", "Parra") #Reemplaza un valor por otro