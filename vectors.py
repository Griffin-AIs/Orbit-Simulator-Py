class Vec2i:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


class Vec2f:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def ret_as_int(self) -> Vec2i:
		return Vec2i(round(self.x), round(self.y))
