import random

# Matriz de markobv cada maquina

matrixPecho = [ 
    [0,0,0,0,0,0,0,0,0,0], # Eliptica
    [0,0,0,0,0,0,0,0,0,0], # Caminadora
    [0,0,0,0,0,0,0,0,0,0], # Pullup/Dip Machine 
    [0,0,0,0,0,0,0,0,0,0], # Cable Machine
    [0,0,0,0,0,0,0,0,0,0], # Bench Press
    [0,0,0,0,0,0,0,0,0,0], # Tricep Extension Machine
    [0,0,0,0,0,0,0,0,0,0], # Sentadilla Smith
    [0,0,0,0,0,0,0,0,0,0], # Row Machine
    [0,0,0,0,0,0,0,0,0,0], # Cuadriceps Extension
    [0,0,0,0,0,0,0,0,0,0]] # Curl Acostado Femoral                   

rutina = []
pos = 0
numero = 0
#Generar rutina

for i in range (2):
    valor = random.uniform(0, 1)
    acum = matrixPecho[pos][0]
    print("Valor: ", valor)
    print("Acumulación:", acum)
    for x in range(1, len(matrixPecho[pos])):
        print("Dato: ", matrixPecho[pos][x], "Maquina: ", x)
        if valor >= acum:
            acum += matrixPecho[pos][x]
            numero = x
        else:
            break

    rutina.append(numero)
    print("Número: ", numero)
    pos = numero
    numero = 0

print(rutina)








