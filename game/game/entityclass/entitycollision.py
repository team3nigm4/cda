from game.game.entityclass import entity


class EntityCollision(entity.Entity):


	# NO_STATE = 0
	# GIVE_STATE = 1
	# TAKE_STATE = 2

	def __init__(self, args):
		super().__init__(args)
		self.colSize = [1,1]
		self.halfColSize = [0.5,0.5]

		self.entCol = False
		self.inMov = [False, False]
		self.speed = [0,0]

		self.attributes = {
			"collision": 0,
			"interaction": 0,
			"heavy": 0,
			"damage": 0,
		}

	def setColBox(self, size, test):
		self.colSize = size
		self.halfColSize[0] = self.colSize[0]/2
		self.halfColSize[1] = self.colSize[1]/2

		self.entCol = test
		from game.game.entityclass.entitymanager import EntityManager as em
		if self.entCol:
			em.addToTest(self.id)
		else:
			em.removeToTest(self.id)

