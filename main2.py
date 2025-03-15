import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Wave Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Wave parameters
time = 0
amplitude = 50  # Initial amplitude
frequency = 0.02  # Initial frequency
speed = 0.1  # Wave speed

running = True
while running:
  screen.fill(WHITE)
  
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        amplitude += 5  # Increase amplitude
      elif event.key == pygame.K_DOWN:
        amplitude = max(5, amplitude - 5)  # Decrease amplitude
      elif event.key == pygame.K_RIGHT:
        frequency += 0.005  # Increase frequency
      elif event.key == pygame.K_LEFT:
        frequency = max(0.005, frequency - 0.005)  # Decrease frequency
      elif event.key == pygame.K_w:
        speed += 0.01  # Increase speed
      elif event.key == pygame.K_s:
        speed = max(0.01, speed - 0.01)  # Decrease speed

  # Draw wave
  for x in range(WIDTH):
    y = int(HEIGHT // 2 + amplitude * np.sin(frequency * x + time))
    pygame.draw.circle(screen, BLUE, (x, y), 2)

  time += speed  # Update time
  
  pygame.display.flip()
  pygame.time.delay(20)

pygame.quit()