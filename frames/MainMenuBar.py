import wx


class MainMenuBar(wx.MenuBar):
    def __init__(self, parent):
        wx.MenuBar.__init__(self)

        self.parent = parent
        fileMenu = wx.Menu()

        if parent.__class__.__name__ != "LoginFrame":
            menuNewConnection = fileMenu.Append(wx.ID_NEW, "&New Connection", "Opens new connection window")
            menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
            menuClose = fileMenu.Append(wx.ID_CLOSE, "&Close", "Close Window")

            self.Append(fileMenu, "&File")

            self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
            self.Bind(wx.EVT_MENU, self.OnNewConnection, menuNewConnection)
            self.Bind(wx.EVT_MENU, self.OnClose, menuClose)

        else:
            menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
            menuClose = fileMenu.Append(wx.ID_CLOSE, "&Close", "Close Window")

            self.Append(fileMenu, "&File")

            self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
            self.Bind(wx.EVT_MENU, self.OnClose, menuClose)

    def OnAbout(self, e):
        dialog = wx.MessageDialog(self, "Simple eMail client", "About eMail Client", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def OnNewConnection(self, e):
        from frames.LoginFrame import LoginFrame
        mainFrame = LoginFrame(None)

    def OnClose(self, e):
        self.parent.Close()


