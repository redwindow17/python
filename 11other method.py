# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((600,500))

# Initialing Color
color = (255,0,0)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 100, 60))
pygame.display.flip()
