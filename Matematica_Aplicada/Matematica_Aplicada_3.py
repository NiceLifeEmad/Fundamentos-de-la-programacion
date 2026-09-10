import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve



##Problema 5
#Problema 5.1

#El ingreso por ventas inicial es de 1 millon de pesos y va disminuyendo en 20 miles de pesos por semana.
#El costo de inversion inicial es de 500 miles de pesos y va aumentando en 200 miles de pesos por semana.

#Problema 5.2

def I(x):
    return -20*x+1000

def C(x):
    return 200*x+500

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

def f(x):
    return I(x) - C(x)

#Valor/es inicial/es de la aproximación
xo = np.linspace(2, 4, 1)
solucion = fsolve(f, xo)

print(f"La cordenada x del punto de equilibrio es de {solucion[0]:.2f}.")
print(f"La cordenada y del punto de equilibrio es de {I(solucion[0])}")

#El punto de equilibrio es (2.27 , 954.55) aproximadamente.

#Problema 5.4

#En la semana 5 no conviene mantener la campaña, ya que los costos son mas altos que los ingresos. 
#En general, conviene mantener la campaña hasta las 2.27 semanas.
