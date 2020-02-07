import wx

from frames.MainMenuBar import MainMenuBar


class DisplayEmailFrame(wx.Frame):
    def __init__(self, parent, subject, emailFrom, date, emailText):
        wx.Frame.__init__(self, parent, title=subject, size=(650, 650), style=wx.SYSTEM_MENU | wx.CAPTION
                                                                              | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.menuBar = MainMenuBar(self)
        self.CreateStatusBar()

        self.SetMenuBar(self.menuBar)

        self.subject = wx.StaticText(self, label="Subject: " + subject)
        self.emailFrom = wx.StaticText(self, label="From: " + emailFrom)
        self.date = wx.StaticText(self, label="Date: " + date)
        self.emailText = wx.TextCtrl(self, value=emailText, size=(500, 600), style=wx.TE_READONLY | wx.TE_PROCESS_ENTER
                                                                                   | wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.subject, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.emailFrom, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.date, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.emailText, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)

        self.Show(True)


