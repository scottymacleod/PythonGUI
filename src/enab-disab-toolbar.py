#!/usr/bin/python

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddLabelTool(wx.ID_UNDO, '', wx.Bitmap('../img/tundo.png'))
        tredo = self.toolbar.AddLabelTool(wx.ID_REDO, '', wx.Bitmap('../img/tredo.png'))
        self.toolbar.EnableTool(wx.ID_REDO,False)
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('../img/exit.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

        self.SetSize((600,400))
        self.SetTitle('Undo Redo')
        self.Centre()
        self.Show(True)

    def OnUndo(self, e):
        if self.count > 1 and self.count <=5:
            self.count = self.count - 1
        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO,True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >= 1:
            self.count = self.count + 1
        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnQuit(self, e):
        self.Close()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
