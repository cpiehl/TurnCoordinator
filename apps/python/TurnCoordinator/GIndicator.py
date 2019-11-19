
import ac

class GIndicator:

	def __init__(self, app, x, y, w, h):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.halfW = w / 2
		self.halfH = h / 2
		self.qtrW = w / 4
		self.qtrH = h / 4
		self.frontBack = 0  # -1 to +1
		self.leftRight = 0
		self.alpha = 1

		self.barWidth = 1
		self.dotSize = 5

	
	def setValues(self, frontBack, leftRight):
		self.frontBack = frontBack
		self.leftRight = leftRight


	def setAlpha(self, alpha):
		self.alpha = alpha

		
	def render(self):
		# bars
		ac.glColor4f(1, 1, 1, 1)
		ac.glQuad(self.qtrW, self.halfH, self.halfW, self.barWidth)
		ac.glQuad(self.halfW, self.qtrH, self.barWidth, self.halfH)

		# dot
		ac.glColor4f(1, 0, 0, self.alpha)
		_x = self.halfW + (self.halfW * self.leftRight)
		_y = self.halfH + (self.halfH * self.frontBack)
		ac.glQuad(_x - self.dotSize, _y - self.dotSize, self.dotSize * 2, self.dotSize * 2)
