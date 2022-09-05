
import random
import numpy as np
import PySimpleGUI as sg
import pygame

# lista = ['do','re','mi','fa','sol','la','si','DO_','RE_','MI_','FA_','SOL_','LA_','SI_']

# # def mezclar(lista):
# simple = []
# simple = [lista[np.random.randint(low=0,high=len(lista))]]
# abeja=f'imagen_de_notas/{random.choice(simple)}.png'

ale = []

def mezclar():
        lista = ['do','re','mi','fa','sol','la','si','DO_','RE_','MI_','FA_','SOL_','LA_','SI_']
        for i in range(8):
            ale.append(lista[np.random.randint(low=0,high=len(lista))])

mezclar()

def separar_audio(audio):
    ad=f'audio_notas_sol/{audio}.wav'
    return ad


def separar_imagen(imagen):
    img=f'imagen_notas_sol/{imagen}.png'
    return img

# print (ale)
# separar_audio(ale[0])
# separar_imagen(ale[0])

def hacer_juego_sol_1():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[0]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_1 = separar_audio(ale[0])
    
def hacer_juego_sol_2():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[1]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_2 = separar_audio(ale[1])

def hacer_juego_sol_3():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[2]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_3 = separar_audio(ale[2])

def hacer_juego_sol_4():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[3]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_4 = separar_audio(ale[3])

def hacer_juego_sol_5():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[4]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_5 = separar_audio(ale[4])

def hacer_juego_sol_6():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[5]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_6 = separar_audio(ale[5])

def hacer_juego_sol_7():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[6]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Siguiente')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_7 = separar_audio(ale[6])

def hacer_juego_sol_8():
    ly_sol = [
        [sg.Text("Práctica con un pentagrama en clave de sol")],
        [sg.Button('REPRODUCIR')],
        [sg.Image(separar_imagen(ale[7]))], #aqui va un ramdom
        [sg.Text('¿Qué nota musical es?')],[sg.InputText()],
        [sg.Button('OK')],[sg.Button('Cancel')],
        [sg.Button('Ver puntuación')]
        ]
    return sg.Window("Juego en clave de sol", ly_sol)

music_8 = separar_audio(ale[7])
