import KBEngine
import locationData
from PlayerInRoom import PlayerInRoom
from KBEDebug import *

class Area(KBEngine.Base):
	def __init__(self):
		if(KBEngine.entities[self.SpaceId].cell!=None):
			self.createCellEntity(KBEngine.entities[self.SpaceId].cell)
