from world import World 
from particle import Particle

world = World()

world.add(Particle())

# initial test line 
print(len(world.particles))