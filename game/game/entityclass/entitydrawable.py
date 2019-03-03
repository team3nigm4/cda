# Entity class to display something

from game.game.entityclass import entitycollision
from game.render.shape import entityrenderer as ed


class EntityDrawable(entitycollision.EntityCollision):

	def __init__(self, args):
		super().__init__(args)
		self.displayLayer = -1
		self.setDisplayLayer(self.em.DISPLAY_DOWN)
		self.entityRenderer = ed.EntityRenderer()
		self.setPos(self.pos)

		self.gapDisplayPos = 0

	def display(self):
		self.entityRenderer.display()

	def setPos(self, position):
		super().setPos(position)
		self.entityRenderer.updateModel([round(self.pos[0] * 32) / 32, round(self.pos[1] * 32) / 32])
		if self.displayLayer == self.em.DISPLAY_MIDDLE:
			self.em.displayMiddleEntity(self.id)

	def setDisplayLayer(self, layer):
		if not self.displayLayer == -1:
			self.em.removeToDipslay(self.displayLayer, self.id)

		# Security
		if layer >= 0 and layer <= 2:
			self.displayLayer = layer
			self.em.addToDisplay(self.displayLayer, self.id)
		else:
			print("Error : want to set an invalid display layer (" + str(layer) + ") to", self.type,"with id", str(id))

	def unload(self):
		self.entityRenderer.unload()
		if self.displayLayer >= 0 and self.displayLayer <= 2:
			self.em.removeToDipslay(self.displayLayer, self.id)
