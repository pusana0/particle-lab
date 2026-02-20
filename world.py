from particle import Particle 
import physics

class World:
    def __init__(self, integrator):
        self.particles = []
        self.integrator = integrator

    def add_particle(self, particle):
        self.particles.append(particle)

    def step(self, dt=0.01):
        # call physical functions here
        self.integrator.step(self.particles, dt)
        for particle in self.particles:
            particle.force = [0.0, 0.0]
