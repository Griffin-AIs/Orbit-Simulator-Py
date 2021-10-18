from vectors import *


class Planet:
	def __init__(self, mass: int, radius: int, pos: Vec2f, vel: Vec2f):
		self.mass = mass
		self.radius = radius
		self.pos = pos
		self.vel = vel
		self.display_pos = Vec2i(0, 0)

	def update_pos(self, acceleration: Vec2f):
		self.vel.x += acceleration.x
		self.vel.y += acceleration.y

		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
