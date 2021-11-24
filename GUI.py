from tkinter import *
import tkinter
from PIL import ImageTk, Image
import Gym
states = [1,1,1,1,1,1,1,1,1,1]
print("IMPRIMIENDO LOS ESTADOS DESTATES")
for elemento in states:
    print(elemento)
statesCircles = [0] * 10
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

    # Seleccionar rutina
    RutinaList = [
        "Pierna",
        "Espalda",
        "Pecho"
    ] 

    dropdown = tkinter.StringVar(ventana)
    dropdown.set(RutinaList[0])
    opt = tkinter.OptionMenu(ventana, dropdown, *RutinaList)
    opt.config(width=20, font=('Helvetica', 11), bg="lavender")
    opt.place(x=30, y=170)

    #Boton
    boton = tkinter.Button(text="Enviar")
    boton.config(width=10, font=('Helvetica', 11), fg="white",bg="light slate blue")
    boton.place(x=80, y=220)

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
    statesCircles[0] = canvas2.create_oval(190, 295, 210, 315, width=2, fill='red')

    canvas2.create_image(400,155, image= canvas2.image, anchor = "nw")
    statesCircles[1] = canvas2.create_oval(450, 295, 470, 315, width=2, fill='red')

    canvas2.create_image(660,155, image= canvas2.image, anchor = "nw")
    statesCircles[2] = canvas2.create_oval(710, 295, 730, 315, width=2, fill='red')

    canvas2.create_image(60,345, image= canvas2.image, anchor = "nw")
    statesCircles[3] = canvas2.create_oval(110, 485, 130, 505, width=2, fill='red')

    canvas2.create_image(290,345, image= canvas2.image, anchor = "nw")
    statesCircles[4] = canvas2.create_oval(340, 485, 360, 505, width=2, fill='red')

    canvas2.create_image(520,345, image= canvas2.image, anchor = "nw")
    statesCircles[5] = canvas2.create_oval(570, 485, 590, 505, width=2, fill='red')

    canvas2.create_image(750,345, image= canvas2.image, anchor = "nw")
    statesCircles[6] = canvas2.create_oval(800, 485, 820, 505, width=2, fill='red')
    
    canvas2.create_image(140,535, image= canvas2.image, anchor = "nw")
    statesCircles[7] = canvas2.create_oval(190, 675, 210, 695, width=2, fill='red')

    canvas2.create_image(400,535, image= canvas2.image, anchor = "nw")
    statesCircles[8] = canvas2.create_oval(450, 675, 470, 695, width=2, fill='red')

    canvas2.create_image(660,535, image= canvas2.image, anchor = "nw")
    statesCircles[9] = canvas2.create_oval(710, 675, 730, 695, width=2, fill='red')
  
    ventana.after(1000,changeState(canvas2))

def changeState( canvas : Canvas):
    for i in range(0,len(states)):

        if states[i] == 0:
            canvas.itemconfig(statesCircles[i], fill='green')
            #states[i] = 1

        else:
            #states[i] = 0
            canvas.itemconfig(statesCircles[i], fill='red')
    for element in states:
        print(element)
#print

def main():
    ventana.title("Simulador de Gimnasio")
    ventana.geometry("1200x800")
    ventana.resizable(width=False, height=False)


if __name__ == "__main__":
    ventana = Tk()
    
    main()
    CanvasLeft(ventana)
    CanvasRight(ventana)
    ventana.mainloop()

    
