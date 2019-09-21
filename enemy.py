class Enemy:
	def __init__ (self,x,y,size,v):
		self.x = x
		self.y = y
		self.size = size
		self.v = v
		self.destroyed=False

	def step(self):
		self.x = self.x
		self.y = self.y + self.v