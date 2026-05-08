from random import randint

limi=int(input("Ingrese el limite inferior: "))
lims=int(input("Ingrese ingrese el limite superior: "))
while limi>lims:
    print("Limite superior es inferior al limite inferior, porfavor, corrijalo")
    limi=int(input("Ingrese el limite inferior: "))
    lims=int(input("Ingrese ingrese el limite superior: "))
num=randint(limi, lims)

num=5
if num%2!=0:
    if num+1>lims:
        num-=1
    else:
        num+=1

intentos=3
print("Ahora intente adivinar el numero")
adivino1=int(input("Ingrese un numero: "))

while intentos!=0:

    if adivino1==num:
        print("Felicitaciones, pudiste adivinarlo en tu primer intento")
    elif adivino1!=num and intentos==3:
        if adivino1<num:
            print("Lo siento, te equivocaste, el numero es mayor, intentalo de nuevo")
            intentos-=1
            adivino2=int(input("Ingrese un numero: "))
        elif adivino1>num:
            print("Lo siento, te equivocaste, el numero es menor, intentalo de nuevo")
            intentos-=1
            adivino2=int(input("Ingrese un numero: "))

    if adivino2==num:
        print("Felicitaciones, pudiste adivinarlo en tu segundo intento")
    elif adivino2!=num and intentos==2:
        if adivino2<num:
            print("Lo siento, te equivocaste, el numero es mayor, intentalo de nuevo")
            print("Pero te dare una pista")
            if abs(adivino1)>abs(adivino2):
                print("Tu primer intento estuvo mas cerca del numero")
            elif abs(adivino1)<abs(adivino2):
                print("Tu segundo intento estuvo mas cerca del numero")
            intentos-=1
            print("Ahora intente adivinar el numero de nuevo, es tu ultima oportunidad")
            adivino3=int(input("Ingrese un numero: "))
        elif adivino2>num:
            print("Lo siento, te equivocaste, el numero es menor, intentalo de nuevo")
            print("Pero te dare una pista")
            if abs(adivino1)>abs(adivino2):
                print("Tu primer intento estuvo mas cerca del numero")
            elif abs(adivino1)<abs(adivino2):
                print("Tu segundo intento estuvo mas cerca del numero")
            intentos-=1
            print("Ahora intente adivinar el numero de nuevo, es tu ultima oportunidad")
            adivino3=int(input("Ingrese un numero: "))

            if adivino3==num:
                print("Felicitaciones, pudiste adivinarlo en tu ultimo intento")
            elif adivino3!=num and intentos==1:
                print(f"Lo siento, te equivocaste y se te acabaron los intentos, el numero era {num}")
                intentos-=1
     
        


