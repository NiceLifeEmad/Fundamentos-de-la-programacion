
tramo=0
edad=int(input("Ingrese su edad: "))
tramo=int(input("Ingrese su tramo 1)A 2)B 3)C 4)D: "))
med=60000
despa=8000

if edad<=30:
    if tramo==1 or tramo==2:
        print(f"El valor de sus medicamentos es {med*0.82}")
        print(f"El valor de su despacho es {despa*0.9}")
    elif tramo==3 or tramo==4:
        print(f"El valor de sus medicamentos es {med*0.88}")
        print(f"El valor de su despacho es {despa}")
elif edad>=55 and edad<=60:
    if tramo==1 or tramo==2:
        print(f"El valor de sus medicamentos es {med*0.82}")
        print(f"El valor de su despacho es {despa*0.85}")
    elif tramo==3 or tramo==4:
        print(f"El valor de sus medicamentos es {med*0.92}")
        print(f"El valor de su despacho es {despa*0.95}")
elif edad>=31 and edad<=60:
    if tramo==1 or tramo==2:
        print(f"El valor de sus medicamentos es {med*0.82}")
        print(f"El valor de su despacho es {despa*0.9}")
    elif tramo==3 or tramo==4:
        print(f"El valor de sus medicamentos es {med*0.92}")
        print(f"El valor de su despacho es {despa}")


