# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from RoomInformation import RoomInformation

class Hall(KBEngine.Base):
	def __init__(self):
		KBEngine.Base.__init__(self)
		INFO_MSG("Hall")
		KBEngine.globalData["Hall"] = self
				
		self.playerIds=[]#在线玩家的列表
		self.playerInHallIds=[]#沒有在房間的玩家列表,用於送roomList
		self.roomIdPoor=[]#用于存放被摧毁房间的id,当新的房间创建时,如果此列表不为空,则优先使用此列表的项目
		self.rooms=[]#roomInformation形態陣列
				
		self.addTimer(5,5,1)
	def addPlayer(self,newone):
		if newone.id in self.playerIds:
			DEBUG_MSG("id in playerIds len is%d" %len(self.playerIds))
			return
				
		self.playerIds.append(newone.id)
		if newone.id in self.playerInHallIds:
			#DEBUG_MSG("id in HallIds len is%d" %len(playerIds))
			return
		self.playerInHallIds.append(newone.id)
		DEBUG_MSG("in addPlayer Ids is")
		DEBUG_MSG(self.playerIds)
		
			
	def delPlayer(self,theOld):
		if theOld.id in self.playerIds:
			self.playerIds.remove(theOld.id)
		if theOld.id in self.playerIds:
			self.playerInHallIds.remove(theOld.id)
		
	def onTimer(self, id, userArg):
                #更新在线人数
		if userArg == 1:
			self.UpdatePlayer()
			
	def UpdatePlayer(self):
		for i in  range(len(self.playerIds)):
			if KBEngine.entities[self.playerIds[i]].isDestroyed == True:
				del self.playerIds[i]
				
		for item in  self.playerInHallIds:
			#DEBUG_MSG(KBEngine.entities[self.playerIds[i]])
			KBEngine.entities[item].sendNumToClient(len(self.playerInHallIds))
	def updateRoom(self,roomId,roomName,playerNum):
		for item in self.rooms:
			if item.roomId==roomId:
				item.name=roomName
				item.num=playerNum
		data={'roomId':roomId,'roomName':roomName,'playerNum':playerNum}
		DEBUG_MSG(self.playerIds)
		for pid in self.playerInHallIds:
			DEBUG_MSG("in updateRoom pid is %d" %pid)
			KBEngine.entities[pid].updateRoom(data)
	def createRoom(self,roomName,playerId,roleKind,equipmentList):#rolekind是房主的角色類型編號
		newid=len(self.rooms)#新房间的id预设为rooms长度
		if(len(self.roomIdPoor)>0):#如果roomidpoor有剩余优先使用roomidpoor
			newid=self.roomIdPoor.pop(0)
		newRoom=KBEngine.createBaseLocally("Room",{"roomName":roomName,"roomId":newid,"masterId":playerId,"masterKind":roleKind,"mequipmentList":equipmentList})
		self.rooms.append(RoomInformation(newRoom.id,newid,roomName,1))
		return newRoom.id;
	def sendRoomInfos(self,asker):#asker是Account形態
		list=[]
		for item in self.rooms:
			data={"roomId":item.roomId,"roomName":item.name,"playerNum":item.num}
			list.append(data)
		datas={"list":list}
		asker.client.getRoomList(datas)