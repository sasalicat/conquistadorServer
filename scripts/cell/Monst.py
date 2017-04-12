import KBEngine
import Math
from KBEDebug import *
class Monst(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("Monst -cell- init!!!!")
		traget=Math.Vector3(self.position.x,self.position.y+100,self.position.z)
		self.moveToPoint(traget,1,0,None,True,True)
		#self.addTimer(0.5,0.5,0)

		DEBUG_MSG("in space:",self.spaceID,"  direction:",self.direction,"position:",self.position,"radiu:",self.getAoiRadius())
		
	def onTimer(self,id,userArg):
		if userArg==0:
			traget=Math.Vector3(self.position.x,self.position.y+1,self.position.z)
			self.moveToPoint(traget,1,0,None,True,True)
			DEBUG_MSG("on timer")
	