import KBEngine
from KBEDebug import *

class  PlayerInRoom:
	def __init__(self,playerId,ready,roleKind,roomNo,equipmentList):
		self.playerId=playerId#這是Account Entity的id
		self.ready=ready
		self.roleKind=roleKind
		self.roomNo=roomNo
		self.equipmentList=equipmentList
		self.playerGamingId=-1#這是player Entity的id,用於記錄開始遊戲後giveclient之後的玩家entity,只有在那個時候才會被賦值
		self.team=-1;
		DEBUG_MSG("InRoom init!!!")