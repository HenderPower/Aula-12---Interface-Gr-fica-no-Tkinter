import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Minha Primeira Interface Gráfica")
janela.geometry("400x300")

# 2 Adiciona um texto 
texto = tk.Label(janela, text="Olá! Bem-vindo ao Tkinter.")
texto.pack(pady=20)

janela.mainloop()


