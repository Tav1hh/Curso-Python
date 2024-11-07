# Abre e reproduz um áudio MP3
from pygame import mixer
mixer.init()
mixer.music.load('04 - Body And Soul.mp3')
mixer.music.play()
x = input("Aperte Enter para finalizar o programa: ")
