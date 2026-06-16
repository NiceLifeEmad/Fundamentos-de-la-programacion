## Ejemplo y uso de listas

#     -5 -4 -3 -2  -1
# lista=[4, 7, 9, 2, 3.8]
# #      0  1  2  3   4

# print(lista)
# print(lista[2])

# name="LINK"

# for i in name:
#     print(i)

# for i in lista:
#     print(i)


# Cree una lista de 4 frutas y muestrelas por pantalla

# frutas=["MANZANA", "NARANJA", "platano", "durazno", "Uva"]
# ccVocal=0
# for f in frutas:
#     if f[0].lower() in ("aeiou"): 
#         print("la fruta es ", f " comienza con vocal")
#         ccVocal+=1
#     else:
#         print("la fruta es ", f)
# print("Total de frutas que inician con vocal ", ccVocal)

## Cree una lista con 3 nombres
## Cree una lista con 3 apellidos
## Que aparescan los nombres y apellidos correspondientes

# nombres=["Vicente", "Ricardo", "Alexander"]
# ape=["Muñoz", "Araya", "Inostroza"]

# for p in range(len(ape)):
#     print(nombres[p], ape[p]) 

# ## Añadir cosas a la lista con .append
# nombres.append("Felipe")
# ape.append("Camiroaga")

# for p in range(len(ape)):
#     print(nombres[p], ape[p]) 


## Cree una lista de animales con 3 elementos
## Agregue dos mas y muestre el resultado

animales=["Leon", "Tigre", "Leopardo"]

for i in animales:
    print(i)

animales.append("Pantera")
animales.append("Gato")

for i in animales:
    print(i)

## animales.remove("Pantera") para quitar de la lista
## animales.insert(1, "Pantera") Para añadir en cierto punto en especifico el objeto
