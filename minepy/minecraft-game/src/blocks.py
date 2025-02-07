class Block:
    def __init__(self, name, texture):
        self.name = name
        self.texture = texture
        self.is_solid = True

    def break_block(self):
        # Lógica para romper el bloque
        pass

    def place_block(self):
        # Lógica para colocar el bloque
        pass


class DirtBlock(Block):
    def __init__(self):
        super().__init__("Dirt", "textures/dirt.png")


class StoneBlock(Block):
    def __init__(self):
        super().__init__("Stone", "textures/stone.png")


class WoodBlock(Block):
    def __init__(self):
        super().__init__("Wood", "textures/wood.png")