class Player:
    def __init__(self, position):
        self.position = position
        self.speed = 1.0
        self.is_jumping = False
        self.jump_height = 5.0
        self.camera_angle = 0.0

    def move(self, direction):
        if direction == "forward":
            self.position[0] += self.speed
        elif direction == "backward":
            self.position[0] -= self.speed
        elif direction == "left":
            self.position[1] -= self.speed
        elif direction == "right":
            self.position[1] += self.speed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            # Logic for jumping can be added here

    def run(self):
        self.speed = 2.0

    def walk(self):
        self.speed = 1.0

    def rotate_camera(self, angle):
        self.camera_angle += angle
        # Logic for camera rotation can be added here

    def update(self):
        # Update player state, handle jumping logic, etc.
        pass