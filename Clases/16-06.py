# Crear al gestor de pacientes en un centro medico
# para poner el nombre se debe validar que no este vacio
# y ademas tenga mas de 8 caracteres
# para la prevision de salud solo existen 3 posibles valores
# Fonasa, Isapre o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no 
# para que este grave debe tener mas de 39°C
# Cada atencion vale $25.000 pesos
# Los descuentos corresponden a:
# Fonasa 54%
# Isapre 27%
# Fodesa 12.5%

pacientes= [
    {"nombre:":"Wanda Maximoff", "prevision:": "Fonasa",
     "temperatura:": 24, "grave": False}
]

# nombre=input("Ingrese el nombre del paciente: ")
# prevision=input("Ingrese la prevision del paciente: ")
# temperatura=int(input("Ingrese la temperatura del paciente: "))
# if temperatura>=39:
#     grave=True
# else:
#     grave=False




# while True:
#     try:
#         nombre=input("Ingrese el nombre del paciente: ")
#         while len(nombre)<8:
#             print("El nombre es muy corto")
#             nombre=input("Ingrese el nombre del paciente: ")
#     except:
#         print("Minimo 8 caracteres")

#     try:
#         prevision=input("Ingrese la prevision del paciente, Fonasa, Isapre o Fodesa: ")
#         while prevision!="Fonasa" or "Isapre" or "Fodesa":
#             print("Prevision invalida, ingrese una prevision valida")
#             prevision=input("Ingrese la prevision del paciente, Fonasa, Isapre o Fodesa: ")
#     except:
#         print("Prevision invalida, ingrese una prevision valida")
#     temperatura=int(input("Ingrese la temperatura del paciente: "))
#     if temperatura>=39:
#         grave=True
#     else:
#         grave=False


#     paciente.append({"nombre:":nombre, "prevision:": prevision,
#     "temperatura:": temperatura, "grave": grave})

def validarEstado(tempe):
    if tempe>39:
        return True
    else:
        return False
def mostrarPaciente():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1 
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1


while True:
    try:
        print("1.- Ingresar paciente")
        print("2.- Sacar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobrar atencion")
        print("5.- Mostrar pacientes")
        print("6.- Salir")
        op=int(input("Ingrese una opcion"))
        match op:
            case 1:
                nombre=input("Ingrese nombre: ")
                prevision=input("Ingrese prevision: ")
                temp=float(input("Ingrese temperatura: "))
                pacientes.append({"nombre:":nombre, "prevision:": prevision,
                            "temperatura:": temp, "grave": validarEstado(temp)})
                print("Paciente agregado con exito")

            case 2:
                mostrarPaciente()
                paci=int(input("Que paciente se va?"))
                pacientes.pop(paci-1)
                print("Paciente eliminado con exito")
            case 3:
                print("")
            case 4:
                print("")
            case 5:
                mostrarPaciente()

            case 6:
                print("")
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("Error:", e)