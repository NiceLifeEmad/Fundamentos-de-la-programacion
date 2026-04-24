## Uso y explicacion de While

# cont=0
# while cont<=3:
#     print("Repeticion numero", cont)
#     cont+=1

#Ingrese PIN
pin=3232

baka=int(input("Ingrese su pin"))
while pin!=baka:
    print("Pin Incorrecto")
    baka=int(input("Ingrese su pin"))
print("PIN correcto")
