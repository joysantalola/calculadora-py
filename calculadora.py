import tkinter as tk

# Variables globals (Es fan servir per tal de poder moure més fàcilment les funcions al programa)
operacio = ""
resultat = 0

# Funcions per a les operacions
def afegir_numero(num):
    global operacio
    operacio += str(num)
    lbl_calculadora.config(text=operacio)
    
def afegir_0():
    afegir_numero(0)

def afegir_1():
    afegir_numero(1)

def afegir_2():
    afegir_numero(2)

def afegir_3():
    afegir_numero(3)

def afegir_4():
    afegir_numero(4)

def afegir_5():
    afegir_numero(5)

def afegir_6():
    afegir_numero(6)

def afegir_7():
    afegir_numero(7)

def afegir_8():
    afegir_numero(8)

def afegir_9():
    afegir_numero(9)

def afegir_punt():
    afegir_numero(".")

def afegir_mes():
    afegir_numero("+")

def afegir_menys():
    afegir_numero("-")

def afegir_multiplicar():
    afegir_numero("*")

def afegir_divisio():
    afegir_numero("/")


def calcular():
    global operacio, resultat
    try:
        resultat = eval(operacio)
        lbl_calculadora.config(text=resultat)
        operacio = str(resultat)
    except:
        lbl_calculadora.config(text="Error")
        operacio = ""

def esborrar():
    global operacio
    operacio = ""
    lbl_calculadora.config(text="")

# Programa principal
#finestra
finestra = tk.Tk()
finestra.title("Calculadora")

lbl_calculadora = tk.Label(finestra, text="", width=20, height=2)
lbl_calculadora.grid(row=0, column=0, columnspan=4)

# Creació dels botons
btn_7 = tk.Button(finestra, text="7", command=afegir_7, width=5, height=2) #7
btn_8 = tk.Button(finestra, text="8", command=afegir_8, width=5, height=2) #8
btn_9 = tk.Button(finestra, text="9", command=afegir_9, width=5, height=2) #9
btn_4 = tk.Button(finestra, text="4", command=afegir_4, width=5, height=2) #4 
btn_5 = tk.Button(finestra, text="5", command=afegir_5, width=5, height=2) #5
btn_6 = tk.Button(finestra, text="6", command=afegir_6, width=5, height=2) #6
btn_1 = tk.Button(finestra, text="1", command=afegir_1, width=5, height=2) #1
btn_2 = tk.Button(finestra, text="2", command=afegir_2, width=5, height=2) #2
btn_3 = tk.Button(finestra, text="3", command=afegir_3, width=5, height=2) #3
btn_0 = tk.Button(finestra, text="0", command=afegir_0, width=5, height=2) #0
btn_punt = tk.Button(finestra, text=".", command=afegir_punt, width=5, height=2) #punt
btn_barra = tk.Button(finestra, text="/", command=afegir_divisio, width=5, height=2) #barra
btn_multiplicar = tk.Button(finestra, text="*", command=afegir_multiplicar, width=5, height=2) #multiplicar
btn_menys = tk.Button(finestra, text="-", command=afegir_menys, width=5, height=2) #menys
btn_mes = tk.Button(finestra, text="+", command=afegir_mes, width=5, height=2) #mes
btn_igual = tk.Button(finestra, text="=", command=calcular, width=5, height=2) #igual
btn_c = tk.Button(finestra, text="C", command=esborrar, width=25, height=2) #borrar

# Posicionament dels botons
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_barra.grid(row=1, column=3)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_multiplicar.grid(row=2, column=3)
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_menys.grid(row=3, column=3)
btn_0.grid(row=4, column=0)
btn_punt.grid(row=4, column=1)
btn_mes.grid(row=4, column=2)
btn_igual.grid(row=4, column=3)
btn_c.grid(row=5, column=0, columnspan=4)

finestra.mainloop() #evitar que es tenqui la finestra
