from world import World 
from particle import Particle

world = World(integrator="EulerIntegrator")

world.add(Particle())

# initial test line 
print(len(world.particles))

running = False # test line 

while running:
    pass