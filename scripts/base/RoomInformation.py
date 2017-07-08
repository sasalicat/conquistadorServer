import KBEngine
from KBEDebug import *

class RoomInformation:
	def __init__(self,Entityid,roomNo,name,num):
		self.EntityId=Entityid
		self.roomNo=roomNo
		self.name=name
		self.num=num
		DEBUG_MSG("RoomInformation init!!!")