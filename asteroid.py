from circleshape import *
from constants import *
import pygame
from logger import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
            )
    
    def update(self,dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle=random.uniform(20,50)
        first_new_asteriod_movement=self.velocity.rotate(random_angle)
        second_new_asteriod_movement=self.velocity.rotate(-(random_angle))
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        asteriod_1=Asteroid(self.position.x,self.position.y,new_radius)
        asteriod_2=Asteroid(self.position.x,self.position.y,new_radius)
        asteriod_1.velocity=first_new_asteriod_movement*1.2
        asteriod_2.velocity=second_new_asteriod_movement*1.2
        