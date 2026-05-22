libros=120
historial=0
prestamo=0
devolver=0

print("===MENÚ PRINCIPAL===")
print("1. Libros disponibles")
print("2. Realizar préstamo")
print("3. Devolver préstamo")
print("4. Historial de préstamos")
print("5. Salir")
while True:
    try:
        op=int(input("Seleccione una opcion: "))
        break
    except ValueError:
        print("Opcion invalida, seleccione una de las opciones porfavor")

while op!=5:
    match op:
        case 1:
            print(f"La biblioteca cuenta actualmente con {libros} libros")
            op=int(input("Seleccione una opcion: "))
        case 2:
            while True:
                try:
                    prestamo=int(input("Cuantos libros desea pedir prestado?: "))
                    while prestamo<=0:
                        print("Valor invalido")
                        prestamo=int(input("Cuantos libros desea pedir prestado?: "))
                    libros=libros-prestamo
                    historial=prestamo+historial
                    print(f"Ha pedido prestados {prestamo} libros")
                    print("===MENÚ PRINCIPAL===")
                    print("1. Libros disponibles")
                    print("2. Realizar préstamo")
                    print("3. Devolver préstamo")
                    print("4. Historial de préstamos")
                    print("5. Salir")
                    op=int(input("Seleccione una opcion: "))
                    break
                except ValueError:
                    print("Valor invalido")
        case 3:
            while True:
                try:
                    devolver=int(input("Cuantos libros desea devolver?: "))
                    if devolver<=0:
                        print("Valor invalido")
                        prestamo=int(input("Cuantos libros desea pedir prestado?: "))
                    elif libros==120:
                        print("La biblioteca no acepta mas libros")
                        print("===MENÚ PRINCIPAL===")
                        print("1. Libros disponibles")
                        print("2. Realizar préstamo")
                        print("3. Devolver préstamo")
                        print("4. Historial de préstamos")
                        print("5. Salir")
                        op=int(input("Seleccione una opcion: "))
                        break
                    elif devolver<=0 or libros!=120:
                        libros=libros+devolver
                        historial=devolver-historial
                        print(f"Ha devuelto {devolver} libros")
                    print("===MENÚ PRINCIPAL===")
                    print("1. Libros disponibles")
                    print("2. Realizar préstamo")
                    print("3. Devolver préstamo")
                    print("4. Historial de préstamos")
                    print("5. Salir")
                    op=int(input("Seleccione una opcion: "))
                    break
                except ValueError:
                    print("Valor invalido")
        case 4:
            print(f"El numero de prestamos activos es {prestamo}")
            print("===MENÚ PRINCIPAL===")
            print("1. Libros disponibles")
            print("2. Realizar préstamo")
            print("3. Devolver préstamo")
            print("4. Historial de préstamos")
            print("5. Salir")
            op=int(input("Seleccione una opcion: "))
        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
        case _:
            print("Opcion invalida, seleccione una de las opciones porfavor")
            print("===MENÚ PRINCIPAL===")
            print("1. Libros disponibles")
            print("2. Realizar préstamo")
            print("3. Devolver préstamo")
            print("4. Historial de préstamos")
            print("5. Salir")
            op=int(input("Seleccione una opcion: "))

print("Gracias por utilizar nuestro software, hasta la próxima.")