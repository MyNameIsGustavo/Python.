#Bibliotecas importadas;
from cgitb import text
import re
from tkinter import *
from tkinter import ttk
from turtle import color, st
from unittest import result

#Biblioteca de cores;
cor1 = '#BFBFBF'
cor2 = '#262626'
cor3 = '#000000'
cor4 = '#ffffff'

#Configurações da interface;
janela = Tk()
janela.title("Calculadora")
janela.iconbitmap('Calc_Icone.ico')
janela.geometry("400x550")

#Frames do display;
frmDisplay = Frame(janela, width=400, height=125, bg='#0852c9')
frmDisplay.grid(row=0, column=0)

#Frames inferiores;
frmInferiores = Frame(janela, width=400, height=550)
frmInferiores.grid(row=1, column=0)

#Desenvolvimento da lógica do display;
todos_valores = ''
valor_texto= StringVar() 

#Função de exibição;
def Entrada_Dados(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

#Função de exibição do calculo;
def calcular():
    global todos_valores
    
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#Função de limpação dos dados;
def limpar_tela():
    global todos_valores

    todos_valores = ""
    valor_texto.set("")

#Frame do display;
Display_label = Label(frmDisplay, textvariable=valor_texto, font=('Poppins 20'), width=25, height=4, justify=RIGHT)
Display_label.place(x=0, y=0)

#Frames dos botões - Primeira linha;
btnAC = Button(frmInferiores,command=limpar_tela, text="AC", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnAC.place(x=0, y=0)
btnMod = Button(frmInferiores, command=lambda:Entrada_Dados('%'), text="MOD", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnMod.place(x=100, y=0)
btnDiv = Button(frmInferiores, command=lambda:Entrada_Dados('/'),text="/", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnDiv.place(x=200, y=0)
btnVezes = Button(frmInferiores, command=lambda:Entrada_Dados('*'),text="*", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnVezes.place(x=300, y=0)

#Frames dos botões - Segunda linha;
btn7 = Button(frmInferiores, command=lambda:Entrada_Dados('7'),text="7", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn7.place(x=0, y=85)
btn8 = Button(frmInferiores, command=lambda:Entrada_Dados('8'),text="8", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn8.place(x=100, y=85)
btn9 = Button(frmInferiores, command=lambda:Entrada_Dados('9'),text="9", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn9.place(x=200, y=85)
btnMais = Button(frmInferiores, command=lambda:Entrada_Dados('+'),text="+", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnMais.place(x=300, y=85)

#Frames dos botões - Terceira linha;
btn4 = Button(frmInferiores, command=lambda:Entrada_Dados('4'),text="4", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn4.place(x=0, y=170)
btn5 = Button(frmInferiores, command=lambda:Entrada_Dados('5'),text="5", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn5.place(x=100, y=170)
btn6 = Button(frmInferiores, command=lambda:Entrada_Dados('6'),text="6", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn6.place(x=200, y=170)
btnMenos = Button(frmInferiores, command=lambda:Entrada_Dados('-'),text="-", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE, bg=cor1)
btnMenos.place(x=300, y=170)

#Frames dos botões - Quarta linha;
btn1 = Button(frmInferiores, command=lambda:Entrada_Dados('1'),text="1", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn1.place(x=0, y=255)
btn2 = Button(frmInferiores, command=lambda:Entrada_Dados('2'),text="2", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn2.place(x=100, y=255)
btn3 = Button(frmInferiores, command=lambda:Entrada_Dados('3'),text="3", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn3.place(x=200, y=255)

#Frames dos botões - Quinta linha;
btn0 = Button(frmInferiores, command=lambda:Entrada_Dados('0'), text="0", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btn0.place(x=0, y=340)
btnPonto = Button(frmInferiores, command=lambda:Entrada_Dados('.'), text=".", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btnPonto.place(x=100, y=340)
btnApagar = Button(frmInferiores, command=limpar_tela, text="DEL", width=10, height=4, font=('Poppins 12'), overrelief=RIDGE)
btnApagar.place(x=200, y=340)
btnIgual = Button(frmInferiores, command=calcular, text="=", width=9, height=7, font=('Poppins 14'), overrelief=RIDGE, bg=cor3, fg=cor4)
btnIgual.place(x=300, y=255)

janela.mainloop()