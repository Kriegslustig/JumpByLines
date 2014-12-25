import sublime, sublime_plugin

class JumpByLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit, by = 1, direction = "backward"):
    if(direction == "forward"):
      line, column = self.view.rowcol(self.view.sel()[0].begin())
      pt = self.view.text_point(line + by, 0)
    else:
      line, column = self.view.rowcol(self.view.sel()[0].begin())
      pt = self.view.text_point(line - by, 0)

    self.view.sel().clear()
    self.view.sel().add(sublime.Region(pt))

    self.view.show(pt)