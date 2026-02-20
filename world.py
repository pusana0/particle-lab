from particle import Particle 

class World:
    def __init__(self):
        self.particles = []

    def add(self, particle):
        self.particles.append(particle)
