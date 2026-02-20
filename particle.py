class Particle:
    def __init__(self, pos=[0.0, 0.0], vel=[0.0, 0.0], mass=1.0):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.force = [0.0, 0.0]