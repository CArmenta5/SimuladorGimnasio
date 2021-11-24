from tkinter import *
import tkinter
import Gym
from PIL import ImageTk, Image
states = [1,1,1,1,1,1,1,1,1,1]
maquinas = Gym.crear_maquinas()
maquinas2 = Gym.generarBots()
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
    canvas1.create_text(135, 400, text="[]", fill="black", font=('Helvetica 14'))

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

    # Método click
    def buttonClick():
        #Gym.generarRuntina()
        print(dropdown.get())
        if(dropdown.get() == "Pierna"):
            Gym.generarRuntina(matrixPierna)
        elif(dropdown.get() == "Espalda"):
            Gym.generarRuntina(matrixEspalda)
        elif(dropdown.get() == "Pecho"):
            Gym.generarRuntina(matrixPecho)
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


    
