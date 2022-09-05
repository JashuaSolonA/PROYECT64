import pygame
import PySimpleGUI as sg
import random
import numpy as np
import pru
import pru_2

class Interface:
    
    def reproductor(cancion):
        pygame.mixer.init(frequency=44100)
        pygame.mixer.music.load(str(cancion))
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(1)

    def hacer_saludo():
        ly_saludo = [  [sg.Text("Este programa de ayudará a identificar las notas musicales en el pentagrama", text_color = "Black")],
                [sg.Text("Introduce tu nombre: "), sg.Input()],
                [sg.Button("OK")], [sg.Button("Salir")]
                ]
        return sg.Window("Proyecto Grupo 08: Aprende a leer el pentagrama", ly_saludo)

    def hacer_inicio():
        ly_inicio = [  [sg.Button("Aprende las notas musicales")],
                [sg.Button("Pon en práctica tus conocimientos")],
                [sg.Button('Ranking')],
                [sg.Button("Salir de la aplicación")]
                ]   
        return sg.Window("Menú inicio", ly_inicio)

    def hacer_aprender():
        ly_aprender = [ [sg.Text("Estas son las notas ubicadas en el pentagrama en clave de sol:")],
                [sg.Image("recursos2/clave_de_sol.png")],
                [sg.Text("Estas son las notas ubicadas en el pentagrama en clave de fa:")],
                [sg.Image("recursos2/clave_de_fa.png")],
                [sg.Button("Salir de la aplicación")]
                ]
        return sg.Window("Aprende la ubicación de las notas musicales", ly_aprender)

    def hacer_elegir():
        ly_elegir = [  [sg.Text("Elige la clave de tu preferencia")],
                [sg.Button("sol")],
                [sg.Button("fa")],
                [sg.Button("Salir de la aplicación")],
                [sg.Text('AVISO: Para una nota grave utiliza minúsculas y para una aguda, mayúsculas acompañada con un guión bajo')],
                [sg.Text('Ejemplo: mi (en caso de grave)  MI_ (en caso de aguda)')]
                ]
        return sg.Window("Elige la clave", ly_elegir)
    
    b=[]

    def lim():
        f=open('file.txt','r')
        a=f.read()
        Interface.b.append(a)
        f.close
    
    def hacer_puntuacion():
        ly_lima = [
            [sg.Text(Interface.b[0])],
            [sg.Button('Salir')]
        ]
        return sg.Window('puntuacion final',ly_lima)

Interface.lim()

pygame.mixer.init(frequency=44100)

pygame.mixer.music.load('recursos2/Allegro_Otoño.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

size = 900, 600

VENTANA = pygame.display.set_mode(size)
pygame.display.set_caption('Musica de fondo')
Imagen = pygame.image.load('recursos2/icono.png')
pygame.display.set_icon(Imagen)

fondo = pygame.image.load('recursos2/fondo.png')
VENTANA.blit(fondo,(0,0))

ejecuta = True

while ejecuta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    
    pygame.display.update()
    sg.theme("DarkBlue8")

    saludo = Interface.hacer_saludo()
    inicio = Interface.hacer_inicio()
    aprender = Interface.hacer_aprender()
    elegir = Interface.hacer_elegir()
    puntuacion = Interface.hacer_puntuacion()
    juego_sol_1 = pru.hacer_juego_sol_1()
    juego_sol_2 = pru.hacer_juego_sol_2()
    juego_sol_3 = pru.hacer_juego_sol_3()
    juego_sol_4 = pru.hacer_juego_sol_4()
    juego_sol_5 = pru.hacer_juego_sol_5()
    juego_sol_6 = pru.hacer_juego_sol_6()
    juego_sol_7 = pru.hacer_juego_sol_7()
    juego_sol_8 = pru.hacer_juego_sol_8()
    juego_fa_1 = pru_2.hacer_juego_fa_1()
    juego_fa_2 = pru_2.hacer_juego_fa_2()
    juego_fa_3 = pru_2.hacer_juego_fa_3()
    juego_fa_4 = pru_2.hacer_juego_fa_4()
    juego_fa_5 = pru_2.hacer_juego_fa_5()
    juego_fa_6 = pru_2.hacer_juego_fa_6()
    juego_fa_7 = pru_2.hacer_juego_fa_7()
    juego_fa_8 = pru_2.hacer_juego_fa_8()

    try:
        while True:
            event, values = saludo.read()
            if event == "Salir"  or event == sg.WIN_CLOSED:
                break
            if event == "OK":
                sg.popup_ok("Bienvenido/a " + values[0] + ". ¿Estás listo/a para empezar a aprender?")
                saludo.close()
                while True:
                    event, values = inicio.read()
                    if event == "Salir de la aplicación"  or event == sg.WIN_CLOSED:
                        break
                    if event == 'Ranking':
                        inicio.close()
                        while True:
                            event, values = puntuacion.read()
                            if event == "Salir"  or event == sg.WIN_CLOSED:
                                break
                    if event == "Aprende las notas musicales":
                        inicio.close()
                        while True:
                            event, values = aprender.read()
                            if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                                break
                    elif event == "Pon en práctica tus conocimientos":
                        inicio.close()
                        while True:
                            event, values = elegir.read()
                            if event == "Salir de la aplicación" or event == sg.WIN_CLOSED:
                                break
                            if event == "sol":
                                elegir.close()
                                while True:
                                    event, values = juego_sol_1.read()
                                    if event == 'REPRODUCIR':
                                        Interface.reproductor(pru.music_1)
                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                        break
                                    elif values[1] == '':
                                        pass
                                    elif values[1] != str(pru.ale[0]):
                                        sg.popup_ok('Incorrecto :c')
                                        f = open("file.txt", "a")
                                        f.write("1(❌)")
                                        f.close
                                    else:
                                        sg.popup_ok('Felicitaciones')
                                        f = open("file.txt", "a")
                                        f.write("1(✔️)")
                                        f.close
                                    if event == 'Siguiente':
                                        juego_sol_1.close()
                                        while True:
                                            event, values = juego_sol_2.read()
                                            if event == 'REPRODUCIR':
                                                Interface.reproductor(pru.music_2)
                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                break
                                            elif values[1] == '':
                                                pass
                                            elif values[1] != str(pru.ale[1]):
                                                sg.popup_ok('Incorrecto :c')
                                                f = open("file.txt", "a")
                                                f.write("2(❌)")
                                                f.close
                                            else:
                                                sg.popup_ok('Felicitaciones')
                                                f = open("file.txt", "a")
                                                f.write("2(✔️)")
                                                f.close                                        
                                            if event == 'Siguiente':
                                                juego_sol_2.close()
                                                while True:
                                                    event, values = juego_sol_3.read()
                                                    if event == 'REPRODUCIR':
                                                        Interface.reproductor(pru.music_3)
                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                        break
                                                    elif values[1] == '':
                                                        pass
                                                    elif values[1] != str(pru.ale[2]):
                                                        sg.popup_ok('Incorrecto :c')
                                                        f = open("file.txt", "a")
                                                        f.write("3(❌)")
                                                        f.close
                                                    else:
                                                        sg.popup_ok('Felicitaciones')
                                                        f = open("file.txt", "a")
                                                        f.write("3(✔️)")
                                                        f.close                                                  
                                                    if event == 'Siguiente':
                                                        juego_sol_3.close()
                                                        while True:
                                                            event, values = juego_sol_4.read()
                                                            if event == 'REPRODUCIR':
                                                                Interface.reproductor(pru.music_4)
                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                break
                                                            elif values[1] == '':
                                                                pass
                                                            elif values[1] != str(pru.ale[3]):
                                                                sg.popup_ok('Incorrecto :c')
                                                                f = open("file.txt", "a")
                                                                f.write("4(❌)")
                                                                f.close
                                                            else:
                                                                sg.popup_ok('Felicitaciones')
                                                                f = open("file.txt", "a")
                                                                f.write("4(✔️)")
                                                                f.close                                                             
                                                            if event == 'Siguiente':
                                                                juego_sol_4.close()
                                                                while True:
                                                                    event, values = juego_sol_5.read()
                                                                    if event == 'REPRODUCIR':
                                                                        Interface.reproductor(pru.music_5)
                                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                                        break
                                                                    elif values[1] == '':
                                                                        pass
                                                                    elif values[1] != str(pru.ale[4]):
                                                                        sg.popup_ok('Incorrecto :c')
                                                                        f = open("file.txt", "a")
                                                                        f.write("5(❌)")
                                                                        f.close
                                                                    else:
                                                                        sg.popup_ok('Felicitaciones')
                                                                        f = open("file.txt", "a")
                                                                        f.write("5(✔️)")
                                                                        f.close                                                                      
                                                                    if event == 'Siguiente':
                                                                        juego_sol_5.close()
                                                                        while True:
                                                                            event, values = juego_sol_6.read()
                                                                            if event == 'REPRODUCIR':
                                                                                Interface.reproductor(pru.music_6)
                                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                break
                                                                            elif values[1] == '':
                                                                                pass
                                                                            elif values[1] != str(pru.ale[5]):
                                                                                sg.popup_ok('Incorrecto :c')
                                                                                f = open("file.txt", "a")
                                                                                f.write("6(❌)")
                                                                                f.close
                                                                            else:
                                                                                sg.popup_ok('Felicitaciones')
                                                                                f = open("file.txt", "a")
                                                                                f.write("6(✔️)")
                                                                                f.close                                                                             
                                                                            if event == 'Siguiente':
                                                                                juego_sol_6.close()
                                                                                while True:
                                                                                    event, values = juego_sol_7.read()
                                                                                    if event == 'REPRODUCIR':
                                                                                        Interface.reproductor(pru.music_7)
                                                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                        break
                                                                                    elif values[1] == '':
                                                                                        pass
                                                                                    elif values[1] != str(pru.ale[6]):
                                                                                        sg.popup_ok('Incorrecto :c')
                                                                                        f = open("file.txt", "a")
                                                                                        f.write("7(❌)")
                                                                                        f.close
                                                                                    else:
                                                                                        sg.popup_ok('Felicitaciones')
                                                                                        f = open("file.txt", "a")
                                                                                        f.write("7(✔️)")
                                                                                        f.close                                                                                     
                                                                                    if event == 'Siguiente':
                                                                                        juego_sol_7.close()
                                                                                        while True:
                                                                                            event, values = juego_sol_8.read()
                                                                                            if event == 'REPRODUCIR':
                                                                                                Interface.reproductor(pru.music_8)
                                                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                                break
                                                                                            elif values[1] == '':
                                                                                                pass
                                                                                            elif values[1] != str(pru.ale[7]):
                                                                                                sg.popup_ok('Incorrecto :c')
                                                                                                f = open("file.txt", "a")
                                                                                                f.write("8(❌) JuegoSol")
                                                                                                f.close
                                                                                            else:
                                                                                                sg.popup_ok('Felicitaciones')
                                                                                                f = open("file.txt", "a")
                                                                                                f.write("8(✔️) JuegoSol")
                                                                                                f.close
                                                                                            if event == 'Finalizar':
                                                                                                juego_sol_8.close()


                            elif event =="fa":
                                elegir.close()
                                while True:
                                    event, values = juego_fa_1.read()
                                    if event == 'REPRODUCIR':
                                        Interface.reproductor(pru_2.music_1f)
                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                        break
                                    elif values[1] == '':
                                        pass
                                    elif values[1] != str(pru_2.alo[0]):
                                        sg.popup_ok('Incorrecto :c')
                                        f = open("file.txt", "a")
                                        f.write("1(❌)")
                                        f.close
                                    else:
                                        sg.popup_ok('Felicitaciones')
                                        f = open("file.txt", "a")
                                        f.write("1(✔️)")
                                        f.close
                                    if event == 'Siguiente':
                                        juego_fa_1.close()
                                        while True:
                                            event, values = juego_fa_2.read()
                                            if event == 'REPRODUCIR':
                                                Interface.reproductor(pru_2.music_2f)
                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                break
                                            elif values[1] == '':
                                                pass
                                            elif values[1] != str(pru_2.alo[1]):
                                                sg.popup_ok('Incorrecto :c')
                                                f = open("file.txt", "a")
                                                f.write("2(❌)")
                                                f.close
                                            else:
                                                sg.popup_ok('Felicitaciones')
                                                f = open("file.txt", "a")
                                                f.write("2(✔️)")
                                                f.close
                                            if event == 'Siguiente':
                                                juego_fa_2.close()
                                                while True:
                                                    event, values = juego_fa_3.read()
                                                    if event == 'REPRODUCIR':
                                                        Interface.reproductor(pru_2.music_3f)
                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                        break
                                                    elif values[1] == '':
                                                        pass
                                                    elif values[1] != str(pru_2.alo[2]):
                                                        sg.popup_ok('Incorrecto :c')
                                                        f = open("file.txt", "a")
                                                        f.write("3(❌)")
                                                        f.close
                                                    else:
                                                        sg.popup_ok('Felicitaciones')
                                                        f = open("file.txt", "a")
                                                        f.write("3(✔️)")
                                                        f.close
                                                    if event == 'Siguiente':
                                                        juego_fa_3.close()
                                                        while True:
                                                            event, values = juego_fa_4.read()
                                                            if event == 'REPRODUCIR':
                                                                Interface.reproductor(pru_2.music_4f)
                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                break
                                                            elif values[1] == '':
                                                                pass
                                                            elif values[1] != str(pru_2.alo[3]):
                                                                sg.popup_ok('Incorrecto :c')
                                                                f = open("file.txt", "a")
                                                                f.write("4(❌)")
                                                                f.close
                                                            else:
                                                                sg.popup_ok('Felicitaciones')
                                                                f = open("file.txt", "a")
                                                                f.write("4(✔️)")
                                                                f.close
                                                            if event == 'Siguiente':
                                                                juego_fa_4.close()
                                                                while True:
                                                                    event, values = juego_fa_5.read()
                                                                    if event == 'REPRODUCIR':
                                                                        Interface.reproductor(pru_2.music_5f)
                                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                                        break
                                                                    elif values[1] == '':
                                                                        pass
                                                                    elif values[1] != str(pru_2.alo[4]):
                                                                        sg.popup_ok('Incorrecto :c')
                                                                        f = open("file.txt", "a")
                                                                        f.write("5(❌)")
                                                                        f.close
                                                                    else:
                                                                        sg.popup_ok('Felicitaciones')
                                                                        f = open("file.txt", "a")
                                                                        f.write("5(✔️)")
                                                                        f.close
                                                                    if event == 'Siguiente':
                                                                        juego_fa_5.close()
                                                                        while True:
                                                                            event, values = juego_fa_6.read()
                                                                            if event == 'REPRODUCIR':
                                                                                Interface.reproductor(pru_2.music_6f)
                                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                break
                                                                            elif values[1] == '':
                                                                                pass
                                                                            elif values[1] != str(pru_2.alo[5]):
                                                                                sg.popup_ok('Incorrecto :c')
                                                                                f = open("file.txt", "a")
                                                                                f.write("6(❌)")
                                                                                f.close
                                                                            else:
                                                                                sg.popup_ok('Felicitaciones')
                                                                                f = open("file.txt", "a")
                                                                                f.write("6(✔️)")
                                                                                f.close
                                                                            if event == 'Siguiente':
                                                                                juego_fa_6.close()
                                                                                while True:
                                                                                    event, values = juego_fa_7.read()
                                                                                    if event == 'REPRODUCIR':
                                                                                        Interface.reproductor(pru_2.music_7f)
                                                                                    if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                        break
                                                                                    elif values[1] == '':
                                                                                        pass
                                                                                    elif values[1] != str(pru_2.alo[6]):
                                                                                        sg.popup_ok('Incorrecto :c')
                                                                                        f = open("file.txt", "a")
                                                                                        f.write("7(❌)")
                                                                                        f.close
                                                                                    else:
                                                                                        sg.popup_ok('Felicitaciones')
                                                                                        f = open("file.txt", "a")
                                                                                        f.write("7(✔️)")
                                                                                        f.close
                                                                                    if event == 'Siguiente':
                                                                                        juego_fa_7.close()
                                                                                        while True:
                                                                                            event, values = juego_fa_8.read()
                                                                                            if event == 'REPRODUCIR':
                                                                                                Interface.reproductor(pru_2.music_8f)
                                                                                            if event == 'Cancel' or sg.WIN_CLOSED:
                                                                                                break
                                                                                            elif values[1] == '':
                                                                                                pass
                                                                                            elif values[1] != str(pru_2.alo[7]):
                                                                                                f = open("file.txt", "a")
                                                                                                f.write("8(❌) JuegoFa")
                                                                                                f.close
                                                                                            else:
                                                                                                sg.popup_ok('Felicitaciones')
                                                                                                f = open("file.txt", "a")
                                                                                                f.write("8(✔️) JuegoFa")
                                                                                                f.close
                                                                                            if event == 'Finalizar':
                                                                                                juego_fa_8.close()

    except: 
        print("Ocurrió algún error")
    finally:
        saludo.close()
        inicio.close()
        aprender.close()
        elegir.close()
        puntuacion.close()
        juego_sol_1.close()
        juego_sol_2.close()
        juego_sol_3.close()
        juego_sol_4.close()
        juego_sol_5.close()
        juego_sol_6.close()
        juego_sol_7.close()
        juego_sol_8.close()
        juego_fa_1.close()
        juego_fa_2.close()
        juego_fa_3.close()
        juego_fa_4.close()
        juego_fa_5.close()
        juego_fa_6.close()
        juego_fa_7.close()
        juego_fa_8.close()
        print("Todo cerrado")
        
    pygame.quit()
