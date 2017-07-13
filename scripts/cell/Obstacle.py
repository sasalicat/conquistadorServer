import KBEngine
import Math
from KBEDebug import *

class Obstacle(KBEngine.Entity):
	def __init__(self):
		DEBUG_MSG("Obstacle cell init !!!")
	def reduceHp(self,expose,damageNum):
		self.Hp-=damageNum
	def method_Null(self,expose):
		self.allClients.methodNull()
	def methodSbyte(self,data,expose):
		self.allClients.methodSbyte(data)