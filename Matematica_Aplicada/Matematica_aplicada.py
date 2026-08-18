## Problema 1
## Escribe un código que pida al usuario ingresar un número real y determine si el número ingresado es positivo, negativo o cero.

# num=float(input("Ingrese un numero real: "))

# if num>=1:
#     print("El numero es positivo")
# elif num<=-1:
#     print("El numero es negativo")
# else:
#     print("El numero es cero")


## Problema 2
## Escribe un código que pida al usuario ingresar un número entero y que determine si el número ingresado es par o impar.

# num=int(input("Ingrese un numero entero: "))

# if num % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

## Problema 3
## Escribe un código que, mediante un ciclo while, sume los primeros  100  números naturales.

# suma=0
# numero=1

# while numero<=100:
#     suma+= numero
#     numero += 1
# print("La suma de los 100 primeros numeros es", suma)

## Problema 4
## Escribe un código que almacene en una variable el string "Contraseña". 
## Luego, el programa debe solicitar al usuario "Introducir contraseña", hasta que la palabra ingresada sea correcta.

# contraseña=str(input("Ingrese una contraseña: "))

# contra=str(input("Introducir contraseña: "))

# while contra!=contraseña:
#     contra=str(input("Contraseña incorrecta, intente de nuevo: "))

# print("Contraseña correcta")

## Problema 5
## Escribe un código que, utilizando un ciclo for, pida al usuario ingresar un número entero 
## y muestre la tabla de multiplicar desde el 1 al 12 de dicho número

# num=int(input("Ingrese un numero entero: "))

# for i in range(12):
#     print(num, "x", i+1, "=", num * (i+1))

## Problema 6
## 1. Escribe una función que reciba dos números y retorne el producto de los números recibidos.
## 2. Escribe una nueva función que tome el producto calculado en el ítem anterior y redondee el valor al entero.
## 3. Pide al usuario que ingrese dos números, y utiliza ambas funciones para imprimir el valor de la multiplicación redondeado al entero.

# def producto(a, b):
#     return a*b

# def redondeo(a):
#     return round(a)

# n1=float(input("Ingrese un primer numero real: "))
# n2=float(input("Ingrese un segundo numero real: "))

# print(f"El resultado de la multiplicacion redondeada al entero es: {redondeo(producto(n1, n2))}")

## Problema 7
## Crear una funcion que que convierta celsius a farenheit redondeado a la centesima

def f(a):
    return (9/5)*a+32

c=float(input("Ingresa la temperatura en °C: "))
print(f"La temperatura en grados Farenheit es de {round(f(c),2)}")
