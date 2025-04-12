from circleshape import *

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
