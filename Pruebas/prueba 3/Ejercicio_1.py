while True:
    try:
        numero=int(input("Ingrese el numero de medicos: "))
        break
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar")


especialista=0
interno=0

for i in range(numero):
        while True:
            try:
                nombre=input("Ingrese el nombre profesional del medico: ")
                while len(nombre)<=5:
                    print("Registro Medico Invalido, debe tener almenos 6 caracteres y sin espacios")
                    nombre=input("Ingrese el nombre profesional del medico: ")
                    break
                while " " in nombre:
                    print("Registro Medico Invalido, debe tener almenos 6 caracteres y sin espacios")
                    nombre=input("Ingrese el nombre profesional del medico: ")
                    break
                break
            except ValueError:
                print("Registro Medico Invalido, debe tener almenos 6 caracteres y sin espacios")

        while True:
            try:
                expe=int(input("Ingrese la experiencia en años del medico: "))
                while expe<=0:
                    print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
                    expe=int(input("Ingrese la experiencia en años del medico: "))
                if expe>5:
                    especialista+=1
                elif 0<expe<=5:
                    interno+=1
                break
            except ValueError:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

print(f"¡El hospital cuenta con {especialista} Especialistas Senior y {interno} Residentes Junior!")
print("¡Sistema listo para operar!")