import pygame

def runStartScreen(screen):
    is_running = True
    font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 36)

    # Mensaje de inicio
    title_text = font.render("Convex Hull Algorithm", True, (255, 255, 255))
    button_rect = pygame.Rect(300, 600, 200, 50)

    while is_running:
        screen.fill((0, 0, 0))
        screen.blit(title_text, (80, 250))

        # Dibujar el botón
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        button_text = button_font.render("Start", True, (0, 0, 0))
        text_rect = button_text.get_rect(center=(button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2))
        screen.blit(button_text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Click izquierdo
                if button_rect.collidepoint(event.pos):
                    is_running = False  # Salir de la pantalla de inicio

        pygame.display.flip()

