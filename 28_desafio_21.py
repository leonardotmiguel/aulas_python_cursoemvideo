'''
Desafio 21
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
'''

import pygame
pygame.init()
pygame.mixer.music.load('28_desafio_21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



'''import pygame  
# Importa a biblioteca pygame, que é usada para criar jogos, sons e gráficos.

pygame.init()  
# Inicializa todos os módulos do pygame que você vai usar (como som, gráficos, etc.).

pygame.mixer.music.load('28_desafio_21.mp3')  
# Carrega o arquivo de áudio '28_desafio_21.mp3' para reprodução. 
# O módulo 'mixer.music' é usado para lidar com música de fundo.

pygame.mixer.music.play()  
# Começa a tocar o áudio que foi carregado anteriormente.

input()  
# Pausa a execução do programa até que o usuário pressione Enter. 
# Isso é usado aqui para evitar que o programa feche imediatamente e pare a música.

pygame.event.wait()  
# Aguarda que algum evento do pygame aconteça (como fechar a janela). 
# Evita que o programa termine abruptamente e dá chance do pygame processar eventos.
'''