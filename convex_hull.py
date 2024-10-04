import pygame
import collections
from math import sqrt

# Definir colores
Colors = {
    "green": (0, 230, 0),
    "white": (255, 255, 255),
    "red": (230, 0, 0),
    "blue": (0, 0, 230),
    "black": (0, 0, 0),
}

# Definir punto como tupla
NewPoint = collections.namedtuple("NewPoint", "x y")

# Funciones de dibujo
def drawPoint(screen, p, color, radius=10):
    pygame.draw.circle(screen, Colors[color], (p.x, p.y), radius)

def drawLine(screen, origin, target, color, width=2):
    pygame.draw.line(screen, Colors[color], origin, target, width)

def drawButton(screen, text, x, y, width, height):
    pygame.draw.rect(screen, Colors["white"], (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, Colors["black"])
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def checkButtonClick(pos, button_rect):
    return button_rect.collidepoint(pos)

def distance(p1, p2):
    """Calcula la distancia entre dos puntos."""
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def cross(o, a, b):
    """Calcula el producto cruzado (o, a, b) para determinar la orientación."""
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convexHull(points):
    points = sorted(points, key=lambda p: (p.x, p.y))  # Ordenar los puntos por x, luego por y
    if len(points) <= 1:
        return points

    # Construir la parte inferior del hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Construir la parte superior del hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Eliminar el último punto de cada parte porque es repetido
    del lower[-1]
    del upper[-1]

    return lower + upper  # Retorna el Convex Hull

def runConvexHull(screen):
    selected_points = []
    is_running = True
    hull = []  # Para almacenar el Convex Hull
    show_instructions = True  # Para mostrar instrucciones y botón Convex Hull

    # Mensaje de instrucciones
    font = pygame.font.Font(None, 20)
    message_text = font.render("Click to select points (up to 50). Click 'Convex Hull' to execute.", True, Colors["white"])


    button_rect = pygame.Rect(400+100, 750, 150, 30)  # Botón Convex Hull
    reset_button_rect = pygame.Rect(400+280, 750, 100, 30)  # Botón Reset


    while is_running:
        # screen.fill(Colors["black"])
        background_image = pygame.image.load("bg.jpg")
        screen.blit(pygame.transform.scale(background_image, (800, 800)), (0, 0))
        # Mostrar instrucciones y botón Convex Hull si es necesario
        if show_instructions:
            screen.blit(message_text, (20, 750))
            drawButton(screen, "Convex Hull", button_rect.x, button_rect.y, button_rect.width, button_rect.height)
            # Dibujar el botón de Reset si se ha hecho clic en Convex Hull
        else:
            drawButton(screen, "Reset", reset_button_rect.x, reset_button_rect.y, reset_button_rect.width, reset_button_rect.height)

        # Dibujar todos los puntos seleccionados en cada frame
        for point in selected_points:
            drawPoint(screen, point, "white", 10)

        # Dibujar el Convex Hull si se ha calculado
        if hull:
            for i in range(len(hull)):
                drawLine(screen, (hull[i].x, hull[i].y), (hull[(i + 1) % len(hull)].x, hull[(i + 1) % len(hull)].y), "blue", 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if len(selected_points) < 50 and event.button == 1:
                    # Comprobar si el clic está dentro de las áreas de texto y botón
                    if show_instructions and not button_rect.collidepoint(pos):
                        selected_points.append(NewPoint(pos[0], pos[1]))
                if checkButtonClick(pos, button_rect):  # Click en el botón Convex Hull
                    if len(selected_points) < 3:
                        print("Need at least 3 points to calculate Convex Hull.")
                        continue
                    hull = convexHull(selected_points)
                    show_instructions = False  # Ocultar instrucciones y botón Convex Hull
                if checkButtonClick(pos, reset_button_rect):  # Click en el botón Reset
                    selected_points.clear()  # Borrar todos los puntos
                    hull.clear()  # Borrar el Convex Hull
                    show_instructions = True  # Volver a mostrar instrucciones

        pygame.display.flip()
