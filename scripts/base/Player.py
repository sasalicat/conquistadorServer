import KBEngine
from KBEDebug import *

class Player(KBEngine.Proxy):
	def __init__(self):
		DEBUG_MSG("player init!!!")
		self.createCellEntity(KBEngine.entities[self.InWhichRoomEntityId].cell)