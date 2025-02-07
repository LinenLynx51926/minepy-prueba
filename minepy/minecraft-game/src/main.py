import pygame
from terrain import Terrain
from player import Player

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft Game")

# Crear instancias de Terrain y Player
terrain = Terrain()
player = Player()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el estado del jugador
    player.update()

    # Renderizar el terreno y el jugador
    window.fill((135, 206, 235))  # Color de fondo (cielo)
    terrain.render(window)
    player.render(window)

    pygame.display.flip()

# Cerrar Pygame
pygame.quit()