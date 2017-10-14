import KBEngine
import locationData
from PlayerInRoom import PlayerInRoom
from KBEDebug import *

class Point(KBEngine.Base):
	def __init__(self):
		pass
	def onLoseCell( self ):
		self.destory()