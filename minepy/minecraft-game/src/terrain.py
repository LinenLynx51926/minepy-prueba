class Terrain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = self.generate_terrain()

    def generate_terrain(self):
        # Genera un terreno básico con bloques de tierra
        return [[Block('dirt') for _ in range(self.width)] for _ in range(self.height)]

    def render(self):
        # Renderiza el terreno en la pantalla
        for row in self.blocks:
            for block in row:
                block.render()

    def set_block(self, x, y, block_type):
        # Coloca un bloque en la posición especificada
        if 0 <= x < self.width and 0 <= y < self.height:
            self.blocks[y][x] = Block(block_type)

    def break_block(self, x, y):
        # Rompe el bloque en la posición especificada
        if 0 <= x < self.width and 0 <= y < self.height:
            self.blocks[y][x] = Block('air')  # Reemplaza con aire al romper el bloque

class Block:
    def __init__(self, block_type):
        self.block_type = block_type

    def render(self):
        # Lógica para renderizar el bloque
        pass