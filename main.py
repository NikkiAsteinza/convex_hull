import pygame
from start_screen import runStartScreen
from convex_hull import runConvexHull

def main():
    # Iniciar Pygame
    pygame.init()
    
    # Tamaño de la pantalla
    screen_size = (800, 800)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("Convex Hull Algorithm")

    # Ejecutar la pantalla de inicio
    runStartScreen(screen)

    # Ejecutar el algoritmo de Convex Hull
    runConvexHull(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
