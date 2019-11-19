
import ac
import acsys
import colorsys
import json
import math
import os
import pickle
import platform
import traceback
import sys

from GaugeIndicator import GaugeIndicator
from GIndicator import GIndicator
# from mathybits import *

# if platform.architecture()[0] == "64bit":
#     libdir = 'third_party/lib64'
# else:
#     libdir = 'third_party/lib'
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), libdir))
# os.environ['PATH'] = os.environ['PATH'] + ";."

# from third_party.sim_info import info

doRender = True
appWindow = 0
indicators = {}
customFont = "Consolas"

def acMain(ac_version):
	appWindow = ac.newApp("TurnCoordinator")
	ac.setSize(appWindow, 200, 200)
	ac.drawBorder(appWindow, 0)
	ac.setBackgroundOpacity(appWindow, 0)
	ac.drawBackground(appWindow, 0)
	ac.setIconPosition(appWindow, 0, -10000)
	ac.setTitle(appWindow, "")

	# Only enable rendering if app is activated
	ac.addOnAppActivatedListener(appWindow, onAppActivated)
	ac.addOnAppDismissedListener(appWindow, onAppDismissed)

	# Custom monospace font
	ac.initFont(0, customFont, 0, 0)

	try:
		# indicators["fl"] = GaugeIndicator(appWindow, 0, 0, 100, 100)
		# indicators["fr"] = GaugeIndicator(appWindow, 100, 0, 100, 100)
		# indicators["rl"] = GaugeIndicator(appWindow, 0, 100, 100, 100)
		# indicators["rr"] = GaugeIndicator(appWindow, 100, 100, 100, 100)
		indicators["dot"] = GIndicator(appWindow, 0, 50, 200, 100)
	except Exception:
		ac.log("TurnCoordinator ERROR: Indicator.__init__(): %s" % traceback.format_exc())

	ac.addRenderCallback(appWindow, onFormRender)
		
	return "TurnCoordinator"


def getSlipAngle():
	# flx, fly, flz = ac.getCarState(0, acsys.CS.TyreHeadingVector, acsys.WHEELS.FL)
	# frx, fry, frz = ac.getCarState(0, acsys.CS.TyreHeadingVector, acsys.WHEELS.FR)
	# flv = info.physics.tyreContactHeading.__dict__
	# ac.log(flx + " " + fly + " " + flz)
	# ac.log(flv)
	# carx, cary, carz = ac.getCarState(0, acsys.CS.LocalVelocity)

	# fl = angle((flx, fly, flz), (carx, cary, carz))
	# fr = angle((frx, fry, flz), (carx, cary, carz))

	fl, fr, rl, rr = ac.getCarState(0, acsys.CS.NdSlip)

	return (fl, fr, rl, rr)


def onFormRender(deltaT):
	global doRender
	try:
		if not doRender:
			return

		fl, fr, rl, rr = getSlipAngle()

		_neg = 1
		if ac.getCarState(0, acsys.CS.Steer) > 0:
			_neg = -1
		
		# indicators["fl"].setValue(fl * _neg)
		# indicators["fr"].setValue(fr * _neg)
		# indicators["rl"].setValue(rl * _neg)
		# indicators["rr"].setValue(rr * _neg)

		# ratios of steering angle, -1 to +1
		_front = (fr + fl) / 2
		_rear = (rr + rl) / 2
		# _left = (fl + rl) / 2
		# _right = (fr + rr) / 2
		_frontBack = (_rear - _front) / (_front + _rear)
		# _leftRight = (_left - _right) / (_left + _right)
		indicators["dot"].setValues(0, _frontBack * _neg)
		indicators["dot"].setAlpha((1 - _frontBack)**3)

		# indicators["fl"].render()
		# indicators["fr"].render()
		# indicators["rl"].render()
		# indicators["rr"].render()
		indicators["dot"].render()

	except Exception:
		ac.log("TurnCoordinator ERROR: onFormRender(): %s" % traceback.format_exc())


def onAppActivated(self):
	global doRender
	doRender = True


def onAppDismissed(self):
	global doRender
	doRender = False
