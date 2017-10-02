import KBEngine
import locationData
from PlayerInRoom import PlayerInRoom
from KBEDebug import *
import ConTestFormat

class Room(KBEngine.Base):
	def setFormat(self):
		if self.ContextKind==1:
			self.Format=ConTestFormat.Team_Format_Occupy()
		elif self.ContextKind==2:
			self.Format=ConTestFormat.Team_Format_annihilate()
	def __init__(self):
		self.hall=KBEngine.globalData["Hall"]
		self.Playerlist=[]
		self.roomNoPoor=[]
		self.finishNum=0;#用于记录加载完成的玩家
		#self.ChangedNum=0;#用于记录切换页面完成的玩家
		self.Format=None
		self.setFormat()
		if self.masterId == -1:
			DEBUG_MSG("MasterId is -1!!!")
		else:
			DEBUG_MSG("masterId is %d its vailed Kind is %d" %(self.masterId,self.masterKind))
			self.EnterRoom(self.masterId,self.masterKind,self.mequipmentList)

		#self.roomName
		#self.roomId

		self.updateOut()
	def updateOut(self):
		self.hall.updateRoom(self.roomId,self.roomName,len(self.Playerlist))
		
	def sendAllPlayerInfo(self,playerId,newRoomNo):
		list=[]
		for item in self.Playerlist:
			list.append({"roleRoomId":item.roomNo,"roleKind":item.roleKind,"ready":item.ready,"name":KBEngine.entities[item.playerId].nickName,"team":item.team,"equipmentList":item.equipmentList})
		playerInRoomList={"list":list,"selfRoomId":newRoomNo}
		KBEngine.entities[playerId].client.InitRoomInfo(playerInRoomList)
		
		
	def EnterRoom(self,newPlayerId,rolekind,equipmentList):
		DEBUG_MSG("enter room id is %d" %newPlayerId)
		#DEBUG_MSG("entity typr is{0}".format(isinstance(KBEngine.entities[newPlayerId],Account.Account)))
		#和hall一樣,檢查編號池裏面有沒有編號,如果有,優先使用閒置編號否則賦值玩家列表長度,即編號最大玩家的下一個編號
		newRoomNo=len(self.Playerlist)
		if(len(self.roomNoPoor)>0):
			newRoomNo=self.roomNoPoor.pop(0)
		teamNo=self.Format.onGiveTeam(self,newRoomNo)
		#这里先做给现有玩家添加新的玩家信息
		for item in self.Playerlist:
			KBEngine.entities[item.playerId].client.AddARoomInfo({"roleRoomId":newRoomNo,"roleKind":rolekind,"ready":False,"name":KBEngine.entities[newPlayerId].nickName,"team":teamNo,"equipmentList":equipmentList})
		#完成后在将新玩家加入列表这样能省一个判断句
		self.Playerlist.append(PlayerInRoom(newPlayerId,False,rolekind,newRoomNo,teamNo,equipmentList))
		#如果人數達到2才創建地圖,以防有人一直開房.反正遊戲至少要兩人才能進行
		if len(self.Playerlist)==2 and self.cell==None:
			self.createInNewSpace(None)
		#將玩家從在hall等待的玩家id中移除
		self.hall.playerInHallIds.remove(newPlayerId)
		self.sendAllPlayerInfo(newPlayerId,newRoomNo)
		KBEngine.entities[newPlayerId].RoomNo=newRoomNo#设置新entity的roomNo
		
		self.updateOut()


	def LeaveRoom(self,PlayId):#被Account.py呼叫
		for item in self.Playerlist:
			if item.playerId==PlayId:
				tempid=item.roomNo
				self.Playerlist.remove(item)
				self.roomNoPoor.append(item.roomNo)
				self.noticeLeave(tempid) #這裡告訴其他玩家有人離開
				break
		#將玩家加入在hall等待的玩家id
		if PlayId in self.hall.playerIds and not PlayId  in self.hall.playerInHallIds:
			DEBUG_MSG("add to playId in leaveRoom")
			self.hall.playerInHallIds.append(PlayId)
		self.updateOut()
		if len(self.Playerlist)<1:#如果房间已经没有人
			if self.cell!=None:#如果已经有cell实体则删除cell实体
				self.destroyCellEntity()
			else:
				self.hall.wirteOffRoom(self.roomId)#向大厅注销自己
				self.destroy()#销毁自己
		#else:
			#self.updateOut()
	def PlayerLeaveRoom(self,playId):#用于游戏中强制退出房间,被Player.py呼叫
		for item in self.Playerlist:
			if item.playerGamingId == playId:
				self.Playerlist.remove(item)
				self.roomNoPoor.append(item.roomNo)
				self.hall.delPlayer(KBEngine.entities[item.playerId])
				break
		self.updateOut()
		if len(self.Playerlist)<1:#如果房间已经没有人
			if self.cell!=None:#如果已经有cell实体则删除cell实体
				self.destroyCellEntity()
				
			else:
				self.destroy()#销毁自己
				self.hall.wirteOffRoom(self.roomId)#向大厅注销自己
				
	def onLoseCell( self ):
		self.destroy()
		self.hall.wirteOffRoom(self.roomId)#向大厅注销自己
	def setReady(self,roomNo,TorF):
		DEBUG_MSG("for roomNo is%d" %roomNo)
		data={}
		for item in self.Playerlist:
			if item.roomNo==roomNo:
				DEBUG_MSG("item roomNo is%d" %item.roomNo)
				item.ready=TorF
				data={"roleRoomId":item.roomNo,"roleKind":item.roleKind,"ready":TorF,"team":item.team,"equipmentList":item.equipmentList}
				break
		#更新所有其他玩家
		#檢查所有玩家是否都準備完成
		allReady=True
		for item in self.Playerlist:	
			KBEngine.entities[item.playerId].client.UpdateRoomInfo(data)
			if not item.ready:
				allReady=False
		#開始遊戲
		if allReady and self.Format.onAllReady(self):
			#创造障碍物
			for i in range(len(locationData.obstacleKind)):
				KBEngine.createBaseAnywhere("Obstacle",{"position":locationData.obstacleLocation[i],"SpaceId":self.id,"kind":locationData.obstacleKind[i]})
					
			#通知玩家换页
			for item in self.Playerlist:
				DEBUG_MSG("roomNo is%d" %item.roomNo)
				DEBUG_MSG(locationData.initLocation[item.roomNo])
				item.playerGamingId= KBEngine.entities[item.playerId].changeToPlayer(locationData.initLocation[item.roomNo])
				DEBUG_MSG("item.playerGamingId is %d" %item.playerGamingId)
			#设置cell部分的生存表
			teamlists=[]
			for role in self.Playerlist:
				teamlists.append(role.team)
			self.cell.InitTeamList(teamlists)
				
	def noticeLeave(self,roomId):#告知客戶端有玩家離開房間
		data={"roleRoomId":roomId,"roleKind":-1,"ready":False,"team":-1,"equipmentList":[]}#roleKind為-1代表玩家離開,可以省一個function

		for item in self.Playerlist:
			KBEngine.entities[item.playerId].client.UpdateRoomInfo(data)
	def updateAllZ(self,roomNo,newZ):
		
		for item in self.Playerlist:
			if not item.roomNo ==roomNo:
				DEBUG_MSG("roomNo %d" %roomNo)
				KBEngine.entities[item.playerGamingId].client.updateZ(roomNo,newZ)
	def notifyfinish(self,roomId):
		DEBUG_MSG("notitfy Finish")
		self.finishNum=self.finishNum+1;
		for item in self.Playerlist:
			KBEngine.entities[item.playerGamingId].client.getFinish(roomId)
		if self.finishNum >=len(self.Playerlist):
			self.intervalTimer=self.addTimer(0.1,0.1,1)
			self.cell.clientLoadFinish()
			DEBUG_MSG("addTimer interval...")
	def onTimer( self, timerHandle, userData ):
		if userData==1:#间隔触发
			#DEBUG_MSG("ontimer userData=1")
			for item in self.Playerlist:
				if item.playerGamingId!=-1:
					KBEngine.entities[item.playerGamingId].client.intervalTrigger()
	def setDied(self,roomNo,code):
		if code<=0:#死亡
			self.Playerlist[roomNo].alive=0
		else:#复活角色,将会发送复活请求以code的血量复活
			pass
	def resetRoom(self):
		for item in self.Playerlist:
			item.playerGamingId=-1
			item.alive=1
			item.ready=False
	def gameOver(self,winnerMo):
		#呼叫所有玩家的切回房间页面函数
		self.delTimer(self.intervalTimer)
		self.finishNum=0#重置加载完成玩家的数量
		for item in self.Playerlist:
			KBEngine.entities[item.playerGamingId].client.gameOver(winnerMo)
			KBEngine.entities[item.playerGamingId].changeToAccount()
		self.resetRoom()
		self.cell.cleanAllEntity()
	def ChangeTeam(self,roomNo):
		self.Format.onChangeTeam(self,roomNo)
	def	FormatCreated(self,eid):
		self.Format.createFinish(eid)