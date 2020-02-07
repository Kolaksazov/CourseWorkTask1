import wx
import smtplib
import ssl
import email
import imaplib
import easyimap

from frames.MainFrame import MainFrame
from frames.MainMenuBar import MainMenuBar


class LoginFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Login", size=(400, 290), style=wx.SYSTEM_MENU | wx.CAPTION
                                                                              | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.menuBar = MainMenuBar(self)
        self.CreateStatusBar()

        self.SetMenuBar(self.menuBar)

        # Create Text Box
        self.imapServer = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.smtpServer = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.port = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.userName = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

        # Set Placeholders
        self.imapServer.SetHint("IMAP Server")
        self.smtpServer.SetHint("SMTP Server")
        self.port.SetHint("SMTP Port")
        self.userName.SetHint("Username")
        self.password.SetHint("Password")

        # Create Button
        self.loginButton = wx.Button(self, label="Login")
        self.Bind(wx.EVT_BUTTON, self.OnLogin, self.loginButton)

        # Create Sizer and add elements
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.imapServer, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.smtpServer, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.port, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.userName, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.password, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.loginButton, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)

        self.Show(True)

    def OnLogin(self, e):
        imapServerText = self.imapServer.GetValue()
        smtpServerText = self.smtpServer.GetValue()
        portText = self.port.GetValue()
        userNameText = self.userName.GetValue()
        passwordText = self.password.GetValue()

        context = ssl.create_default_context()

        try:
            smtpServer = smtplib.SMTP_SSL(smtpServerText, portText, context=context)
            imapServer = easyimap.connect(imapServerText, userNameText, passwordText, 'INBOX', ssl=True, port=993)
            smtpServer.login(userNameText, passwordText)
            mainFrame = MainFrame(None, imapServer, smtpServer, userNameText, 0)
            self.Close()

        except smtplib.SMTPServerDisconnected as e:
            exceptionDialog = wx.MessageDialog(self, "Please put correct Login and Server Information", "SMTP Login Error", wx.OK)
            exceptionDialog.ShowModal()
            exceptionDialog.Destroy()

        except Exception as e:
            exceptionDialog = wx.MessageDialog(self, str(e), "Login Error", wx.OK)
            exceptionDialog.ShowModal()
            exceptionDialog.Destroy()


