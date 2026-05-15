while True:
    try:
        pasajes=int(input("Ingrese la cant de pasajes a comprar: "))
        break
    except:
        print("Ingrese numeros solo numeros naturales")

suma=0

for i in range(pasajes):
    try:
        valor=int(input(f"Ingrese el valor del pasaje numero {i}: "))
        suma=valor+suma
    except:
        print("Ingrese solo numeros naturales")

print(f"El valor total de los pasajes es {suma}")