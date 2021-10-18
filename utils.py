from vectors import *


def adjust_accel_for_dt(acceleration: Vec2f, dt: float) -> Vec2f:
	return Vec2f(acceleration.x * dt, acceleration.y * dt)


def adjust_accel_by_quad(quadrant: int, acceleration: Vec2f) -> Vec2f:
	if quadrant == 1:  # Top left
		return acceleration
	elif quadrant == 2:  # Top right
		return Vec2f(-acceleration.x, acceleration.y)
	elif quadrant == 3:  # Bottom right
		return Vec2f(acceleration.x, -acceleration.y)
	elif quadrant == 4:  # Bottom left
		return Vec2f(-acceleration.x, -acceleration.y)
	elif quadrant == 5:  # Top middle
		return Vec2f(0.0, acceleration.y)
	elif quadrant == 6:  # Middle right
		return Vec2f(-acceleration.x, 0.0)
	elif quadrant == 7:  # Bottom middle
		return Vec2f(0.0, -acceleration.y)
	else:  # Middle left
		return Vec2f(acceleration.x, 0.0)


def adjust_pos_for_display(pos: Vec2f) -> Vec2i:
	return pos.ret_as_int()

# Function that requires use of delta time
def calc_accel(force: float, mass: int, move_ratio: Vec2f) -> Vec2f:
	acceleration: float

	x_accel: float
	y_accel: float

	acceleration = force / mass

	x_accel = acceleration * move_ratio.x
	y_accel = acceleration * move_ratio.y

	return Vec2f(x_accel, y_accel)


def calc_force(sat_mass: int, centre_mass: int, line_dist: float, grav: float) -> float:
	return grav * ((centre_mass * sat_mass) / (line_dist ** 2))


def movement_ratio(axis_dist: Vec2i) -> Vec2f:
	total_dist: int
	x_prop: float
	y_prop: float

	total_dist = axis_dist.x + axis_dist.y

	x_prop = axis_dist.x / total_dist
	y_prop = axis_dist.y / total_dist

	return Vec2f(x_prop, y_prop)


def get_dist(obj1: Vec2f, obj2: Vec2f) -> tuple:
	# axis dist is used to calculate a movement ratio
	obj1i = obj1.ret_as_int()
	obj2i = obj2.ret_as_int()
	axis_dist = Vec2i(abs(obj1i.x - obj2i.x), abs(obj1i.y - obj2i.y))

	# line_dist is used to calculate gravitational influence
	line_dist = ((axis_dist.x ** 2) + (axis_dist.y ** 2)) ** 0.5

	return axis_dist, line_dist


def get_quadrant(sat_pos: Vec2i, centre: Vec2i):
	if sat_pos.x == centre.x:
		# Value will either be 5 or 7
		if sat_pos.y < centre.y:
			return 5
		else:
			return 7
	elif sat_pos.y == centre.y:
		# value will either be 6 or 8
		if sat_pos.x > centre.x:
			return 6
		else:
			return 8
	elif sat_pos.y > centre.y:
		# Value will either be 3 or 4
		if sat_pos.x < centre.x:
			return 3
		else:
			return 4
	else:
		# Value will either be 1 or 2
		if sat_pos.x < centre.x:
			return 1
		else:
			return 2
