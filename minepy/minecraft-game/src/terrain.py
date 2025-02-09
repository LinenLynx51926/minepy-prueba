from ursina import *
from blocks import Block

class Terrain:
    def __init__(self):
        self.blocks = []
        self.generate_terrain()
        
    def generate_terrain(self):
        for z in range(20):
            for x in range(20):
                height = random.randint(0, 3)
                for y in range(height + 1):
                    block_type = self.get_block_type(y, height)
                    block = Block(position=(x, y, z), block_type=block_type)
                    self.blocks.append(block)

    def get_block_type(self, y, max_height):
        if y == max_height:
            return 'grass'
        elif y > max_height - 3:
            return 'dirt'
        else:
            return 'stone'
