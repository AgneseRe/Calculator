import tkinter
import math
import tkinter.messagebox

def button_click(numero: float):
    # Catturo il numero eventualmente già presente sullo schermo
    numero_presente = schermo.get()
    # Pulisco lo schermo
    schermo.delete(0, tkinter.END)
    # Aggiornare lo schermo (concatenazione)
    schermo.insert(0, numero_presente + str(numero))

def button_add():
    primo_numero = schermo.get()
    # per avere il primo numero visibile all'esterno di button_add
    # NON è buona norma utilizzare la keyword 'global'
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    # setto operazione algebrica
    global operazione
    operazione = "+"

def button_subtract():
    primo_numero = schermo.get()
    # per avere il primo numero visibile all'esterno di button_add
    # NON è buona norma utilizzare la keyword 'global'
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "-"

def button_mult():
    primo_numero = schermo.get()
    # per avere il primo numero visibile all'esterno di button_add
    # NON è buona norma utilizzare la keyword 'global'
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "x"

def button_div():
    primo_numero = schermo.get()
    # per avere il primo numero visibile all'esterno di button_add
    # NON è buona norma utilizzare la keyword 'global'
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "/"

def calculate_perc():
    primo_numero = schermo.get()
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "%"

def calculate_sqrtN():
    primo_numero = schermo.get()
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "sqrtN"

def calculate_pow():
    primo_numero = schermo.get()
    global primo_numero_globale
    primo_numero_globale = float(primo_numero)
    schermo.delete(0, tkinter.END)
    global operazione
    operazione = "^"

def button_equal():
    secondo_numero = schermo.get()
    schermo.delete(0, tkinter.END)
    # gestione operazione algebrica (+, -, *, /)
    if operazione == "+":
        schermo.insert(0, f"{(primo_numero_globale + float(secondo_numero)):.4f}")
    elif operazione == "-":
        schermo.insert(0, f"{(primo_numero_globale - float(secondo_numero)):.4f}")
    elif operazione == "x":
        schermo.insert(0, f"{(primo_numero_globale * float(secondo_numero)):.4f}")
    elif operazione == "/":
        schermo.insert(0, f"{(primo_numero_globale / float(secondo_numero)):.4f}")
    elif operazione == "%":  
        schermo.insert(0, f"{primo_numero_globale * (float(secondo_numero)/100):4f}")
    elif operazione == "sqrtN":
        schermo.insert(0, f"{math.pow(primo_numero_globale, 1/float(secondo_numero)):.4f}")
    else: # operazione == "^":
        schermo.insert(0, f"{math.pow(primo_numero_globale, float(secondo_numero))}")

def button_clear():
    """ associata al tasto CANC """
    schermo.delete(0, tkinter.END)


# Creazione della finestra
window = tkinter.Tk()
window.title("CalCOOLatore")
window.iconbitmap("icons8-calcolatrice-di-mele-48.ico")
# window.geometry("300x300")

# schermo=tkinter.Entry(window, font=("Verdana", 20, "bold"), background="#bcc3d5", width=15, borderwidth=5)
schermo = tkinter.Entry(window, width = 40, borderwidth = 5, justify = "left",
                       background = "#000000", foreground = "#00ff00")
schermo.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 15)

# Creazione dei bottoni
button1 = tkinter.Button(window, text = "1", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(1))
button2 = tkinter.Button(window, text = "2", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(2))
button3 = tkinter.Button(window, text = "3", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(3))
button4 = tkinter.Button(window, text = "4", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(4))
button5 = tkinter.Button(window, text = "5", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(5))
button6 = tkinter.Button(window, text = "6", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(6))
button7 = tkinter.Button(window, text = "7", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(7))
button8 = tkinter.Button(window, text = "8", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(8))
button9 = tkinter.Button(window, text = "9", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(9))
button0 = tkinter.Button(window, text = "0", padx = 40, pady = 10, borderwidth = 3, command = lambda: button_click(0))
button_piu = tkinter.Button(window, text = "+", background = "#BBD2EC", borderwidth = 3,
                                activebackground = "#DFE9F5", padx = 39, pady = 10, command = button_add)
button_pulizia = tkinter.Button(window, text = "CANC", background = "#BBD2EC", borderwidth = 3,
                                activebackground = "#DFE9F5", padx = 74, pady = 10, command = button_clear)
button_uguale = tkinter.Button(window, text = "=", background = "#2271B3", borderwidth = 3,
                                activebackground = "#DFE9F5", foreground = "white", padx = 87, pady = 10, command = button_equal)
button_meno = tkinter.Button(window, text = "-", background = "#BBD2EC", borderwidth = 3,
                                activebackground = "#DFE9F5", padx = 40, pady = 10, command = button_subtract)
button_molt = tkinter.Button(window, text = "x", background = "#BBD2EC", borderwidth = 3,
                                activebackground = "#DFE9F5", padx = 40, pady = 10, command = button_mult)
button_divi = tkinter.Button(window, text = "/", background = "#BBD2EC", borderwidth = 3,
                                activebackground = "#DFE9F5", padx = 40, pady = 10, command = button_div)
button_perc = tkinter.Button(window, text = "%", background = "#ffbf82", borderwidth = 3, 
                                padx = 38, pady = 10, command = calculate_perc)
button_sqrt = tkinter.Button(window, text = "\u221A", background = "#FFBF82", borderwidth = 3, 
                                padx = 38, pady = 10, command = calculate_sqrtN)
button_pow = tkinter.Button(window, text = "x\u207f", background = "#FFBF82", borderwidth = 3, 
                                padx = 38, pady = 10, command = calculate_pow)

# Posizionamento bottoni
button1.grid(row = 3, column = 0, padx = (10, 1), pady = 1)
button2.grid(row = 3, column = 1, padx = (0, 1), pady = 1)
button3.grid(row = 3, column = 2, padx = (0, 10), pady = 1)

button4.grid(row = 2, column = 0, padx = (10, 1), pady = 1)
button5.grid(row = 2, column = 1, padx = (0, 1), pady = 1)
button6.grid(row = 2, column = 2, padx = (0, 10), pady = 1)

button7.grid(row = 1, column = 0, padx = (10, 1), pady = 1)
button8.grid(row = 1, column = 1, padx = (0, 1), pady = 1)
button9.grid(row = 1, column = 2, padx = (0, 10), pady = 1)

button0.grid(row = 4, column = 0, padx = (10, 1), pady = 1)

button_pulizia.grid(row = 4, column = 1, columnspan = 2, padx = (0, 10), pady = 1)
button_piu.grid(row = 5, column = 0, padx = (10, 1), pady = 1)
button_uguale.grid(row = 5, column = 1, columnspan = 2, padx = (0, 10), pady = 1)

button_meno.grid(row = 6, column = 0, padx = (10, 1), pady = 1)
button_molt.grid(row = 6, column = 1, padx = (0, 1), pady = 1)
button_divi.grid(row = 6, column = 2, padx = (0, 10), pady = 1)

button_perc.grid(row = 7, column = 0, padx = (10, 0), pady = (1, 10))
button_sqrt.grid(row = 7, column = 1, padx = (0, 1), pady = (1, 10))
button_pow.grid(row = 7, column = 2, padx = (0, 10), pady = (1, 10))


window.mainloop()