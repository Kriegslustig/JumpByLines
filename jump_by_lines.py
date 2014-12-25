import sublime, sublime_plugin

class JumpByLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit, by = 1, direction = "backward"):
    line, column = self.view.rowcol(self.view.sel()[0].begin())
    if(direction == "forward"):
      pt = self.view.text_point(line + by, column)
    else:
      pt = self.view.text_point(line - by, column)

    self.view.sel().clear()
    self.view.sel().add(sublime.Region(pt))

    self.view.show(pt)