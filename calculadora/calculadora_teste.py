from tkinter import *
import math

class Calculadora:
    def __init__(self, main):
        main.title('Calculadora')
        main.geometry('357x500+0+0')
        main.config(bg = 'gray')
        main.resizable(False,False)
        
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width = 17, bg = '#996633', font = ('Arial Bold', 28), textvariable = self.equation).place(x=0,y=0)
        
        numero_de_botoes_em_x = 4
        numero_de_botoes_em_y = 6
        lista_botoes_x = list(range(numero_de_botoes_em_x))
        lista_botoes_y = list(range(numero_de_botoes_em_y))
        cont = 0
        lista_text = ['sen','cos','tg', '√','(', ')', '%', '/', '1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+', 'C', '0', '.', '=']

        for y in lista_botoes_y:
            for x in lista_botoes_x:
                valor_x = x
                valor_y = y
                texto_botao = lista_text[cont]

                if texto_botao == '=':
                    comando = self.solve
                    cor = '#66CCCC'
                elif texto_botao == 'C':
                    comando = self.clean
                    cor = 'grey'
                else:
                    cor = 'orange'
                    if texto_botao == ('sen'):
                        comando = lambda: self.show('math.sin(math.radians(')
                    elif texto_botao == ('cos'):
                        comando = lambda: self.show('math.cos(math.radians(')
                    elif texto_botao == ('tg'):
                        comando = lambda: self.show('math.tan(math.radians(')
                    elif texto_botao == ('√'):
                        comando = lambda: self.show('math.sqrt(')
                    else:    
                        comando = lambda valor=texto_botao: self.show(valor)
                        

                Button(width=11, height=4, text=texto_botao, relief='flat', bg=cor, command=comando).place(x=90 * valor_x, y=50 + (75 * valor_y))
                cont += 1
    
    def show(self, valor):
        self.entry_value = self.entry_value + str(valor)
        self.equation.set(self.entry_value)
        
    def clean(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
        
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)
        
        
janela=Tk()
calculadora = Calculadora(janela)
janela.mainloop()
