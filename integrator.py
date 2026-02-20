class Integrator:
    def step(self, particles, dt):
        raise NotImplementedError


class EulerIntegrator(Integrator):
    def step(self, particles, dt):
        for particle in particles:
            a_x = particle.force[0] / particle.mass
            a_y = particle.force[1] / particle.mass

            particle.vel[0] += a_x * dt 
            particle.vel[1] += a_y * dt

            particle.pos[0] += particle.vel[0] * dt 
            particle.pos[1] += particle.vel[1] * dt 