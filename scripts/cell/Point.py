import KBEngine
import Math
from KBEDebug import *

class Point(KBEngine.Entity):
	format=None
	index=-1
	def __init__(self):
		pass
	def notifyAbate(self,expose):
		DEBUG_MSG("notifyAbate been call")
		self.format.pointAbate(self.index)
		self.destroy()
