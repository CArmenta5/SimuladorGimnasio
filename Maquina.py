import time

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
            #mins, secs = divmod(self.tiempo, 60)
            #timer = '{:02d}:{:02d}'.format(mins, secs)
            #print(timer, end="\r")
            time.sleep(1)
            self.tiempo -= 1
        self.estado = False

    def usarMaquina(self, tiempo):
        self.estado = True
        self.tiempo = tiempo