import random
import time

# Matriz de markobv cada maquina

class Maquina:

    def __init__(self, nombre, estado, tiempo):
        self.nombre = nombre
        self.estado = estado
        self.tiempo = tiempo

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getTiempo(self):
        return self.tiempo

    def countDown(self):
        while self.tiempo:
            # mins, secs = divmod(self.tiempo, 60)
            # timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end="\r")
            time.sleep(1)
            self.tiempo -= 1
        self.estado = False

    def usarMaquina(self, tiempo):
        self.estado = False
        self.tiempo = tiempo


# Matriz de markov de las rutinas
#Pecho/Tricep
matrixPecho=[
    [0,0.15,0.05,0.1,0.6,0.02,0.02,0.02,0.02,0.2], # Eliptica
    [0.15,0,0.05,0.1,0.6,0.02,0.02,0.02,0.02,0.2], # Caminadora
    [0.1,0.1,0,0.15,0.25,0.4,0,0,0,0], # Pullup/Dip Machine
    [0,0,0.4,0,0.3,0.3,0,0,0,0], # Cable Machine
    [0,0,0.3,0.4,0.2,0.1,0,0,0,0], # Bench Press
    [0,0,0,0,0,0,0,0,0,0], # Tricep Extension Machine
    [0,0,0.05,0.35,0.55,0.05,0,0,0,0], # Sentadilla Smith
    [0,0,0.05,0.35,0.55,0.05,0,0,0,0], # Row Machine
    [0,0,0.05,0.35,0.55,0.05,0,0,0,0], # Cuadriceps Extension
    [0,0,0.05,0.35,0.55,0.05,0,0,0,0]] # Curl Acostado Femoral

# Pierna
matrixPierna = [
    [0,0.15,0.02,0.02,0.001,0.001,0.5,0.001,0.203,0.104], # Eliptica
    [0,0.15,0.02,0.02,0.001,0.001,0.5,0.001,0.203,0.104], # Caminadora
    [0,0,0,0.1,0,0,0.5,0,0.2,0.2], # Pullup/Dip Machine
    [0.33,0.4,0,0.1,0,0,0.07,0,0.05,0.05], # Cable Machine
    [0,0,0,0.1,0,0,0.5,0,0.2,0.2], # Bench Press
    [0,0,0,0.1,0,0,0.5,0,0.2,0.2], # Tricep Extension Machine
    [0,0,0,0.1,0,0,0.2,0,0.35,0.35], # Sentadilla Smith
    [0,0,0,0.1,0,0,0.5,0,0.2,0.2], # Row Machine
    [0,0,0,0.1,0,0,0.45,0,0,4.5], # Cuadriceps Extension
    [0,0.25,0,0.35,0,0,0.3,0,0.1,0]] # Curl Acostado Femoral

#Espalda/Bicep
matrixEspalda= [
    [0,0.05,0.4,0.2,0.01,0.01,0.01,0.3,0.01,0.01], # Eliptica
    [0.05,0,0.4,0.2,0.01,0.01,0.01,0.3,0.01,0.01], # Caminadora
    [0.15,0.15,0,0.1,0,0,0.3,0.3,0,0], # Pullup/Dip Machine
    [0.15,0.15,0,0.1,0,0,0.3,0.3,0,0], # Cable Machine
    [0,0,0.3,0.3,0,0,0.2,0.2,0,0], # Bench Press
    [0,0,0.3,0.3,0,0,0.2,0.2,0,0], # Tricep Extension Machine
    [0.15,0.15,0.3,0.3,0,0,0,0.1,0,0], # Sentadilla Smith
    [0.15,0.15,0.3,0.3,0,0,0.1,0,0,0], # Row Machine
    [0,0,0.3,0.3,0,0,0.2,0.2,0,0], # Cuadriceps Extension
    [0,0,0.3,0.3,0,0,0.2,0.2,0,0]] # Curl Acostado Femoral

def crear_maquinas():

    nombres = ["Eliptica","Caminadora","Pullup/Dip Machine","Cable Machine","Bench Press","Tricep Extension Machine","Sentadilla Smith","Row Machine","Cuadriceps extension","Curl acostado Femoral"]
    maquinas = []
    print("NOMBRES DE LAS MAQUINAS ")
    for j in range(0, len(nombres)):
        tmp = Maquina(nombres[j], False, 30)
        maquinas.append(tmp)
        print(maquinas[j].nombre, end=",")
    return maquinas


machines = crear_maquinas()

#Generar rutina
def generarRuntina(matriz):
    rutina = []
    pos = 0
    numero = 0
    rutina.append(numero)
    for i in range (5):
        valor = random.uniform(0, 1)
        acum = matriz[pos][0]
        print("Valor: ", valor)
        print("Acumulaci??n:", acum)
        for x in range(1, len(matriz[pos])):
            print("Dato: ", matriz[pos][x], "Maquina: ", x)
            if (valor >= acum):
                acum += matriz[pos][x]
                numero = x
            else:
                break
        rutina.append(numero)
        print("N??mero: ", numero)
        pos = numero
        numero = 0
    return rutina


#Recorrido bots

def generarBots():
    pos = 3
    numero = 0
    for i in range(9):
        valor = random.uniform(0, 1)
        acum = matrixEspalda[pos][0]
        print("Valor: ", valor)
        print("Acumulaci??n:", acum)
        for x in range(1, len(matrixEspalda[pos])):
            print("Dato: ", matrixEspalda[pos][x], "Maquina: ", x)
            if valor >= acum:
                acum += matrixEspalda[pos][x]
                numero = x
            else:
                break
        print("N??mero: ", numero)
        machines[numero].estado = True
        #machines[numero].countDown()
        pos = numero
        numero = 0
    return machines

generarBots()
print("MATRIZ A PARTIR DE USUARIOS RANDOM")
for elemento in machines:
    print(elemento.estado, elemento.tiempo)



#RECORRIENDO LA RUTINA
def recorridoUsuario(matrix):
    rutina = generarRuntina(matrix)
    #Checar elementos
    print(rutina,"\n")
    for i in rutina:
        if(machines[i].getEstado()==False):
           #Ocupado
           continue;
        else:
            #Desocupado
            machines[i].estado = True
            
            print("Usando Maquina: ", machines[i].nombre,"\n")

recorridoUsuario(matrixEspalda)





