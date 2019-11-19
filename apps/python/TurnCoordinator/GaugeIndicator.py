
import ac
import acsys
import math
import traceback

halfpi = math.pi/2

class GaugeIndicator:

	def __init__(self, app, x, y, w, h):

		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.halfW = w / 2
		self.value = 0
		self.targetValue = 0
		self.color = {'r':1,'g':1,'b':1,'a':1}
		# self.minValue = -10
		self.maxValue = 5
		self.fontSize = 24
		self.padding = 5

		self.valueLabel = ac.addLabel(app, "0.0°")
		ac.setPosition(self.valueLabel, x + self.halfW, y + h - self.fontSize - (2 * self.padding))
		ac.setFontSize(self.valueLabel, self.fontSize)
		ac.setFontAlignment(self.valueLabel, "center")

	def setValue(self, v):
		self.value = v
		ac.setText(self.valueLabel, "{0:.1f}°".format(abs(v)))

	def render(self):
		global halfpi
		ac.glBegin(acsys.GL.Lines)
		ac.glColor4f(1, 0, 0, 1)
		_x = self.x + self.halfW
		_y = self.y + self.h - self.fontSize - self.padding
		_value = halfpi * (self.value / self.maxValue)
		_dx = math.cos(_value + halfpi) * self.halfW
		_dy = math.sin(_value + halfpi) * self.halfW
		ac.glVertex2f(_x, _y)
		ac.glVertex2f(_x + _dx, _y - _dy)
		ac.glEnd() 