import KBEngine
import Math
import random
from KBEDebug import *

class Player(KBEngine.Entity):
	InWhichRoomEntityId=-1
	def __init__(self):
		DEBUG_MSG("players cell init !!!%d" %self.InWhichRoomEntityId)
	def updateZ(self,expose,newz):
		self.allClients.updateZ(newz)
	def notify1(self,expose,Pos,action):
		self.allClients.receive1(Pos,action)
	def notify2(self,expose,roomNo,action,dirZ):#用于同步转向
		self.allClients.receive2(roomNo,action,dirZ)
	def notify3(self,expose,equipmentIndex,playerPos,mousePos):#用于主动技能
		randomNum=random.randint(0,99)
		self.allClients.receive3(equipmentIndex,playerPos,mousePos,randomNum)
	def notify4(self,expose,playerPos,eulerAngles,damagerPos,damagerNo,kind,num,stiff,makeConversaly,hitConversaly):#用于传伤害
		randomNum=random.randint(0,99)
		self.allClients.receive4(playerPos,eulerAngles,damagerPos,damagerNo,kind,num,stiff,makeConversaly,hitConversaly,randomNum)
	def notify5(self,expose,treaterNo,treatNum):
		randomNum=random.randint(0,99)
		self.allClients.receive5(treaterNo,treatNum,randomNum)
	def setRoomId(self,roomId):
		DEBUG_MSG("set roomId %d" %roomId)
		self.InWhichRoomEntityId=roomId