import KBEngine
import Math
from KBEDebug import *
import ConTestFormat

class Room(KBEngine.Entity):
	teamList=[]
	alivelist=[]
	def setFormat(self):
		if self.ContextKindCell==1:
			self.Format=ConTestFormat.Team_Format_Occupy()
		elif self.ContextKindCell==2:
			self.Format=ConTestFormat.Team_Format_annihilate()
	def __init__(self):
		KBEngine.Entity.__init__(self)
		#self.setAoiRadius(100,0)
		DEBUG_MSG("room init<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<spaceId{0} {1}".format(self.spaceID,self.getAoiRadius()))
		self.setFormat()#设置赛制
		self.Format.onMapBuild(self)#初始化地图
	def cleanAllEntity(self):#清除场地上的所有entity
		self.delTimer(self.updateTimer)#注销计时器
		allEntity=self.entitiesInRange(100)
		DEBUG_MSG(allEntity)
		for e in allEntity:
			if e!=self:
				DEBUG_MSG("in clean!!!",type(e))
				e.destroy()
		self.Format.onMapBuild(self)
	def InitTeamList(self,teamList):
		self.teamList=teamList
		self.alivelist=[]
		for t in teamList:
			self.alivelist.append(True)
		DEBUG_MSG("InitTeamList OK alivelist:{0}".format(self.alivelist))
		self.updateTimer=self.addTimer(1,1,2)#添加周期检查计时器
	def onTimer( self, timerHandle, userData ):
		#DEBUG_MSG("cell on timer userdata{0}".format(userData))
		if userData==2:#周期性赛制检查
			#DEBUG_MSG("wait on update")
			self.Format.onUpdate(self)
	def onEnteredAoI( self, entity ):
		DEBUG_MSG("enter AOI:{0}".format(entity))
		Format.onEnitityCreated(entity)
	def afterCreate(self,eid):
		DEBUG_MSG(">>>after create!!!<<<")
		Format.onEnitityCreated(KBEngine.entities[eid])
	def setDied(self,roomNo,code):
		if code<=0:
			self.alivelist[roomNo]=False
		else:
			self.alivelist[roomNo]=True
	def clientLoadFinish(self):
		self.Format.onLoadFinish(self)
	def destroyItSpace(self):
		self.destroySpace()
		DEBUG_MSG("room destroy clear-------------------------------------")
	#def onDestroy( self ):#当自己被销毁时
	#	allEntity=self.entitiesInRange(100)
	#	for e in allEntity:
	#		if e!=self:
	#			DEBUG_MSG("in room destroy!!!",type(e))
	#			e.destroy()