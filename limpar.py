from pynput.keyboard import Controller, Key

def limpar_teclado():
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

    print("✅ Todas as teclas liberadas.")

limpar_teclado()
