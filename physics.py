# def compute_distance(pos1, pos2):
#     Δx = abs(pos1[0]-pos2[0])
#     Δy = abs(pos1[1]-pos2[1])
#     return ((Δx**2 + Δy**2 )**0.5)

def apply_force(particle, magnitude_x, magnitude_y):
    particle.force[0] += magnitude_x
    particle.force[1] += magnitude_y

def global_gravity(particle, a_y=-9.80665):
    force = a_y * particle.mass
    apply_force(particle, 0, force)

# class Drag:
# drag class will replace the function soon

def apply_drag(particle, k=0.1): 
    particle.force[0] -= particle.vel[0] * k
    particle.force[1] -= particle.vel[1] * k

def apply_gravitational_force(particle1, particle2, G = 6.67430e-11, eps=1e-5):
    dx = (particle1.pos[0]-particle2.pos[0])
    dy = (particle1.pos[1]-particle2.pos[1])
    r = ((dx**2) + (dy**2) + (eps**2))**0.5 # softening to avoid division by 0
    force = (G*(particle1.mass*particle2.mass)/r**2)
    force_x = -(dx/r) * force
    force_y = -(dy/r) * force

    apply_force(particle1, force_x, force_y)
    apply_force(particle2, -force_x, -force_y)
