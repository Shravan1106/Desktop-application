import random
import wx

class TabPanel(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

        btn = wx.Button(self, label="insert")
        btn2 = wx.Button(self, label="delete")
        btn3 = wx.Button(self, label="update")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        sizer.Add(btn3, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        self.SetSizer(sizer)
class TabPanel2(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

        btn = wx.Button(self, label="insert")
        btn2 = wx.Button(self, label="delete")
        btn3 = wx.Button(self, label="update")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        sizer.Add(btn3, 0, wx.ALIGN_LEFT|wx.ALL, 10)
        self.SetSizer(sizer)
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    def __init__(self):
        """Constructor"""        
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Notebook Tutorial",
                          size=(600,400)
                          )
        panel = wx.Panel(self)

        notebook = wx.Notebook(panel)
        tabOne = TabPanel(notebook)
        notebook.AddPage(tabOne, "Table 1")

        tabTwo = TabPanel2(notebook)
        notebook.AddPage(tabTwo, "Table 2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = DemoFrame()
    app.MainLoop()
