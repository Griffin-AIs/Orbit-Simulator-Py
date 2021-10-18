# Import custom classes
from objects import *
from utils import *

# Import Raylib
from raylib.static import *
from raylib.colors import *

# Constants
GRAVITY = 2.0
END_MSG = "The satellite has burnt up upon reaching the sun."
WINDOW_SIZE = Vec2i(600, 600)
CENTRE = Vec2f(float(WINDOW_SIZE.x / 2), float(WINDOW_SIZE.y / 2))

# Initialize raylib
SetConfigFlags(FLAG_MSAA_4X_HINT)  # Enable Multi Sampling Anti Aliasing 4x (if available)
SetTargetFPS(80)
InitWindow(WINDOW_SIZE.x, WINDOW_SIZE.y, b"Space Orbit Sim")


# Main function
def main() -> None:
	sat = Planet(1, 5, Vec2f(CENTRE.x, CENTRE.y - 100.0), Vec2f(4.47213595499958, 0.0))
	sun = Planet(1000, 20, CENTRE, Vec2f(0.0, 0.0))
	sat.display_pos = Vec2i(round(sat.pos.x), round(sat.pos.y))
	sun.display_pos = Vec2i(round(sun.pos.x), round(sun.pos.y))

	axis_dist: Vec2i
	line_dist: float
	ratio: Vec2f
	force: float
	acceleration: Vec2f
	is_complete: bool
	sat_quad: int

	is_complete = False

	while not WindowShouldClose():
		# Update variables
		axis_dist, line_dist = get_dist(sat.pos, sun.pos)
		ratio = movement_ratio(axis_dist)
		force = calc_force(sat.mass, sun.mass, line_dist, GRAVITY)
		acceleration = calc_accel(force, sat.mass, ratio)

		sat_quad = get_quadrant(sat.display_pos, sun.display_pos)
		acceleration = adjust_accel_by_quad(sat_quad, acceleration)

		sat.update_pos(acceleration)
		sat.display_pos = adjust_pos_for_display(sat.pos)

		if line_dist < (sat.radius + sun.radius):
			is_complete = True

		BeginDrawing()
		ClearBackground(BLACK)
		if not is_complete:
			DrawCircle(sun.display_pos.x, sun.display_pos.y, sun.radius, WHITE)
			DrawCircle(sat.display_pos.x, sat.display_pos.y, sat.radius, RED)
		else:
			DrawText(END_MSG.encode(), 43, 240, 20, GREEN)
		EndDrawing()

		print(sat.pos.x, sat.pos.y)


if __name__ == "__main__":
	main()
