from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        width = 2
        pygame.draw.circle( screen, (255,255,255), self.position, self.radius, width )    

    def update(self, dt):
        self.position += ( self.velocity * dt )
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        new_asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
        

