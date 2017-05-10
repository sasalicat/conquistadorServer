import KBEngine
import Math
from KBEDebug import *

class Player(KBEngine.Entity):
	InWhichRoomEntityId=-1
	def __init__(self):
		DEBUG_MSG("players cell init !!!%d" %self.InWhichRoomEntityId)
	
	def notify1(self,expose,roomNo,action):
		self.allClients.receive1(roomNo,action)
	def notify2(self,expose,roomNo,action,dirZ):
		self.allClients.receive2(roomNo,action,dirZ)
	def notify3(self,expose,equipmentIndex,playerPos,mousePos):
		self.allClients.receive3(equipmentIndex,playerPos,mousePos)
	def setRoomId(self,roomId):
		DEBUG_MSG("set roomId %d" %roomId)
		self.InWhichRoomEntityId=roomId