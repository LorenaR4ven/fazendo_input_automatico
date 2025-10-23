import customtkinter as ctk
from pynput.keyboard import Controller, Key
import time
import threading

def enviar_atalho():
    def baixarphotoshop():
        keyboard = Controller()

        time.sleep(1.0)
        keyboard.press(Key.shift)
        keyboard.press(Key.alt)
        keyboard.press(Key.ctrl)
        keyboard.press('w')

        keyboard.release('w')
        keyboard.release(Key.ctrl)
        keyboard.release(Key.alt)
        keyboard.release(Key.shift)
        print("Atalho Shift + Alt + Ctrl + W enviado!")
    threading.Thread(target=baixarphotoshop).start() 

def layout_arq():
    def definir_layout():
        keyboard = Controller()

        time.sleep(0.5)
        keyboard.press(Key.shift)
        keyboard.press(Key.ctrl)
        keyboard.press('2')

        keyboard.release('2')
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        print("Atalho Shift + Ctrl + 2 enviado!")
    threading.Thread(target=definir_layout).start()

def colar_apos():
    def colarapos():
        keyboard = Controller()

        time.sleep(1.5)
        keyboard.tap(Key.f2)
        time.sleep(0.2)
        keyboard.tap(Key.right)

        time.sleep(0.2)
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl)

        time.sleep(0.2)
        keyboard.tap(Key.enter)
        time.sleep(0.2)
        keyboard.tap(Key.right)

        print("colar_após enviado!")
    threading.Thread(target=colarapos).start()


# --- Configuração da janela ---

app = ctk.CTk()
app.title("Painel")
app.geometry("240x260")
app.resizable(True, True)
app.attributes("-topmost", True)

card = ctk.CTkFrame(app, fg_color="#0f2230")
card.pack(fill="both", expand=True, padx=0, pady=0)

# ctk.CTkLabel(card, text="").pack(pady=8)

# Botão branco "Exportar"
def acao_exportar():
    enviar_atalho()

btn_exportar = ctk.CTkButton(
    card,
    text="Exportar",
    command=acao_exportar,
    height=30,
    corner_radius=14,
    fg_color="#ffffff",
    hover_color="#e9e9e9",
    text_color="#0f2230"
)
btn_exportar.pack(pady=(6,6), padx=18, fill="x")

def acao_definir_layout():
    layout_arq()

btn_layout = ctk.CTkButton(
    card,
    text="Layout",
    command=acao_definir_layout,
    height=30,
    corner_radius=14,
    fg_color="#ffffff",
    hover_color="#e9e9e9",
    text_color="#0f2230"
)
btn_layout.pack(pady=(6, 6), padx=18, fill="x")

def acao_colar_apos():
    colar_apos()

btn_layout = ctk.CTkButton(
    card,
    text="colar após",
    command=acao_colar_apos,
    height=30,
    corner_radius=14,
    fg_color="#ffffff",
    hover_color="#e9e9e9",
    text_color="#0f2230"
)
btn_layout.pack(pady=(6, 6), padx=18, fill="x")

# spacer = ctk.CTkLabel(card, text="")
# spacer.pack(expand=True)

def limpar_teclado(_event=None):
    keyboard = Controller()
    todas_teclas = [
        Key.alt, Key.alt_l, Key.alt_r,
        Key.ctrl, Key.ctrl_l, Key.ctrl_r,
        Key.shift, Key.shift_l, Key.shift_r,
        Key.cmd, Key.cmd_l, Key.cmd_r,
        Key.caps_lock, Key.tab, Key.esc,
        Key.enter, Key.space,
        *[chr(i) for i in range(32, 127)]
    ]

    for tecla in todas_teclas:
        try:
            keyboard.release(tecla)
        except Exception:
            pass

lbl_limpar = ctk.CTkLabel(card, text="Limpar tudo", text_color="#ffffff", font=ctk.CTkFont(size=16, weight="bold"))
lbl_limpar.pack(pady=(0, 18))

# torna clicável
lbl_limpar.bind("<Button-1>", limpar_teclado)
lbl_limpar.bind("<Enter>", lambda e: lbl_limpar.configure(text_color="#cfe3ff"))
lbl_limpar.bind("<Leave>", lambda e: lbl_limpar.configure(text_color="#ffffff"))

app.mainloop()