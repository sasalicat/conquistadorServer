# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Obstacle(KBEngine.Base):
	def __init__(self):
		self.createCellEntity(KBEngine.entities[self.SpaceId].cell)
		