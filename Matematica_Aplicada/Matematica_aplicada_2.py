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

##Problema 3
#Problema 3.1

# x = np.array([50, 100, 250, 500, 1000])
# y1 = np.array([10, 20, 50, 100, 200])
# y2 = np.array([8, 16, 40, 80, 160])
# #Si la función es de grado 1
# pendiente1, intercepto1 = np.polyfit(x, y1, 1)
# pendiente2, intercepto2 = np.polyfit(x, y2, 1)

# print(f"f(x)= {pendiente1.round(2)}x + {intercepto1.round(2)}")
# print(f"f(x)= {pendiente2.round(2)}x + {intercepto2.round(2)}")

#f(x)=0.2x  // Tiempo de Carga
#g(x)=0.16x // Tiempo de Descarga

#Problema 3.2

# Variable dependiente: Tiempo de carga (s) y Tiempo de descarga (s)
# Variable independiente: Tamaño del archivo (MB)

#Problema 3.3

# def f(x):
#     return 0.2*x

# def g(x):
#     return 0.16*x

# print (f"Para un archivo de 750 Mb, el tiempo de carga es {f(750)} segundos y el tiempo de descarga es {g(750)} segundos ")

#Problema 3.4

# def f(x):
#     return 0.2*x-163

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 200, 1)
# solucion = fsolve(f, xo)

# print(f"Si el tiempo de carga es de 163 segundos, el tamaño del archivo debe ser {solucion} Mb")

#Problema 3.5

# def f(x):
#     return 0.16*x-195

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 200, 1)
# solucion = fsolve(f, xo)

# print(f"Si el tiempo de descarga es de 195 segundos, el tamaño del archivo debe ser {solucion} Mb")

#Problema 3.6

# def f(x):
#     return 0.2*x

# def g(y):
#     return 0.16*y

# x = np.arange(0, 1500, 0.01)
# y = np.arange(0, 1500, 0.01)
# plt.plot(x, f(x), label = 'Tiempo de Carga (Mb)')
# plt.plot(y, g(y), label = 'Tiempo de Descarga (Mb)')
# plt.title('Velocidad de Carga y Descarga en relacion al tamaño del archivo')
# plt.ylabel('Tiempo transcurrido (s)')
# plt.xlabel('Tamaño del Archivo (Mb)')
# plt.legend()
# plt.show()

##Problema 4
#Problema 4.1

# Variable dependiente: Uso de memoria (GB)
# Variable independiente: Numero de usuarios activos (Unidades)

#Problema 4.2

#La pendiente es 0.5 y significa que por cada usuario el uso de memoria aumenta en 0.5

#Problema 4.3

#El servidor usa 2 GB de memoria cuando no hay usuarios activos

#Problema 4.4

# def suma(x):
#     return 0.5*x+2

# # resultado = suma(637)

# # print (f"Se usan {resultado} GB cuando hay 637 usuarios activos")

# #Problema 4.5

# def f(y):
#     return 0.5*y+2-32

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 50, 1)
# solucion = fsolve(f, xo)

# print(f"Para usar 32 GB de memori9a debe haber {solucion} usuarios activos")

# #Problema 4.6

# def f(y):
#     return 0.5*y+2-59.8

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 50, 1)
# solucion = fsolve(f, xo)

# print(f"No, porque para que hubiesen 59.8 GB de uso en el servidor, deberian haber {solucion} usuarios, lo cual no es posible")

##Problema 7
#Problema 7.1

# Variable dependiente: Valor residual (Miles de dolares)
# Variable independiente: Antiguedad (Años)

#Problema 7.2

#En cuanto varia el valor residual a medida que pasan los años, siendo la pendiente igual a: -1.2

#Problema 7.3

# Es igual a 10.000 dolares, dado que N es igual a 10

#Problema 7.4

# El dominio contextualizado es de: 0 a 8 años

#Problema 7.5

# def f(x):
#     return -1.2*x+10

# print(f"El valor del equipo residual con 3 años y seis meses de antiguedad es de {f(3.5)} miles de dolares")

#Problema 7.6

# def f(x):
#     return -1.2*x+10-4000

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 5000, 1)
# solucion = fsolve(f, xo)

# print(solucion)

#Problema 7.7

# def f(x):
#     return -1.2*x+10

# x = np.arange(0, 100, 0.01)
# plt.plot(x, f(x), label = 'f(x)')
# plt.title('Valor residual del equipo')
# plt.ylabel('Valor residual (Miles de dolares)')
# plt.xlabel('Tiempo transcurrido (Años)')
# plt.legend()
# plt.show()


##Problema 8
#Problema 8.1

# x = np.array([0, 20, 40, 60, 80])
# y = np.array([2, 3, 4, 5, 6])
# #Si la función es de grado 1
# pendiente, intercepto = np.polyfit(x, y, 1)

# print (f"T(x)= {pendiente:.2f}x + {intercepto:.2f}")

# #Problema 8.2

# def f(x):
#     return 0.05*x+2

#Problema 8.3


##Problema 10
#Problema 10.1

#Atleta 1
# def f(x):
#     return 0.7*x**2

# #Atleta 2
# def g(y):
#     return 10*y

# x = np.arange(0, 10, 0.01)
# y = np.arange(0, 10, 0.01)
# plt.plot(x, f(x), label = 'Atleta 1')
# plt.plot(y, g(y), label = 'Atleta 2')
# plt.title('Relacion entre distancia recorrida y el tiempo transcurrido')
# plt.ylabel('Distancia recorrida (Metros)')
# plt.xlabel('Tiempo Transcurrido (Seg)')
# plt.legend()
# plt.show()

#El atleta 2 mantuvo una velocidad constante en aumento

#Problema 10.2

#El atleta 2 segun lo observado en el grafico llego a los 100 metros tras 10 segundos

#Problema 10.3

# distancia8= g(8) - f(8)

# distancia10= g(10) - f(10)

# print(f"A los 8 segundos se encontraban a {distancia8} m de distancia")
# print(f"A los 10 segundos se encontraban a {distancia10} m de distancia")

#Problema 10.4

# distancia = f(10)-f(8)

# velocidad= distancia/2

# print(f"El atleta 1 tenia una velocidad de {velocidad} m/s entre los 8 y 10 segundos")

#El atleta 1 iba mas rapido, con una velocidad de 12.6 m/s, mientras que el atleta 2 tenia una velocidad de 10 m/s


##Problema 11
#Problema 11.1

#Empresa 1
# def f(x):
#     return 12*x+50

# #Empresa 2
# def g(y):
#     return 8*y+100

# x = np.arange(0, 50, 0.01)
# y = np.arange(0, 50, 0.01)
# plt.plot(x, f(x), label = 'Empresa 1')
# plt.plot(y, g(y), label = 'Empresa 2')
# plt.title('Relacion entre el costo de desarrollo y el tiempo de desarrollo')
# plt.ylabel('Costo de desarrollo (Millones de pesos)')
# plt.xlabel('Tiempo de desarrollo (Semanas)')
# plt.legend()
# plt.show()

#Problema 11.2

# def f(x):
#     return 12*x+50-155

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 20, 1)
# solucion = fsolve(f, xo)

# print(f"Pagando 155 millones a la empresa 1 el proyecto tardara {solucion} semanas")

#Problema 11.3

#Si el proyecto demorara menos de 12.5, la empresa 1 es mejor, en caso contrario, la empresa 2 es mejor
