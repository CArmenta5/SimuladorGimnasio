from tkinter import *
import tkinter
import random
import time
from PIL import ImageTk, Image

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
        self.estado = True
        self.tiempo = tiempo

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
    for i in range (9):
        valor = random.uniform(0, 1)
        acum = matriz[pos][0]
        print("Valor: ", valor)
        print("Acumulación:", acum)
        for x in range(1, len(matriz[pos])):
            print("Dato: ", matriz[pos][x], "Maquina: ", x)
            if valor >= acum:
                acum += matriz[pos][x]
                numero = x
            else:
                break
        rutina.append(numero)
        print("Número: ", numero)
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
        print("Acumulación:", acum)
        for x in range(1, len(matrixEspalda[pos])):
            print("Dato: ", matrixEspalda[pos][x], "Maquina: ", x)
            if valor >= acum:
                acum += matrixEspalda[pos][x]
                numero = x
            else:
                break
        print("Número: ", numero)
        machines[numero].estado = True
        #machines[numero].countDown()
        pos = numero
        numero = 0
    return machines

#generarBots()
print("MATRIZ A PARTIR DE USUARIOS RANDOM")
for elemento in machines:
    print(elemento.estado, elemento.tiempo)

#print(generarRuntina(matrixEspalda))

#RECORRIENDO LA RUTINA

        
states = [1,1,1,1,1,1,1,1,1,1]
maquinas = crear_maquinas()
maquinas2 = generarBots()
print("IMPRIMIENDO LOS ESTADOS DESTATES")
#for elemento in states:
    #print(elemento)
statesCircles = [0] * 10
statesPCircles = [0] * 10
statesCoord = {}

def CanvasLeft(ventana):
    # Configuración del canvas
    canvas1 = Canvas(ventana)
    canvas1.config(width=280, height=800)
    canvas1.config(bg="lavender")
    canvas1.place(relx=0.0, rely=1.0, anchor=SW)

    # Texto
    canvas1.create_text(130, 50, text="Simulador de GYM", fill="black", font=('Helvetica 18 bold'))
    canvas1.create_text(135, 150, text="Escoge tu rutina:", fill="black", font=('Helvetica 14 bold'))
    canvas1.create_text(135, 350, text="Rutina:", fill="black", font=('Helvetica 14 bold'))
    mytext = canvas1.create_text(135, 500, text="[]", fill="black", font=('Helvetica 14'))

    # Seleccionar rutina
    RutinaList = [
        "Escoger",
        "Pierna",
        "Espalda",
        "Pecho"
    ] 

    dropdown = tkinter.StringVar(ventana)
    dropdown.set(RutinaList[0])
    opt = tkinter.OptionMenu(ventana, dropdown, *RutinaList)
    opt.config(width=20, font=('Helvetica', 11), bg="lavender")
    opt.place(x=30, y=170)

    
    def maquinasRutina(matriz):
        nombres = ""
        rutina_indices = matriz
        for indice in rutina_indices:
            nombres += maquinas[indice].nombre + "\n"
        return nombres

    # Método click
    def buttonClick():
        print("Escogiste: ", dropdown.get())
        if(dropdown.get() == "Pierna"):
            rutinaG = generarRuntina(matrixPierna)
            canvas1.itemconfig(mytext, text=maquinasRutina(rutinaG))
        elif(dropdown.get() == "Espalda"):
            rutinaG = generarRuntina(matrixEspalda)
            canvas1.itemconfig(mytext, text=maquinasRutina(rutinaG))
        elif(dropdown.get() == "Pecho"):
            rutinaG = generarRuntina(matrixPecho)
            canvas1.itemconfig(mytext, text=maquinasRutina(rutinaG))
        else:
            print("No escogiste alguna rutina")
        
        #display_selected(dropdown)
    
    #Boton
    boton = tkinter.Button(text="Enviar")
    boton.config(width=10, font=('Helvetica', 11), fg="white",bg="light slate blue", command=buttonClick)
    boton.place(x=80, y=220) #hola como estas

def CanvasRight(ventana : Tk):
    canvas2 = Canvas(ventana, bg="alice blue", width=920, height=800)

    # Configuración de canvas
    
    canvas2.place(relx=1.0, rely=1.0, anchor=SE)
    
    # Titulo
    canvas2.create_text(475, 50, text="GYM TEC", fill="black", font=('Helvetica 25 bold'))


    img = Image.open("eliptica.png")
    resized_image= img.resize((120,120), Image.ANTIALIAS)
    canvas2.image = ImageTk.PhotoImage(resized_image)

    #Maquinas
    canvas2.create_image(140,155, image= canvas2.image, anchor = "nw")
    statesCircles[0] = canvas2.create_oval(190, 280, 210, 300, width=2, fill='red')
    statesPCircles[0] = canvas2.create_oval(190, 310, 210, 330, width=2, fill='red')

    canvas2.create_image(400,155, image= canvas2.image, anchor = "nw")
    statesCircles[1] = canvas2.create_oval(450, 280, 470, 300, width=2, fill='red')
    statesPCircles[1] = canvas2.create_oval(450, 310, 470, 330, width=2, fill='red')

    canvas2.create_image(660,155, image= canvas2.image, anchor = "nw")
    statesCircles[2] = canvas2.create_oval(710, 280, 730, 300, width=2, fill='red')
    statesPCircles[2] = canvas2.create_oval(710, 310, 730, 330, width=2, fill='red')

    canvas2.create_image(60,345, image= canvas2.image, anchor = "nw")
    statesCircles[3] = canvas2.create_oval(110, 470, 130, 490, width=2, fill='red')
    statesPCircles[3] = canvas2.create_oval(110, 500, 130, 520, width=2, fill='red')

    canvas2.create_image(290,345, image= canvas2.image, anchor = "nw")
    statesCircles[4] = canvas2.create_oval(340, 470, 360, 490, width=2, fill='red')
    statesPCircles[4] = canvas2.create_oval(340, 500, 360, 520, width=2, fill='red')

    canvas2.create_image(520,345, image= canvas2.image, anchor = "nw")
    statesCircles[5] = canvas2.create_oval(570, 470, 590, 490, width=2, fill='red')
    statesPCircles[5] = canvas2.create_oval(570, 500, 590, 520, width=2, fill='red')

    canvas2.create_image(750,345, image= canvas2.image, anchor = "nw")
    statesCircles[6] = canvas2.create_oval(800, 470, 820, 490, width=2, fill='red')
    statesPCircles[6] = canvas2.create_oval(800, 500, 820, 520, width=2, fill='red')


    canvas2.create_image(140,535, image= canvas2.image, anchor = "nw")
    statesCircles[7] = canvas2.create_oval(190, 660, 210, 680, width=2, fill='red')
    statesPCircles[7] = canvas2.create_oval(190, 690, 210, 710, width=2, fill='red')

    canvas2.create_image(400,535, image= canvas2.image, anchor = "nw")
    statesCircles[8] = canvas2.create_oval(450, 660, 470, 680, width=2, fill='red')
    statesPCircles[8] = canvas2.create_oval(450, 690, 470, 710, width=2, fill='red')

    canvas2.create_image(660,535, image= canvas2.image, anchor = "nw")
    statesCircles[9] = canvas2.create_oval(710, 660, 730, 680, width=2, fill='red')
    statesPCircles[9] = canvas2.create_oval(710, 690, 730, 710, width=2, fill='red')

    ventana.after(1000,changeState(canvas2))

def display_selected(variable):
    choice = variable.get()
    print(choice)

def changeState( canvas : Canvas):
    for i in range(0,len(states)):

        if states[i] == 0:
            canvas.itemconfig(statesCircles[i], fill='green')
            #states[i] = 1

        else:
            #states[i] = 0
            canvas.itemconfig(statesCircles[i], fill='red')
    #for element in states:
       # print(element)
#print

def main():
    ventana.title("Simulador de Gimnasio")
    ventana.geometry("1200x800")
    ventana.resizable(width=False, height=False)
    #Gym.crearMaquinas()


if __name__ == "__main__":
    ventana = Tk()
    
    main()
    CanvasLeft(ventana)
    CanvasRight(ventana)
    ventana.mainloop()


    
