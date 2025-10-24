import customtkinter as ctk
from pynput.keyboard import Controller, Key
import time, threading

from fabric import ButtonFactory
from autoinput import (
    enviar_atalho, 
    layout_arq, 
    colar_apos
    )

app = ctk.CTk()
app.title("Atalhos Lore")
app.geometry("240x260")
app.resizable(True, True)
app.attributes("-topmost", True)

card = ctk.CTkFrame(app, fg_color="#0f2230")
card.pack(fill="both", expand=True, padx=0, pady=0)

factory = ButtonFactory(card)

botoes = [
    dict(text="Exportar",   command=enviar_atalho, tooltip="Exportar Photoshop"),
    dict(text="Layout",     command=layout_arq,    tooltip="Mudar_Layout"),
    dict(text="Colar após", command=colar_apos,    tooltip="Colar_Final")
]

for spec in botoes:
    factory.make(**spec)

app.mainloop()
