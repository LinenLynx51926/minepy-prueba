from ursina import *

class Block(Button):
    def __init__(self, position=(0,0,0), block_type='grass'):
        # Definir colores por defecto para cada tipo de bloque
        colors = {
            'grass': color.rgb(34, 139, 34),  # Verde
            'stone': color.rgb(128, 128, 128),  # Gris
            'dirt': color.rgb(139, 69, 19)   # Marrón
        }
        
        block_color = colors.get(block_type, color.white)
        
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            color=block_color,
            highlight_color=color.lime,
            scale=1.0
        )
        self.block_type = block_type

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            elif key == 'right mouse down':
                pos = self.position + mouse.normal
                Block(position=pos, block_type=self.block_type)
