import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Konstanta gelombang
WIDTH, HEIGHT = 800, 600
AMPLITUDE = 0.2  # Amplitudo gelombang
WAVELENGTH = 2.0  # Panjang gelombang
FREQUENCY = 2.0  # Frekuensi gelombang
SPEED = 2.0  # Kecepatan gelombang

def wave_function(x, time):
    return AMPLITUDE * np.sin((2 * np.pi / WAVELENGTH) * x - (FREQUENCY * time))

def draw_wave(time):
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 0.5, 1.0)  # Warna biru
    for x in np.linspace(-1, 1, 100):
        y = wave_function(x, time)
        glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    glOrtho(-1, 1, -1, 1, -1, 1)  # Mengatur perspektif 2D

    clock = pygame.time.Clock()
    time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_wave(time)
        pygame.display.flip()
        
        time += SPEED * 0.01  # Update waktu
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
