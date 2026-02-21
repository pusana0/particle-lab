import physics

class Rod:
    def __init__(self, lenght, anchor1, anchor2):
        self.anchor1 = anchor1 
        self.anchor2 = anchor2
        self.lenght = lenght
        
    def constrain(self): # implementation is positional for now, velocity based correction is planned 
        distance = physics.compute_distance(self.anchor1.position, self.anchor2.position)
        if distance == 0:
            return
        error = distance - self.lenght
        correction = error / 2
        dx, dy = physics.compute_deltas(self.anchor1.position, self.anchor2.position)
        direction_x = dx / distance
        direction_y = dy / distance
        w1 = 0 if self.anchor1.mass == 0 else 1/self.anchor1.mass
        w2 = 0 if self.anchor2.mass == 0 else 1/self.anchor2.mass
        w_sum = w1 + w2
        
        self.anchor1.position[0] += direction_x * correction * (w1/w_sum)
        self.anchor1.position[1] += direction_y * correction * (w1/w_sum)
        self.anchor2.position[0] -= direction_x * correction * (w2/w_sum)
        self.anchor2.position[1] -= direction_y * correction * (w2/w_sum)