
print("1.- Pago de Tarjeta de Credito")
print("2.- Simulacion de Compras")
print("3.- Salir")
op=int(input("Selecione una opcion: "))
deuda=-100000
while op!=3:
    match op:
        case 1:
            print(f"Tiene una deuda de {deuda}")
            try:
                pago=int(input("Cuanto de la deuda desea pagar? "))
                if pago>=0:
                    deuda=deuda+pago
                    print("1.- Pago de Tarjeta de Credito")
                    print("2.- Simulacion de Compras")
                    print("3.- Salir")
                    op=int(input("Selecione una opcion: "))
            except:
                print("Solo numeros naturales mayores o iguales a 0")
        case 2:
            try:
                compras=int(print("Ingrese la cantidad de compras: "))
                for i in range(compras):
                    while True:
                        try:    
                            valor=int(print(f"Ingrese el valor de la compra numero {i+1}: "))


            except:
                print("Valor Invalido")
        case 3:
            print("Adios")
        case _:
            print("Opcion invalida")
            print("1.- Pago de Tarjeta de Credito")
            print("2.- Simulacion de Compras")
            print("3.- Salir")
            op=int(input("Selecione una opcion: "))