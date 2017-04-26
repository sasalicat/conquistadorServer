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
		DEBUG_MSG("----------------------onChangeToWar OK")
		playerList=KBEngine.entities[self.InWhichRoomEntityId].Playerlist
		list=[]
		for item in playerList:
			list.append({"roomNo":item.roomNo,"eId":item.playerGamingId})
		self.client.reqChangeReady(list)
	
	def updateZ(self,newz):
		DEBUG_MSG("updateZ %d" %newz)
		KBEngine.entities[self.InWhichRoomEntityId].updateAllZ(self.roomNo,newz)
	def onIdReady(self):
		DEBUG_MSG("onIdReady OK-----------------------")
		self.createCellEntity(KBEngine.entities[self.InWhichRoomEntityId].cell)