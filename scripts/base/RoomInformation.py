import KBEngine
from KBEDebug import *

class RoomInformation:
	def __init__(self,Entityid,roomid,name,num):
		self.EntityId=Entityid
		self.roomId=roomid
		self.name=name
		self.num=num
		DEBUG_MSG("RoomInformation init!!!")