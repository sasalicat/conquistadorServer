# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		self.InWhichRoomEntityId=-1
		
		
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		#if KBEngine.baseAppData.get('first',None)==None:
		#	self.createInNewSpace(None)
		#	KBEngine.baseAppData['first']=self
		#else:
		#	self.createCellEntity(KBEngine.baseAppData['first'].cell)
		KBEngine.globalData["Hall"].addPlayer(self)
		DEBUG_MSG("account init!!!")#在大廳添加玩家!!!!
		INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		KBEngine.globalData["Hall"].delPlayer(self)#從大廳刪除玩家!!!!!
		if self.InWhichRoomEntityId!=-1:
			KBEngine.entities[self.InWhichRoomEntityId].LeaveRoom(self.id)
		self.destroy()
		#self.destroyCellEntity()
	def onLoseCell( self ): 
		self.destroy()
	#----------------------------------------------------------大廳內的函數---------------------------------------------------------------
	def sendNumToClient(self,num):#發送現在玩家數給client,在timer裏面使用
		self.client.updateNum(num)
	
	def onHallReady(self):#當對應client的大廳準備好時候呼叫此函數,傳遞其暱稱回client端
		KBEngine.globalData["Hall"].sendRoomInfos(self)
		self.client.reqHallReady(self.nickName)
	
	
	def changeNickName(self,newname):
		self.nickName = newname
		self.writeToDB()
	
	def updateRoom(self,data):
		self.client.updateRoom(data)
	
	def createRoom(self,roomName,roleKind,equipList):
		self.InWhichRoomEntityId=KBEngine.globalData["Hall"].createRoom(roomName,self.id,roleKind,equipList)
		DEBUG_MSG("RoomName Receive:%s !!!!!" %roomName)
	def enterRoomReq(self,roomId,roleKind,equipList): 
		roomlist=KBEngine.globalData["Hall"].rooms
		for roomInfo in roomlist:
			if roomInfo.roomId==roomId:
				self.InWhichRoomEntityId=roomInfo.EntityId
				KBEngine.entities[roomInfo.EntityId].EnterRoom(self.id,roleKind,equipList)
				break
	#----------------------------------------------------------房間內的函數-----------------------------------------------------------
	def setReady(self,roomId,TorF):
		DEBUG_MSG("readyset is called!!!")
		if self.InWhichRoomEntityId!=-1:
			KBEngine.entities[self.InWhichRoomEntityId].setReady(roomId,TorF)
		else:
			DEBUG_MSG("on setReady inwhich is -1")
	def leaveRoom(self):
		if self.InWhichRoomEntityId!=-1:
			KBEngine.entities[self.InWhichRoomEntityId].LeaveRoom(self.id)
			self.InWhichRoomEntityId=-1
	def changeToPlayer(self,location):
		self.client.changeToWar()
		playerList=KBEngine.entities[self.InWhichRoomEntityId].Playerlist
		selfRoomNo=-1
		for item in playerList:
			if item.playerId == self.id:
				selfRoomNo=item.roomNo
		player= KBEngine.createBaseLocally("Player",{"InWhichRoomEntityId":self.InWhichRoomEntityId,"position":location,"selfsAccountId":self.id,"roomNo":selfRoomNo})
		self.giveClientTo(player)
		return player.id
