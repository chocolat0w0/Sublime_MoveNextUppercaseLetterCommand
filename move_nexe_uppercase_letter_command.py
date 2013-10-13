import sublime, sublime_plugin
import re

class MoveNextUppercaseLetterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			word = self.view.word(region)
			line = self.view.line(region)
			current_point = region.begin()
			word_start_point = word.begin()
			line_start_point = line.begin()
			m = re.search("[A-Z]", self.view.substr(line)[current_point - line_start_point + 1:])

			self.view.sel().clear()
			move_to_point = current_point + m.start() + 1
			self.view.sel().add(move_to_point)


