indie=0
estudio=0
tod=0
adol=0
mayo=0

while True:
    try:
        juegos=int(input("Cuantos juegos se registraran? "))
        break
    except ValueError as er:
        print("Numero de juegos invalido. Error", er)

for i in range (juegos):
    titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ").upper()

    while " " in titulo:
        print("No debe incluir espacios")
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ")

    while len(titulo)<5:
        print("El titulo es muy corto")
        titulo=input("Ingrese el nombre del juego (Al menos 5 caracteres y sin espacios): ")

    while True:
        try:
            precio=int(input("Ingrese el precio del juego: "))
            break
        except:
            print("Solo numeros enteros positivos")

    if precio>=20000 and precio<40000:
        print("El juego es indie")
        indie+=1
    elif precio>=40000:
        print("El juego es de estudio")
        estudio+=1

    while True:
        try:
            clasif=int(input("Ingrese la clacificacion del juego (edad): "))
            break
        except:
            print("Solo numeros enteros positivos")
    
    if clasif<=12:
        print("El juego es de todo publico")
        tod+=1
    elif clasif>12 and clasif<17:
        print("El juego es para adolescentes")
        adol+=1
    elif clasif>=18:
        print("El juego es para mayores")
        mayo+=1

print(f"hay {indie} juegos indie y {estudio} juegos de estudios")
print(f"Tambien hay {tod} juegos de todas las edades , {adol} juegos para adolecentes y {mayo} juegos para mayores")




# nom=" Hitler "
# print(nom.strip()) ## quita espacios al inicio y final
# print(nom.lower()) ## pone todo en minuscula
# print(nom.upper()) ## Pone todo en mayuscula
# print(nom.replace("Hitler, Musolini")) ## Remplaza un string por otro
# print(nom.find()) ## Busca un string
# print(nom.split()) ## Convierte un string en una lista

