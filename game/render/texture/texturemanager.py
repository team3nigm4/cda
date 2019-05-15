# Static class manages all textures to know which ones are loaded

from game.render.texture import texture
from game.util.logger import Logger

import json


class TextureManager:
	textureInfo = {}
	textures = {}

	# Load all textures from the json before starting the game
	@staticmethod
	def init():
		TextureManager.textureInfo = json.load(open("game/resources/textures/textures.json"))["textures"]

		TextureManager.load("", TextureManager.textureInfo)

	# Recursive method to load every textures in the texture info tree
	@staticmethod
	def load(path, value):
		for key in value:
			if type(value[key]) is type(dict()):
				TextureManager.load(path + key + "/", value[key])
			else:
				TextureManager.textures[key] = texture.Texture(path + value[key])
				if not TextureManager.textures[key].load():
					del TextureManager.textures[key]

	@staticmethod
	def bind(key):
		TextureManager.textures[key].bind()

	@staticmethod
	def state():
		Logger.info("TeManager", "Textures currently loaded :")
		print("=" * 45)
		for key in TextureManager.textures:
			print("Texture " + key)
		print("=" * 45)

	@staticmethod
	def unload():
		for key in TextureManager.textures:
			TextureManager.textures[key].unload()

		TextureManager.textures = {}

		# If there are still textures, the code will warn this
		if len(TextureManager.textures) > 0:
			Logger.error("TextureManager", "Error at the end of the program ->")
			TextureManager.state()
		else:
			Logger.info("TextureManager", "No remaining textures")

	@staticmethod
	def key(key):
		if key in TextureManager.textures:
			return key
		else:
			return "error"
