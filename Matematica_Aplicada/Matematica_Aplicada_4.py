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

##Problema 8
#Problema 8.1

# a_10=20
# -20=a_1+(10-1)*4
# -20=a_1+9*4
# -20=a_1+36
# -20-36=a_1
# -56=a_1

#Problema 8.2

# La expresion general es a_n = -56 + (n-1)*4

#Problema 8.3

# sucesion = []
# for i in range(0,100):
#     n = i + 1
#     sucesion.append(-56+(n-1)*4)
    
# print(f'El término 100 es {sucesion[99]}')

#Problema 8.4

# final=1680 
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=-56+(n-1)*4
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')

##Problema 9
#Problema 9.1

#a_1->a_2->a_3->a_4->a_5->a_6
#           5 ->*r ->*r ->*r = 40
#5*r**3=40
#r**3=40/5
#r**3=8
#r=raiz cubica de 8
#r=2
#La razon geometrica es 2

#Problema 9.2

#a_3=5
#a_2=5/2
#a_2=2.5
#a_1=2.5/2
#a_1=1.25

#Problema 9.3

#1.25*2**(n-1)

#Problema 9.4

# sucesion = []
# for i in range(10):
#     n = i + 1
#     sucesion.append(1.25*2**(n-1))
    
# print(f'El término 8 es {sucesion[7]}')

#Problema 9.5

# final=20480
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=1.25*2**(n-1)
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')^

##Problema 10
#Problema 10.1

#r_2= 1.2
#r_5= 2.7

#1.2*r**3=2.7
#r**3=2.7/1.2
#r**3=2.25
#r=2.25**(1/3)
#r=1.31
#a_1=a_2/r
#a_1=1.2/1.31
#a_1=0.92

# sucesion = []
# for i in range(13):
#     n = i + 1
#     sucesion.append(0.92*1.31**(n-1))
#     print(f'El término {n} es {sucesion[i]:.2f}')

# print(f'El término 9 es {sucesion[8]:.2f}')

#Problema 10.2

#En el decimo tercer mes, el rendimiento es de 23.4 miles de TPS

##Problema 11
#Problema 11.1

#a_3=500
#a_10=1501
#a_3+7x=1501
#500+7x=1501
#7x=1501-500
#7x=1001
#x=1001/7
#x=143
#d=143
#a_1=a_3-(2d)
#a_1=500-(143*2)
#a_1=500-286
#a_1=214

#Problema 11.2

# sucesion = []
# for i in range(31):
#     n = i + 1
#     sucesion.append(214+(n-1)*143)
    
# print(f'El término 31 es {sucesion[30]}')


#Problema 11.3

# final=5505 
# termino=0
# n=0
# dif=final-termino
# while dif>0:
#     n +=1
#     termino=214+(n-1)*143
#     dif=final-termino

# if dif==0:
#     print(f'El {final} es un término de la sucesión y ocupa el lugar {n}')

# else:
#     print(f'El {final} no pertenece a la sucesión')

# print(f"La aplicacion lleva funcionando un mes y 7 dias")
