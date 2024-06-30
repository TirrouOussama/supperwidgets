from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.utils import get_color_from_hex
from kivy_gradient import Gradient



class SupperTextinput(TextInput):

	line_h = NumericProperty()
	underline_width = NumericProperty(1)   #### has to be > 0
	start_x = NumericProperty()
	end_x = NumericProperty()
	rec_x = NumericProperty()
	rec_px = NumericProperty()

	icon_offset = NumericProperty()
	icon_source = StringProperty()
	gr_left = StringProperty()
	gr_right = StringProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.start_x = 0
		self.end_x = 0
		self.rec_x = 0 
		self.rec_px = 0
		self.ref_pos = None
		self.ref_size = None

	def focused_anim(self, sz, ps):
		if self.rec_x == 0:
			self.ref_pos = ps
			self.ref_size = sz
			self.start_x = ps[0] + 20
			self.end_x = ps[0]+ sz[0]-20
			self.rec_px = ps[0] + (sz[0]/2)
			Clock.schedule_interval(self.canvas_rec_expand, 1/60)

	def textinput_line_anime(self, *args):
		if self.start_x < self.ref_pos[0] + (self.ref_size[0]/2) - 30:
			self.start_x += 4       #### this speed by which the line is moving 4px
			self.end_x -= 4 		#### this speed by which the line is moving 4px

		elif self.start_x >= self.ref_pos[0] + (self.ref_size[0]/2) - 30:
			Clock.schedule_interval(self.textinput_line_anime_2, 1/60)
			Clock.unschedule(self.textinput_line_anime)

	def textinput_line_anime_2(self, *args):
		if self.start_x >= self.ref_pos[0] + 20:
			self.start_x -= 4		#### this speed by which the line is moving 4px
			self.end_x += 4 		#### this speed by which the line is moving 4px

		elif self.start_x < self.ref_pos[0] + (self.ref_size[0]/2) - 30:
			Clock.schedule_interval(self.textinput_line_anime, 1/60)
			Clock.unschedule(self.textinput_line_anime_2)

	def on_size(self, *args):
		Clock.unschedule(self.textinput_line_anime)
		Clock.unschedule(self.textinput_line_anime_2)
		Clock.unschedule(self.canvas_rec_expand)
		self.rec_x = 0
		self.focused_anim(self.size, self.pos)

	def canvas_rec_expand(self, *args):
		if self.rec_x < self.ref_size[0]:
			self.rec_x += 8		#### this speed by which the rec is expanding
			self.rec_px -= 4 	#### this speed by which the rec is expanding

		elif self.rec_x >= self.ref_size[0]:
			self.rec_x = self.ref_size[0]
			self.rec_px = self.ref_pos[0]
			Clock.unschedule(self.canvas_rec_expand)
			Clock.schedule_interval(self.textinput_line_anime, 1/60)