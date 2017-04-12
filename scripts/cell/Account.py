import KBEngine
import Math
from KBEDebug import *

class Account(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		self.setAoiRadius(5,1)
		DEBUG_MSG("account -cell- init!!!!")
		DEBUG_MSG("in space:",self.spaceID,"  direction:",self.direction,"position:",self.position,"radiu:",self.getAoiRadius())

	def createMonst(self,exposed):
		nulldic={}
		KBEngine.createEntity('Monst',1,self.position,self.direction,nulldic)
			