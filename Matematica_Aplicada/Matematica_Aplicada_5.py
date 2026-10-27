import numpy as np

##Problema 1
#Problema 1.1

# A = np.array([[2.6,4.8,1.8,0.9],
#               [3.2,4.4,2.5,2.8],
#               [2.4,3.6,3.8,2.5]])

# B = np.array([[3.6,2.5,3.0,2.5],
#               [4.5,5.0,3.5,3.8],
#               [2.9,3.0,4.6,4.0]])

# #Problema 1.2

# S=A+B
# print(S)

# #Problema 1.3

# D=B-A
# print(D)

# #Problema 1.4

# s24=S[1][3]
# print(s24)

# d24=D[1][3]
# print(d24)

#Problema 1.5

#No, no seria posible dado que seria diferente el orden entre estas matrices, aunque se podria rellenar las matrices A y B con 0 para igualar el orden


##Problema 2
#Problema 2.1

# J = np.array([[100,200,150],
#               [120,210,170],
#               [112,200,131],
#               [124,310,170],
#               [136,156,140]])

# C = np.array([[110,190,160],
#               [130,220,180],
#               [146,190,141],
#               [143,312,163],
#               [137,116,156]])

# #Problema 2.2

# j21=J[1][0]
# print(j21)

# c12=C[0][1]
# print(c12)

# #Problema 2.3

# M=C+J
# print(M)

# #Problema 2.4

# print(f"Si, tiene razon, ya que en Japon, el precio del proiducto 3 en el modelo 4 es {J[3][2]} y en China es {C[3][2]}")


##Problema 3
#Problema 3.1

C = np.array([[120,200,155,125,230],
              [155,130,110,160,180],
              [140,205,150,125,155],
              [130,120,230,225,125],
              [135,70,190,175,95],
              [110,265,180,230,180],
              [185,85,120,135,150]])

E = C*0.8

print(E)

#Problema 3.2

#T=C_ij+E_ij

#Problema 3.3

T = C+E
print(T)

#Problema 3.4

c34=C[2][3]
print(c34)

t72=T[6][1]
print(t72)
