from world import World 
from particle import Particle

world = World()

world.add(Particle())

print(len(world.particles))