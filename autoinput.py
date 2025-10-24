import customtkinter as ctk
from pynput.keyboard import Controller, Key
import time
import threading

def enviar_atalho():
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

def layout_arq():
    keyboard = Controller()

    time.sleep(0.5)
    keyboard.press(Key.shift)
    keyboard.press(Key.ctrl)
    keyboard.press('2')

    keyboard.release('2')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    print("Atalho Shift + Ctrl + 2 enviado!")

def colar_apos():
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
