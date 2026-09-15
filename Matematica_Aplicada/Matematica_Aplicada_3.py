import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

##Problema 1
#Problema 1.1

# def r(x):
#     return -1.5*x**2+11.5*x-15

# def g(x):
#     return 1.58*x**4-19.17*x**3+80.92*x**2-139.33*x+85

# x = np.arange(0, 6, 0.01)
# plt.plot(x, r(x), label = 'r(x)')
# plt.plot(x, g(x), label = 'g(x)')
# plt.title('Nombre del gráfico')
# plt.ylabel('Nombre eje y')
# plt.xlabel('Nombre eje x')
# plt.xlim(0,6)
# plt.ylim(-10,10)
# plt.grid(True)
# plt.legend()
# plt.show()

#Problema 1.2

# def f(x):
#     return r(x) - g(x)

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(0, 6, 6)
# solucion = np.around(fsolve(f, xo),3)
# valores = np.unique(solucion)
# print(f"Los puntos de einterseccion entre las dos funciones ocurren cuando x ttoma los valores de {valores}")


##Problema 2
#Problema 2.1

# def h(x):
#     return 2*(x-2)**2

# def i(x):
#     return x-1

# x = np.arange(-3, 10, 0.01)
# plt.plot(x, h(x), label = 'h(x)')
# plt.plot(x, i(x), label = 'i(x)')
# plt.title('Nombre del gráfico')
# plt.ylabel('Nombre eje y')
# plt.xlabel('Nombre eje x')
# plt.legend()
# plt.show()

#Problema 2.2

#Valor/es inicial/es de la aproximación
# xo = np.linspace(-2, 0, 1)
# solucion = fsolve(i, xo)

# print(f"Las funciones h(x) intersecta al eje x cuando x es igual a {solucion[0]:.0f}")

# xo = np.linspace(0, 4, 1)
# solucion = fsolve(h, xo)

# print(f"Las funciones i(x) intersecta al eje x cuando x es igual a {solucion[0]:.0f}")

#Problema 2.3

# def f(x):
#     return h(x) - i(x)

# xo = np.linspace(0, 4, 2)
# solucion = np.around(fsolve(f, xo),3)
# valores = np.unique(solucion)
# print(f"Las funciones se intersectan cuando los valores de x son: {valores}")

#Problema 2.4

#La funcion h(x) es menor o igual a la funcion i(x) cuando x toma valores desde 1 hasta 3.5

#Problema 2.5

# def h(x):
#     return 2*(x-2)**2-50

# xo = np.linspace(-10, 10, 2)
# solucion = fsolve(h, xo)
# print(f"h(x) es igual a 50 cuando x es igual a {solucion}")



##Problema 4
#problema 4.1

#1960 es equivalente al valor de x=0 y 2023 es equivalente al valor de x=63

#problema 4.2

def C(x):
    return 19493*np.exp(0.01*x)

def E(x):
    return 17575*np.exp(0.012*x)

def H(x):
    return 10117*np.exp(0.015*x)

# x = np.arange(0, 150, 0.01)
# plt.plot(x, C(x), label = 'Chile')
# plt.plot(x, E(x), label = 'Ecuador')
# plt.plot(x, H(x), label = 'Honduras')
# plt.title('Crecimiento poblacional en diferentes paises segun el tiempo transcurrido desde 1960 hasta 2023')
# plt.ylabel('Poblacion (Miles)')
# plt.xlabel('Tiempo transcurrido (Años)')
# plt.legend()
# plt.show()

#problema 4.3

# print(f"La poblacion de cada pais en 1960 son las siguientes: Chile {C(0)}, Honduras {H(0)} y Ecuador {E(0)}")

#problema 4.4

# print(f"La poblacion de cada pais en 2000 son las siguientes: Chile {C(40):.3f}, Honduras {H(40):.3f} y Ecuador {E(40):.3f}")

#problema 4.5

# def f(x):
#     return C(x) - E(x)

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(130, 140, 1)
# solucion = fsolve(f, xo)
# print(f"A partir del año {solucion} la poblacion de Ecuador superara a la de Chile")

# #problema 4.6

# def f(x):
#     return C(x) - H(x)

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(130, 140, 1)
# solucion = fsolve(f, xo)
# print(f"En el año {solucion} la poblacion de Chile y Honduras es la misma")

##Problema 5
#Problema 5.1

#El ingreso por ventas inicial es de 1 millon de pesos y va disminuyendo en 20 miles de pesos por semana.
#El costo de inversion inicial es de 500 miles de pesos y va aumentando en 200 miles de pesos por semana.

#Problema 5.2

# def I(x):
#     return -20*x+1000

# def C(x):
#     return 200*x+500

# x = np.arange(0, 10, 0.01)
# plt.plot(x, I(x), label = 'Ingreso')
# plt.plot(x, C(x), label = 'Costo')
# plt.title('Relacion entre ingreso y costo segun tiempo transcurrido')
# plt.ylabel('Dinero (Miles de pesos)')
# plt.xlabel('Tiempo en semanas')
# plt.legend()
# plt.grid(True)
# plt.show()

#Problema 5.3

# def f(x):
#     return I(x) - C(x)

# #Valor/es inicial/es de la aproximación
# xo = np.linspace(2, 4, 1)
# solucion = fsolve(f, xo)

# print(f"La cordenada x del punto de equilibrio es de {solucion[0]:.2f}.")
# print(f"La cordenada y del punto de equilibrio es de {I(solucion[0])}")

#El punto de equilibrio es (2.27 , 954.55) aproximadamente.

#Problema 5.4

#En la semana 5 no conviene mantener la campaña, ya que los costos son mas altos que los ingresos. 
#En general, conviene mantener la campaña hasta las 2.27 semanas.
