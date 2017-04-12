import KBEngine
from KBEDebug import *

class  PlayerInRoom:
	def __init__(self,playerId,ready,roleKind,roomNo,equipmentList):
		self.playerId=playerId
		self.ready=ready
		self.roleKind=roleKind
		self.roomNo=roomNo
		self.equipmentList=equipmentList;
		
		DEBUG_MSG("InRoom init!!!")