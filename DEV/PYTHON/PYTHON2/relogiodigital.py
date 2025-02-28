from tkinter import *
from time import strftime


def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %P")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)


janela = Tk()
janela.title("relogio Digital Simples")


rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "bold"),
    background="light green",
    foreground="white"






)

rotulo_relogio.pack(anchor="center")

atualizar_relogio()

janela.mainloop()