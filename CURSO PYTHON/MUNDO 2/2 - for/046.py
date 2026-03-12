import pygame
import time
for c in range (10, 0, -1):
    time.sleep(0.5)
    print (c)
print ('''🧨
🧨
🧨
🧨
🧨
🧨
🧨
🧨
🧨
🧨
POOOOOOWWWWWWWW
''')
pygame.mixer.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()








