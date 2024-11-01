from tkinter import *
import math

class Calculadora:
    def __init__(self, main):
        main.title('Calculadora')
        main.geometry('357x575+0+0')
        main.config(bg='gray')
        main.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#996633', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        comandos = {
            'sen': lambda: self.show('math.sin(math.radians('),
            'cos': lambda: self.show('math.cos(math.radians('),
            'tg': lambda: self.show('math.tan(math.radians('),
            '√': lambda: self.show('math.sqrt('),
            '=': self.solve,
            'C': self.clean
        }

        lista_text = ['sen', 'cos', 'tg', '√', '(', ')', '%', '/', '1', '2', '3', '*', '4', '5', '6', '-', '7', '8', '9', '+', 'C', '0', '.', '=']
        
        # Criando botões em uma grade de 4x6
        for posicao, texto_botao in enumerate(lista_text):
            comando = comandos.get(texto_botao, lambda valor=texto_botao: self.show(valor))
            
            cor = '#66CCCC' if texto_botao == '=' else ('grey' if texto_botao == 'C' else 'orange')
            
            Button(width=11, height=4, text=texto_botao, relief='flat', bg=cor, command=comando).place(x=90*(posicao % 4), y=50 + (75*(posicao // 4)))

    def show(self, valor):
        self.entry_value += str(valor)
        self.equation.set(self.entry_value)

    def clean(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

janela = Tk()
Calculadora(janela)
janela.mainloop()
