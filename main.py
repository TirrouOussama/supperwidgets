
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
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
from supperwidget.supperbutton import SupperButton
Builder.load_file('supperwidget/supperbutton.kv')
from supperwidget.supperlabel import SupperLabel
Builder.load_file('supperwidget/supperlabel.kv')

########################################################
class fscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)	

	def modify_lbl(self):
		self.ids.lbl.text_saved = 'SupperLabel has been modified'
		self.ids.lbl.text = ''
		self.ids.lbl.letters_list = list(self.ids.lbl.text_saved)
		
		Clock.unschedule(self.ids.lbl.animate_text)
		self.ids.lbl.cnt_anim = 0
		Clock.schedule_interval(self.ids.lbl.animate_text, 0.2)

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
