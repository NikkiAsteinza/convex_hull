import asyncio
import pygame
from start_screen import runStartScreen
from convex_hull import runConvexHull

async def main():
    pygame.init()
    
    # Configuración de la pantalla
    screen_size = (800, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Convex Hull Algorithm")

    # Ejecutar la pantalla de inicio
    await runStartScreen(screen)
    
    # Bucle principal de la aplicación
    clock = pygame.time.Clock()
    running = True
    while running:
        # Limitar los FPS
        clock.tick(60)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla y ejecutar el algoritmo de Convex Hull
        screen.fill((255, 255, 255))  # Limpiar con color blanco
        await runConvexHull(screen)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
