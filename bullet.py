class Bullet:

	def __init__(self,x,y,nx,ny,v):
		self.x = x
		self.y = y
		self.nx = nx
		self.ny = ny
		self.v = v

	def step(self):
		self.x=self.x+self.nx*self.v
		self.y=self.y+self.ny*self.v
