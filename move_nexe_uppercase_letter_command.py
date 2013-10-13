import sublime, sublime_plugin
import re

def isSelectedMode(view):
	return view.sel()[0].begin() != view.sel()[0].end()

class MoveNextUppercaseLetterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = self.view.line(region)
			current_start_point = region.begin()
			current_end_point = region.end()
			line_start_point = line.begin()
			m = re.search("[A-Z]", self.view.substr(line)[current_end_point - line_start_point + 1:])

			move_to_point = current_end_point + m.start() + 1
			self.view.sel().clear()
			if (isSelectedMode(self.view)):
				self.view.sel().add(sublime.Region(current_start_point, move_to_point))
			else:
				self.view.sel().add(move_to_point)


