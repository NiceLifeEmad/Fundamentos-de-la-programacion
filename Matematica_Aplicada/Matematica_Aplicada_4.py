import numpy as np

# sucesion = []
# for i in range(3):
#     n = i + 1
#     sucesion.append(8.4*n-5)
#     print(f'El término {n} es {sucesion[-1]:.1f}')   

# sucesion = []
# for i in range(3):
#     n = i + 1
#     sucesion.append(-3*n**2+40)
#     print(f'El término {n} es {sucesion[-1]}')   

# final=126 
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=7*n-15
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')

##Problema 1
#Problema 1.1
# sucesion = []
# for i in range(5):
#     n = i + 1
#     sucesion.append(3*n**2-7)
#     print(f'El término {n} es {sucesion[-1]:.1f}')   


#=================================================================================================================================
#=================================================================================================================================


# #Problema 1.1
# sucesion = []
# for i in range(0, 5):
#     n = i + 1
#     sucesion.append(3*n**2-7)
#     print(f'El término {n} es {sucesion[-1]:.1f}')   

#Problema 1.2
# sucesion = []
# for i in range(15, 20):
#     n = i + 1
#     sucesion.append(3*n**2-7)
#     print(f'El término {n} es {sucesion[-1]:.1f}')   

##Problema 2
#Problema 2.1

# sucesion = []
# for i in range(4):
#     n = i + 1
#     sucesion.append(5*n**3)
#     print(f'El término {n} es {sucesion[-1]:.1f}')  

# #Problema 2.2

#     sucesion = []
# for i in range(8, 12):
#     n = i + 1
#     sucesion.append(5*n**3)
#     print(f'El término {n} es {sucesion[-1]:.1f}')  

# #Problema 2.3

# final=40000 
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=5*n**3
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')

##Problema 3
#Problema 3.1

# sucesion = [0, 1]
# for i in range(0, 20):
#     n = i + 1
#     sucesion.append(sucesion[i]+sucesion[i+1])
#     print(f'El término {n} es {sucesion[-1]}')


##Problema 4
#Problema 4.1

# sucesion = []
# for i in range(0, 100):
#     n = i + 1
#     sucesion.append(2*n)

# print(f'El término 10 es {sucesion[9]}')

# #Problema 4.2

# suma = sum(sucesion)
# print(f'La suma de los primeros términos de la sucesión es {suma}.') 

#Problema 4.3

# final=58
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=2*n
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')


##Problema 5
#Problema 5.1

# sucesion = []
# for i in range(7):
#     n = i + 1
#     sucesion.append(575*1.15**(n-1))
#     print(f'El mes {n} es {sucesion[-1]:.0f}')

#Problema 5.2

# sucesion = []
# for i in range(13):
#     n = i + 1
#     sucesion.append(500*1.15**(n-1))
#     print(f'El mes {i} es {sucesion[i]:.0f} usuarios.')

#Problema 5.3

# sucesion = []
# for i in range(13):
#     n = i + 1
#     sucesion.append(500*1.15**(n-1))
#     # print(f'El mes {i} es {sucesion[i]:.0f} usuarios.')

# suma = sum(sucesion)
# print(f'Luego de un año la cantidad total de usuarios seria {suma:.0f}.') 

##Problema 6
#Problema 6.1

# sucesion = []
# for i in range(0, 12):
#     n = i + 1
#     sucesion.append(12000+(n-1)*2000)
#     print(f'El término {n} es {sucesion[-1]}')

#Problema 6.2

# sucesion = []
# for i in range(0, 14):
#     n = i + 1
#     sucesion.append(12000+(n-1)*2000)

# print(f'En febrero del segundo año el deposito es {sucesion[-1]} pesos')

#Problema 6.3

# sucesion = []
# for i in range(0, 24):
#     n = i + 1
#     sucesion.append(12000+(n-1)*2000)
#     # print(f'El término {n} es {sucesion[-1]}')

# suma = sum(sucesion)
# print(f'El total ahorrado luego de dos años es de ${suma} pesos.') 


##Problemas 7
#Problema 7.1
 
# sucesion = []
# for i in range(5):
#     n = i + 1
#     sucesion.append(3*0.9**(n-1))
#     print(f'La fase numero {n} dura {sucesion[-1]:.2f} meses') 
 
#Problema 7.2 

# sucesion = []
# for i in range(10):
#     n = i + 1
#     sucesion.append(3*0.9**(n-1))
#     print(f'La fase numero {n} dura {sucesion[-1]:.2f} meses') 
