import KBEngine
from KBEDebug import *

class Team_Format_Occupy:
	centerArea=None;
	point_team1=0;
	point_team2=0;
	inArea=None
	def createFinish(self,eid):
		DEBUG_MSG("createFinish")
		self.centerArea=KBEngine.entities[eid]
		self.centerArea.cell.addobserver(self)
	def onMapBuild(self,room):#初始化地图时呼叫
		DEBUG_MSG("===================onMapBuild---------------------------")
		self.point_team1=0
		self.point_team2=0
		newone=KBEngine.createEntity("Area",room.spaceID,(0.0,0.0,0.0),(0.0,0.0,0.0),{"position":(0,0,0),"SpaceId":room.id,"radius":3000,"SpaceId":room.id,"RoomId":room.id})
		DEBUG_MSG("GetList onmapbuild{0}".format(newone.GetList(True)))
		self.centerArea=newone
	def onEnitityCreated(self,entity):
		if entity.className=="Area":
			self.centerArea=entity
	def onUpdate(self,room):#游戏进行中每一段时间呼叫一次,用于判断胜利
		#DEBUG_MSG("onupdate cell")
		playernum=len(room.teamList)/2;#每一队玩家的人数
		team1_in=0;
		team2_in=0;
		team1_d=0;
		team2_d=0;
		#检查区域并加分
		if self.centerArea!=None:
			self.inArea=self.centerArea.GetList(True)
			DEBUG_MSG("check centerArea not NULL len is{0}".format(len(self.inArea)))
			if self.inArea!=None:
				for item in self.inArea:
					if room.teamList[item]==1:
						team1_in+=1
					elif room.teamList[item]==2:
						team2_in+=1
				if team1_in==0 and team2_in!=0:
					self.point_team1+=1
				elif team1_in!=0 and team2_in==0:
					self.point_team2+=1
				DEBUG_MSG("team1 point:{0} team2 point {1}".format(self.point_team1,self.point_team2))
		if self.point_team1>=60:
			room.base.gameOver(1)
			DEBUG_MSG("win in team1 get 60 point")
			return
		if self.point_team2>=60:
			room.base.gameOver(2)
			DEBUG_MSG("win in team2 get 60 point")
			return
				#检查角色是否都死了
		
		for i in range(0,len(room.alivelist)):
			if not room.alivelist[i]:
				if room.teamList[i]==1:
					team1_d+=1
				elif room.teamList[i]==2:
					team2_d+=1
		if team1_d>=playernum and team2_d<playernum:
			room.base.gameOver(2)
			DEBUG_MSG("win in team2 kill all")
			return 
		elif team1_d<playernum and team2_d>=playernum:
			room.base.gameOver(1)
			DEBUG_MSG("win in team1 kill all")
			return
		elif team1_d>=playernum and team2_d>=playernum:
			room.base.gameOver(0)
			DEBUG_MSG("win in team1 team2 all dead")
			return

	def onAllReady(self,room):#当玩家都准备的时候判断要不要开始游戏
		team1num=0
		team2num=0
		for item in room.Playerlist:
			if item.team==1:
				team1num+=1
			elif item.team==2:
				team2num+=1
		if team1num==team2num:
			return True
		else:
			return False
			
	def onGiveTeam(self,room,roomNo):#给与新进房间的玩家team,此时还新玩家还没有加入list
		team1=0;
		team2=0;
		for item in room.Playerlist:
			if item.team==1:
				team1+=1
			elif item.team==2:
				team2+=1
		if team1<=team2:
			return 1
		else:
			return 2
	def onChangeTeam(self,room,roomNo):
		it=room.Playerlist[roomNo]
		if it.team==1:
			it.team=2
		elif it.team==2:
			it.team=1
		for item in room.Playerlist:
			KBEngine.entities[item.playerId].client.UpdateRoomInfo({"roleRoomId":it.roomNo,"roleKind":it.roleKind,"ready":it.ready,"team":it.team,"equipmentList":it.equipmentList})



class Team_Format_annihilate:
	def onMapBuild(self,room):
		pass
	def onUpdate(self,room):
		#检查角色是否都死了
		list =room.Playerlist
		playernum=len(list)/2;
		team1_d=0;
		team2_d=0;
		for item in list:
			if item.alive!=1:
				if item.team==1:
					team1_d+=1
				elif item.team==2:
					team2_d+=1
		if team1_d>=playernum and team2_d<playernum:
			room.base.gameOver(1)
		elif team1_d<playernum and team2_d>=playernum:
			room.base.gameOver(2)
		elif team1_d>=playernum and team2_d>=playernum:
			room.base.gameOver(0)
	def onAllReady(self,room):#当玩家都准备的时候判断要不要开始游戏
		team1num=0
		team2num=0
		for item in room.Playerlist:
			if item.team==1:
				team1num+=1
			elif item.team==2:
				team2num+=1
		if team1num==team2num:
			return True
		else:
			return False
	def onGiveTeam(self,room,roomNo):#给与新进房间的玩家team,此时还新玩家还没有加入list
		team1=0;
		team2=0;
		for item in room.Playerlist:
			if item.team==1:
				team1+=1
			elif item.team==2:
				team2+=1
		if team1<=team2:
			return 1
		else:
			return 2
	def onChangeTeam(self,room,roomNo):
		it=room.Playerlist[roomNo]
		if it.team==1:
			it.team=2
		elif it.team==2:
			it.team=1
		for item in room.Playerlist:
			KBEngine.entities[item.playerId].client.UpdateRoomInfo({"roleRoomId":it.roomNo,"roleKind":it.roleKind,"ready":it.ready,"team":it.team,"equipmentList":it.equipmentList})