# Criar uma calculadora com +,-, *, /

from tkinter import *
Calc = Tk()

# Funçoes
    
def soma(self,*num):
    self.n = self.num
    self.n+= self.n
    # exibir["text"] = num
    return self.n
    

def sub(self,*num):
    self.n = self.num
    for self.c in self.n:
        self.c = self.c - self.n
        return self.c
    

def mult(self,*num):
    self.n = self.num
    for self.c in self.n:
        self.c = self.n * self.c
        return self.c


def div(self,*num):
    self.n = self.num
    for self.c in self.n:
        self.c = self.c // self.n
        return self.c




#   Programa 
Calc.title("Calculadora")
# Calc.geometry("50x50")

#Botoes Numericos
entra1 = Entry(Calc,width=20)
entra1.grid(column=0, row=0)

entra2 = Entry(Calc, width=20)
entra2.grid(column=0, row=1)

    

resul = Button(Calc, text="=")
resul.grid(column=1, row=5)

#Botoes Aritimeticos
somas = Button(Calc, text="+", command= soma)
somas.grid(column=0, row=2,padx=5, pady=5)

dive = Button(Calc, text="/", command= div)
dive.grid(column=1,row=2, padx=0, pady=5)

multi = Button(Calc, text="X", command= mult)
multi.grid(column=1, row=3, padx=5, pady=5)


subr = Button(Calc, text="-", command= sub)
subr.grid(column=0, row=3,padx=5, pady=5)


# Mostra Tela 
exibir = Label(Calc, text=f"Resultado...")
exibir.grid(column=0, row=5)
    
    
Calc.mainloop()
    


    
