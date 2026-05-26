# while True:
#     try:
#         pasajes=int(input("Ingrese la cant de pasajes a comprar: "))
#         break
#     except:
#         print("Ingrese numeros solo numeros naturales")

# suma=0


# for i in range(pasajes):
#     while True:
#         try:
#             valor=int(input(f"Ingrese el valor del pasaje numero {i+1}: "))
#             suma=valor+suma
#             break
#         except:
#             print("Ingrese solo numeros naturales")


# print(f"El valor total de los pasajes es {suma}")

while True:
    try:
        bultos=int(input("Ingrese la cant de bultos: "))
        break
    except:
        print("Ingrese numeros solo numeros naturales")

suma=0
bl=0
bp=0

for i in range(bultos):
    while True:
        try:
            peso=int(input(f"Ingrese el peso del bulto numero {i+1} en kilos: "))
            if 1<=peso<=5:
                suma+=1000
                bl+=1
                break
            elif 6<=peso<=10:
                suma+=2000
                bp+=1
                break
            elif peso<1 or peso>10:
                print("Valor fuera del rango (1-10 Kg)")
            
        except:
            print("Ingrese solo numeros naturales dentro del rango")

print(f"El valor total de los bultos es {suma} y hubo {bl} bultos livianos y {bp} bultos pesados")