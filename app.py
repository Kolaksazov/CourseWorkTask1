import wx

from frames.LoginFrame import LoginFrame

app = wx.App(False)
loginFrame = LoginFrame(None)

app.MainLoop()
