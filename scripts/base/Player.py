import KBEngine
import locationData
from KBEDebug import *

class Player(KBEngine.Proxy):
	def __init__(self):
		DEBUG_MSG("player init!!!")
		
	def onClientDeath(self):
		KBEngine.entities[self.InWhichRoomEntityId].PlayerLeaveRoom(self.id)
		if self.cell!=None:#如果已经有cell实体则删除cell实体
			self.destroyCellEntity()
		else:
			self.destroy()#销毁自己
	def onLoseCell( self ):
		self.destroy()
	
	def onChangeToWar(self):
		self.createCellEntity(KBEngine.entities[self.InWhichRoomEntityId].cell)