from particle import Particle 
import physics

class World:
    def __init__(self, integrator):
        self.particles = []
        self.integrator = integrator

    def add_particle(self, particle):
        self.particles.append(particle)

    def step(self, world_gravity=True, particle_gravity=True ,dt=0.01):
        particles_amount = len(self.particles)
        if world_gravity:
            for particle in self.particles:
                physics.global_gravity(particle)
        if particle_gravity:
            for i in range(particles_amount-1):
                for j in range(i+1, particles_amount):
                    physics.apply_gravitational_force(self.particles[i], self.particles[j])

        self.integrator.step(self.particles, dt)
        for particle in self.particles:
            particle.force[:] = 0
