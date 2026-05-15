## Para evitar que se pierdan los datos ingresados
## se puede añadir else y finally, si no se usa except ocure else y finally ocurre siempre
##Tipos de errores:
## ZeroDivisionError
## TypeError 
## ValueError
## FileNotFoundError
## SyntaxError

while True:
    try:
        num=int(input("Ingrese un numero: "))
        break
    except:
        print("Solo numeros enteros")