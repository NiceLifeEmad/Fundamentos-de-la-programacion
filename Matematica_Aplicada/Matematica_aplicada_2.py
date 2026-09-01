import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# def suma(x):
#     return 14*x+35

# resultado = suma(18)

# print (resultado)


## GUIA 2

#Problema 1.1

# Variable dependiente = Tiempo de ejecucion (ms)
# Variable independiente = Cant. de elementos (Unidades)

#Problema 1.2

# x = np.array([100, 200, 500, 1000, 2000])
# y = np.array([2, 4, 10, 20, 40])
# #Si la función es de grado 1
# pendiente, intercepto = np.polyfit(x, y, 1)

# print(f"f(x)= {pendiente.round(2)}x + {intercepto.round(2)}")


#Problema 1.3

# def suma(x):
#      return 0.02*x

# resultado = suma(1500)

# print (f"El tiempo de ejecucion con una cantidad de 1500 elementos es de {resultado} ms")

#Problema 1.4

# def f(m):
#     return 0.02*m-50

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 5000, 1)
# solucion = fsolve(f, xo)

# print(f"Para que el tiempo de ejecucion sea de 50 ms, tienen que considerar {solucion[0]} elementos.")

## Problema 2

#Problema 2.1

# Variable dependiente: Tiempo de transferencia (Min)
# Variable independiente: Datos transferidos (GB)

#Problema 2.2

# x = np.array([5, 10, 25, 50, 100])
# y = np.array([10, 20, 50, 100, 200])
# #Si la función es de grado 1
# pendiente, intercepto = np.polyfit(x, y, 1)

# print(f"f(x)= {pendiente.round(2)}x + {intercepto.round(2)}")

#Problema 2.3

#La pendiente es igual a 2, lo que significa que por cada Gigabyte que pesa el archivo, 
#la cantidad de minutos necesarios para transferirlo aumenta en dos

#Problema 2.4

# def f(g):
#     return 2*g

# resultado = f(73.2)

# print (resultado)

#Problema 2.5

# def f(l):
#     return 2*l-123.5

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 500, 1)
# solucion = fsolve(f, xo)

# print(f"Para que se transfieran 123.5 GB, tienen que pasar {solucion[0]} minutos.")

#Problema 2.6

# def f(x):
#     return 2*x

# x = np.arange(0, 100, 0.01)
# plt.plot(x, f(x), label = 'f(x)')
# plt.title('Relacion entre tiempo y datos de transferencia')
# plt.ylabel('Tiempo de transferencia (Min)')
# plt.xlabel('Datos de transferencia (GB)')
# plt.legend()
# plt.show()





#Problema 4.1

# Variable dependiente: Uso de memoria (GB)
# Variable independiente: Numero de usuarios activos (Unidades)

#Problema 4.2

#La pendiente es 0.5 y significa que por cada usuario el uso de memoria aumenta en 0.5

#Problema 4.3

#El servidor usa 2 GB de memoria cuando no hay usuarios activos

#Problema 4.4

def suma(x):
    return 0.5*x+2

# resultado = suma(637)

# print (f"Se usan {resultado} GB cuando hay 637 usuarios activos")

#Problema 4.5

def f(y):
    return 0.5*y+2-32

#Valor/es inicial/es de la aproximación
xo = np.linspace(0, 50, 1)
solucion = fsolve(f, xo)

print(f"Para usar 32 GB de memori9a debe haber {solucion} usuarios activos")

#Problema 4.6

def f(y):
    return 0.5*y+2-59.8

#Valor/es inicial/es de la aproximación
xo = np.linspace(0, 50, 1)
solucion = fsolve(f, xo)

print(f"No, porque para que hubiesen 59.8 GB de uso en el servidor, deberian haber {solucion} usuarios, lo cual no es posible")
