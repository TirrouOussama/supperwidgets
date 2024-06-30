
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty, ListProperty
from kivy.graphics.texture import Texture
from kivy.graphics import *
from kivy.core.window import Window
from kivy.lang import Builder
########################################################
from supperwidget.suppertextinput import SupperTextinput
Builder.load_file('supperwidget/suppertextinput.kv')
########################################################
class fscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)	

class theapp(App):
	def build(self):
		self.screenm = ScreenManager() 
		self.fscreen = fscreen()
		screen = Screen(name = "first screen")
		screen.add_widget(self.fscreen)
		self.screenm.add_widget(screen)
		return self.screenm

if __name__ == "__main__":
	theapp = theapp()										
	theapp.run() 