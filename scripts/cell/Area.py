import KBEngine
import Math
from KBEDebug import *

class Area(KBEngine.Entity):
	insideNo=[]
	observers=[]
	def __init__(self):
		KBEngine.entities[self.RoomId].base.FormatCreated(self.id)
		DEBUG_MSG("Area cell init!!!")
	def EnterArea(self,expose,No):
		self.insideNo.append(No)
		DEBUG_MSG("%d enter Area"%No)
		DEBUG_MSG(self.insideNo)
	def ExitArea(self,expose,No):
		self.insideNo.remove(No)
	def GetList(self,expose):
		DEBUG_MSG("in getlist:")
		DEBUG_MSG(self.insideNo)
		return self.insideNo
	def addobserver(self,obs):
		observers.append(obs)
	def updateData(self):
		for item in observers:
			item.updateList(insideNo)