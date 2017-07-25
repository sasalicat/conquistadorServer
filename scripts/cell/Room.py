import KBEngine
import Math
from KBEDebug import *

class Room(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("room init")
	def cleanAllEntity(self):#清除场地上的所有entity
		allEntity=self.entitiesInRange(100)
		DEBUG_MSG(allEntity)
		for e in allEntity:
			if e!=self:
				DEBUG_MSG("in clean!!!",type(e))
				e.destroy()