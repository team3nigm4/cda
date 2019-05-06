# This class performs the display and the update of the client

from game.inputs.inputmanager import InputManager as im
from game.screen.screens import screen
from game.render.text import text
from game.render.gui import button

from game.render.shape import guirenderer
from game.screen import gamemanager


class MenuScreen(screen.Screen):

	def __init__(self, info):
		super().__init__()

		self.title = text.Text("pixel1")
		self.title.setSize(1.3)
		self.title.setColor([1,1,1,1])
		self.title.setPosition([9, 10.5])
		self.title.setText("Coop Dungeon Adventure")

		self.copyleft = text.Text("pixel1")
		self.copyleft.setSize(0.4)
		self.copyleft.setColor([1,1,1,1])
		#self.copyleft.setPosition([18, 12])
		self.copyleft.setCentering("down-left")
		self.copyleft.setText("(C) 2019 Maxence, Alexandre & Baptiste" + " "*29 + "v.0.1")

		self.screenTitle = guirenderer.GuiRenderer()
		self.screenTitle.setImage([18, 12], "screentitle")

		def gameLocal():
			from game.screen import gamemanager
			gamemanager.GameManager.setCurrentScreen("gamescreen", [False])

		def gameMulti():
			from game.screen import gamemanager
			gamemanager.GameManager.setCurrentScreen("gamescreen", [True])

		def gameQuit():
			from game.main.window import Window
			Window.exit()

		def gameCredits():
			print("(C) 2019 Maxence, Alexandre & Baptiste")
			from game.screen import gamemanager
			gamemanager.GameManager.setCurrentScreen("creditsscreen", [True])

		self.playLocal = button.Button([9, 6.5], [5, 1], "Local", gameLocal)

		self.playMulti = button.Button([9, 5], [5, 1], "Mutltijoueur", gameMulti)
		
		self.credits = button.Button([7.7, 3.9], [2.45, 0.6], "Credits", gameCredits)
		
		self.quit = button.Button([10.3, 3.9], [2.45, 0.6], "Quitter", gameQuit)

	def init(self):
		pass

	def update(self):
			# Keys test
			if im.inputPressed(im.ESCAPE):
				from game.main.window import Window
				Window.exit()

			self.playLocal.update()
			self.playMulti.update()
			self.credits.update()
			self.quit.update()

	def display(self):
		self.screenTitle.display()
		self.title.display()
		self.copyleft.display()
		self.playLocal.display()
		self.playMulti.display()
		self.credits.display()
		self.quit.display()

	def unload(self):
		self.screenTitle.unload()
		self.title.unload()
		self.copyleft.unload()
		self.playLocal.unload()
		self.playMulti.unload()
		self.credits.unload()
		self.quit.unload()

