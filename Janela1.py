import tkinter as tk
from tkinter import *

# Janela principal 
janela = tk.Tk()
janela.title("Minha Primeira Interface Gráfica")
janela.geometry("400x300")

# 2 Adiciona um texto 
texto = tk.Label(janela, text="Olá! Bem-vindo ao Tkinter.")
texto.pack(pady=20)

def alterar_texto():
    texto.config(text="Clicado com sucesso!")

# 4 Adicionar um botao

botao = tk.Button(janela, text="Clique Aqui", command=alterar_texto)
botao.pack()

janela.mainloop()


