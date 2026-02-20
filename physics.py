def gravity(particle, a_y=9.80665):
    particle.force[1] -= a_y * particle.mass

def apply_force(particle, magnitude_x, magnitude_y):
    particle.force[0] += magnitude_x
    particle.force[1] += magnitude_y

def apply_drag(particle, k=0.1):
    particle.force[0] -= particle.vel[0] * k
    particle.force[1] -= particle.vel[1] * k