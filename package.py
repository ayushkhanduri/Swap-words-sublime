import sublime
import sublime_plugin


class CnpremailerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		if(len(view.sel()) ==2):
			first = self.view.substr(view.sel()[0])
			second = self.view.substr(view.sel()[1])
			view.replace(edit,view.sel()[1],first)
			view.replace(edit,view.sel()[0],second)
