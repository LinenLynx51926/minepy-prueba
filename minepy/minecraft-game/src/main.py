from ursina import *
from player import Player
from terrain import Terrain
from textures import load_game_textures

class Game:
    def __init__(self):
        self.app = Ursina()
        window.title = 'Minecraft en Python'
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True

        # Cargar recursos
        self.textures = load_game_textures()
        global block_textures
        block_textures = self.textures
        
        # Crear jugador y terreno
        self.terrain = Terrain()
        self.player = Player()
        
        # Ejecutar el juego
        self.app.run()

if __name__ == '__main__':
    game = Game()
