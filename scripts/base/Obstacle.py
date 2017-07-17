# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Obstacle(KBEngine.Base):
	def __init__(self):
		DEBUG_MSG("Obstacle base init !!!")
		self.createCellEntity(KBEngine.entities[self.SpaceId].cell)
