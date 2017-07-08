import KBEngine
import locationData
from KBEDebug import *

class Player(KBEngine.Proxy):
	def __init__(self):
		DEBUG_MSG("player init!!!")
		
	def onClientDeath(self):
		KBEngine.entities[self.InWhichRoomEntityId].PlayerLeaveRoom(self.id)
		if self.cell!=None:#如果已经有cell实体则删除cell实体
			DEBUG_MSG("cell!=None-----------------------------")
			self.destroyCellEntity()
		else:
			self.destroy()#销毁自己
		KBEngine.entities[self.selfsAccountId].onClientDeath()
		
	def onLoseCell( self ):
		self.destroy()
	
	def onChangeToWar(self):
		DEBUG_MSG("----------------------onChangeToWar OK")
		playerList=KBEngine.entities[self.InWhichRoomEntityId].Playerlist
		list=[]
		for item in playerList:
			list.append({"roomNo":item.roomNo,"eId":item.playerGamingId})
		self.client.reqChangeReady(list)
	
	def notifyFinish(self):
		KBEngine.entities[self.InWhichRoomEntityId].notifyfinish(self.roomNo)
		
	def onIdReady(self):
		DEBUG_MSG("onIdReady OK-----------------------")
		self.createCellEntity(KBEngine.entities[self.InWhichRoomEntityId].cell)
		#self.cell.InWhichRoomEntityId=self.InWhichRoomEntityId
	def notify1(self,roomNo,action):
		playerList=KBEngine.entities[self.InWhichRoomEntityId].Playerlist
		for item in playerList:
			if not item.roomNo == roomNo:
				KBEngine.entities[item.playerGamingId].client.receive1(roomNo,action)
	def onGetCell( self ):
		if self.InWhichRoomEntityId!=-1:
			self.cell.setRoomId(self.InWhichRoomEntityId)
	
	def msTask(self):
		self.client.reqmsTask();
	
	def compulsiveLeaveRoom(self):
		KBEngine.entities[self.InWhichRoomEntityId].PlayerLeaveRoom(self.id)
		KBEngine.entities[self.selfsAccountId].InWhichRoomEntityId=-1#设置Account的inwhichroomEntityId
		self.InWhichRoomEntityId=-1#设置为-1和掉线做区分
		self.giveClientTo(KBEngine.entities[self.selfsAccountId])
		self.destroyCellEntity()
		DEBUG_MSG("compulsive Leave!!!")
		