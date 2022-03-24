# Import custom classes
from objects import *
from utils import *

# Import Raylib
from raylib import *

# Constants
GRAVITY = 2.0
END_MSG = "The satellite has burnt up upon reaching the sun."
WINDOW_SIZE = Vec2i(600, 600)
CENTRE = Vec2f(float(WINDOW_SIZE.x / 2), float(WINDOW_SIZE.y / 2))

# Initialize raylib
rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT)  # Enable Multi Sampling Anti Aliasing 4x (if available)
rl.SetTargetFPS(30)
rl.InitWindow(WINDOW_SIZE.x, WINDOW_SIZE.y, b"Space Orbit Sim")


# Main function
def main() -> None:
	sat = Planet(1, 5, Vec2f(CENTRE.x + 100.0, CENTRE.y), Vec2f(0.0, 3.0))
	sun = Planet(1000, 20, CENTRE, Vec2f(0.0, 0.0))
	sat.display_pos = Vec2i(round(sat.pos.x), round(sat.pos.y))
	sun.display_pos = Vec2i(round(sun.pos.x), round(sun.pos.y))

	axis_dist: Vec2i
	line_dist: float
	ratio: Vec2f
	force: float
	acceleration: Vec2f
	delta_acceleration: Vec2f
	is_complete: bool
	sat_quad: int
	is_first_frame: bool

	is_complete = False
	is_first_frame = True

	while not rl.WindowShouldClose():
		# Update variables
		
		# Calculate Distances
		axis_dist, line_dist = get_dist(sat.pos, sun.pos)
		ratio = movement_ratio(axis_dist)

		# Calculate force as a float
		force = calc_force(sat.mass, sun.mass, line_dist, GRAVITY)
		# Calculate acceleration as a Vec2f
		acceleration = calc_accel(force, sat.mass, ratio)

		# Find the quadrant that the satelitte is in
		sat_quad = get_quadrant(sat.display_pos, sun.display_pos)
		# Calculate acceleration affected by delta-time
		delta_acceleration = adjust_accel_by_quad(sat_quad, acceleration)
		
		# Update the position of the satellite
		sat.update_pos(delta_acceleration)
		# Adjust the satellite's display
		sat.display_pos = adjust_pos_for_display(sat.pos)

		if not is_first_frame:
			delta_acceleration = adjust_accel_for_dt(acceleration, rl.GetFrameTime())
		else:
			delta_acceleration = Vec2f(0, 0)
			is_first_frame = False

		if line_dist < (sat.radius + sun.radius):
			is_complete = True

		rl.BeginDrawing()
		rl.ClearBackground(BLACK)
		if not is_complete:
			rl.DrawCircle(sun.display_pos.x, sun.display_pos.y, sun.radius, WHITE)
			rl.DrawCircle(sat.display_pos.x, sat.display_pos.y, sat.radius, RED)
		else:
			rl.DrawText(END_MSG.encode(), 43, 240, 20, GREEN)
		rl.EndDrawing()

		print(sat.vel.x, sat.vel.y)


if __name__ == "__main__":
	main()
