import random
import numpy as np
import PySimpleGUI as sg
import pygame

alo = []

def mezclar():
        lista = ['do','re','mi','fa','sol','la','si','DO_','RE_','MI_','FA_','SOL_','LA_','SI_']
        for i in range(8):
            alo.append(lista[np.random.randint(low=0,high=len(lista))])

mezclar()

def separar_audio(audio):
    ad=f'audio_notas_fa/{audio}.wav'
    return ad


def separar_imagen(imagen):
    img=f'imagen_notas_fa/{imagen}.png'
    return img

def hacer_juego_fa_1():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[0]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_1f = separar_audio(alo[0])
    
def hacer_juego_fa_2():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[1]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_2f = separar_audio(alo[1])

def hacer_juego_fa_3():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[2]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_3f = separar_audio(alo[2])

def hacer_juego_fa_4():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[3]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_4f = separar_audio(alo[3])

def hacer_juego_fa_5():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[4]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_5f = separar_audio(alo[4])

def hacer_juego_fa_6():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[5]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_6f = separar_audio(alo[5])

def hacer_juego_fa_7():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[6]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_7f = separar_audio(alo[6])

def hacer_juego_fa_8():
    ly_fa = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(alo[7]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Ver puntuación')]
        ]
    return sg.Window("Juego en clave de fa", ly_fa)

music_8f = separar_audio(alo[7])