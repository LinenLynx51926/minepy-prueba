from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from blocks import Block
class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.cursor = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.008, rotation_z=45)
        self.current_block = 'grass'
        
    def update(self):
        super().update()
        
        if held_keys['left mouse'] or held_keys['right mouse']:
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit:
                if held_keys['left mouse']:
                    destroy(hit_info.entity)
                elif held_keys['right mouse']:
                    new_position = hit_info.entity.position + hit_info.normal
                    Block(position=new_position, block_type=self.current_block)
