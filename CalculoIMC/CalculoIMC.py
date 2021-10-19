import tkinter as tk
from tkinter.messagebox import *


peso=0
altura=0
imc=0
mensaje=""

def calcularIMC():
    
    global mensaje
    res1 = validarCampo(txt.get().strip())
    if res1:
        txt.config(background = "lightgreen")
    else:
        txt.config(background ="orangered")
        mensaje +=" 'Peso'"
        
        
    res2 = validarCampo(txt2.get().strip())
    if res2:
        txt2.config(background = "lightgreen")
    else:
        txt2.config(background ="orangered")
        mensaje += " 'Altura'"
        
        
    if res1 and res2:
    
        try:
            peso = float(txt.get())
            altura = float(txt2.get())
            altura = altura * altura
    
            imc = peso/altura
            txt.config(background = "lightgreen")
            txt2.config(background = "lightgreen")
    
            label2.config(text ="Su indice de masa corporal es: " + str(round(imc,2)))    
        except:
            label2.config(text = "Error en los datos")
            
    else:
        mensajeInfo("Valores no admitidos en los campos: " + mensaje)
    mensaje=""
    


def mensajeInfo( mensajes = "error", titulo = "Error"):
    
    showinfo(message=mensajes, title=titulo)
    
    

def limpiar():
    txt.config(background = "white")
    txt2.config(background = "white")
    
    txt2.delete(0,tk.END)
    txt.delete(0,tk.END)

    
    
    
ventana = tk.Tk()

ventana.config(width=500, height=400)
ventana.title("Calculadora de IMC")


boton1 = tk.Button(text="Calcular IMC", command=calcularIMC)
boton1.place(x=250,y=50, width = 130, height = 30)

boton2 = tk.Button(text="Limpiar", command= limpiar)
boton2.place(x=275,y=90, width = 80, height = 20)

txt = tk.Entry()
txt.place(x=50,y=50, width = 120, height = 20)

txt2 = tk.Entry()
txt2.place(x=50,y=105, width = 120, height = 20)

label = tk.Label(text="Peso (kg)")
label.place(x=50, y=25,)

label3 = tk.Label(text="Altura (m)")
label3.place(x=50, y=80)

label2 = tk.Label(text="")
label2.place(x=150,y=150)


def  validarCampo(arg):
    
    try:
        arg = float(arg)
        return True
    except:
        return False
    








ventana.mainloop()
