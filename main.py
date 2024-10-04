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

    # Crear un reloj para limitar los FPS
    clock = pygame.time.Clock()

    # Ejecutar la pantalla de inicio
    runStartScreen(screen)

    # Bucle principal de la aplicación
    running = True
    while running:
        # Limitar los FPS
        clock.tick(60)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla
        screen.fill((255, 255, 255))  # Limpiar con color blanco

        # Aquí puedes llamar a tu función de dibujo
        runConvexHull(screen)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
