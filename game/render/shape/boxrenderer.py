# Class to instance, use it to render a box

from game.render.shape import shape
from game.render.shader.shadermanager import ShaderManager as sm
from game.util import matrix4f


class BoxRenderer:
	# Shader false : box shader, shader true : box-hud shader
	def __init__(self, size, color, shader=False):
		self.size = size
		self.color = color

		quad = [0.0, 0.0, 0.0, 				self.color[0], self.color[1], self.color[2], self.color[3],
				size[0], 0.0, 0.0, 			self.color[0], self.color[1], self.color[2], self.color[3],
				size[0], size[1], 0.0, 		self.color[0], self.color[1], self.color[2], self.color[3],
				0.0, size[1], 0.0, 			self.color[0], self.color[1], self.color[2], self.color[3]]

		indices = [0, 1, 2,
				2, 3, 0]

		self.setShader(shader)

		self.shape = shape.Shape(self.shaderName, True)
		self.shape.setStorage(shape.Shape.STATIC_STORE, shape.Shape.STATIC_STORE)
		self.shape.setEbo(indices)
		self.shape.setVbo(quad)
		self.shape.setReading([3, 4])

		self.model = matrix4f.Matrix4f(True)

	def display(self):
		sm.updateLink(self.shaderName, "model", self.model.matrix)
		self.shape.display()

	# Define the size and the color of the box render
	def setAttributes(self, size, color):
		self.color = color
		self.size = size
		quad = [0, 0, 0.0, 						self.color[0], self.color[1], self.color[2], self.color[3],
				size[0], 0, 0.0, 				self.color[0], self.color[1], self.color[2], self.color[3],
				size[0], size[1], 0.0, 			self.color[0], self.color[1], self.color[2], self.color[3],
				0, size[1], 0.0, 				self.color[0], self.color[1], self.color[2], self.color[3]]

		self.shape.setVbo(quad)

	def setShader(self, shader):
		self.shader = shader
		if self.shader:
			self.shaderName = "box-hud"
		else:
			self.shaderName = "box"

	# Update the position of the renderer
	def updateModel(self, newPos):
		if self.shader:
			self.model.matrix[3][0] = newPos[0] - self.size[0] / 2 - 9
			self.model.matrix[3][1] = newPos[1] - self.size[1] / 2 - 8
		else:
			self.model.matrix[3][0] = newPos[0] - self.size[0] / 2
			self.model.matrix[3][1] = newPos[1] - self.size[1] / 2

	def unload(self):
		self.shape.unload()
