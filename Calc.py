from tkinter import *

# .get() Retorna a variavel do entry.

# Talvez usando uma class avançada eu consigar usar é criar a função que entre em harmonia, com todo o sistema, porem ja tive um grande avanço, retornando o valor dos entry. 

Calc = Tk()
Calc.title("Calculadora")
Calc.geometry("165x200")

# Entrada de Dados

entry1 = Entry(Calc)
entry1.grid(column=0, row=1)

entry2 = Entry(Calc, )
entry2.grid(column=0, row=2)


# Funções 
def somar():
    n1 = entry1.get()
    n2 = entry2.get()
    re = int(n1) + int(n2)
    resul["text"] = re
    
          
def sub():
    n1 = entry1.get()
    n2 = entry2.get()
    re = int(n1) - int(n2)
    resul["text"] = re
          
                   
def div():
    n1 = entry1.get()
    n2 = entry2.get()
    re = int(n1) // int(n2)
    resul["text"] = re
                            

def multi():
    n1 = entry1.get()
    n2 = entry2.get()
    re = int(n1) * int(n2)
    resul["text"] = re
    
# Feito a calc, ainda precisa mudar grid() pelo place
          
soma = Button(Calc, text="+", command= somar )
soma.place(x= "50", y="70" )

divi = Button(Calc, text="  /", command= div)
divi.place(x="50", y="100")
# divi.grid(column=0 , row=3)

subi = Button(Calc, text=" - ", command=sub)
subi.place(x="90", y="70")

Mul = Button(Calc, text=" x", command= multi)
Mul.place(x="90", y="100")

resul = Label(Calc, text="***")
resul.grid(column=0, row=0)


Calc.mainloop()