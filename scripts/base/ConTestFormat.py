import KBEngine

class Team_Format_Occupy:
	def onMapBuild(self,room):#初始化地图时呼叫
		self.centerArea=KBEngine.createBaseAnywhere("Area",{"position":(0,0,0),"SpaceId":room.id,"radius":3000,"SpaceId":room.id})
	def onUpdate(self,room):#游戏进行中每一段时间呼叫一次,用于判断胜利
		inArea=self.centerArea.GetList()
		DEBUG_MSG("check"+len(inArea))
		for item in inArea:
			pass
	def onAllReady(self,room):#当玩家都准备的时候判断要不要开始游戏
		pass
	def onGiveTeam(self,room,roomNo):#给与新进房间的玩家team
		return -1