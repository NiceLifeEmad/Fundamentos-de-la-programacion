can1=(input("Ingrese el candidato numero 1: "))
can2=(input("Ingrese el candidato numero 2: "))
votantes=int(input("Ingrese el numero de votantes: "))
vcan1=0
vcan2=0

for i in range (votantes):
    voto=int(input(f"Por quien desea votar, 1. el candidato {can1} 2. el candidato {can2}? "))
    if voto==1:
        vcan1=vcan1+1
    elif voto==2:
        vcan2=vcan2+1
    else:
        print("Voto nulo")

if vcan1>vcan2:
    print(f"Tras contar los votos, el ganador es: {can1} con {vcan1} votos")
elif vcan2>vcan1:
    print(f"Tras contar los votos, el ganador es: {can2} con {vcan2} votos")
else:
    print(f"Ha habido un empate entre ambos candidatos con un total de {vcan1} para {can1} y {vcan2} para {can2}")