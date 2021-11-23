from tkinter import *
import tkinter

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
        "Pierna"
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


def CanvasRight(ventana):

    #Configuración de canvas
    canvas2 = Canvas(ventana)
    canvas2.config(width=920, height=800)
    canvas2.config(bg="alice blue")
    canvas2.place(relx=1.0, rely=1.0, anchor=SE)
    
    # Texto
    canvas2.create_text(475, 50, text="GYM TEC", fill="black", font=('Helvetica 25 bold'))

    #canvas2.create_oval(100, 10, 180, 80, width=2, fill='blue')

    #Maquinas
   

    
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

    


