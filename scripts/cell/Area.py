import KBEngine
import Math
from KBEDebug import *

class Area(KBEngine.Entity):
	def __init__(self):
		DEBUG_MSG("Area cell init!!!")
	def EnterArea(self,expose,No):
		self.insideNo.append(No)
		DEBUG_MSG("%d enter Area"%No)
	def LeaveArea(self,expose,No):
		self.insideNo.remove(No)
		DEBUG_MSG("%d leave Area"%No)
	def GetList(self,expose):
		return self.insideNo