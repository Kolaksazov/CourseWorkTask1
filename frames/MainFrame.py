import wx
import wx.grid

from frames.MainMenuBar import MainMenuBar
from frames.SendEmailFrame import SendEmailFrame
from frames.DisplayEmailFrame import DisplayEmailFrame


class MainFrame(wx.Frame):
    def __init__(self, parent, imapServer, smtpServer, username, emailPage):
        wx.Frame.__init__(self, parent, title="Email Client", size=(850, 600), style=wx.SYSTEM_MENU | wx.CAPTION
                                                                              | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.imapServer = imapServer
        self.smtpServer = smtpServer
        self.username = username
        self.emailPage = emailPage
        self.emailList = []

        self.menuBar = MainMenuBar(self)
        self.CreateStatusBar()

        self.SetMenuBar(self.menuBar)

        self.sendMailButton = wx.Button(self, label="Send Email")
        self.Bind(wx.EVT_BUTTON, self.OnSendEmail, self.sendMailButton)

        self.nextPageButton = wx.Button(self, label="Next Page")
        self.previousPageButton = wx.Button(self, label="Previous Page")
        self.Bind(wx.EVT_BUTTON, self.OnNextPage, self.nextPageButton)
        self.Bind(wx.EVT_BUTTON, self.OnPreviousPage, self.previousPageButton)

        self.horizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontalSizer.Add(self.previousPageButton, 0, wx.EXPAND | wx.ALL, 0)
        self.horizontalSizer.Add(self.nextPageButton, 0, wx.EXPAND | wx.ALL, 0)

        self.flexGridEmailSizer = self.ReturnEmailSizer(self.imapServer, self.emailPage)

        self.verticalSizer = wx.BoxSizer(wx.VERTICAL)
        self.verticalSizer.Add(self.sendMailButton, 0,  wx.ALL, 10)
        self.verticalSizer.Add(self.flexGridEmailSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.verticalSizer.Add(self.horizontalSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(self.verticalSizer)
        self.Show()

    def OnSendEmail(self, e):
        sendEmailFrame = SendEmailFrame(self, self.smtpServer)

    def OnOpenEmail(self, email):
        def OnClick(event):
            emailObject = self.emailList[email]
            displayEmailFrame = DisplayEmailFrame(self, emailObject.title, emailObject.from_addr, emailObject.date, emailObject.body)
        return OnClick

    def OnNextPage(self, e):
        mainframe = MainFrame(None, self.imapServer, self.smtpServer, self.username, self.emailPage + 10)
        self.Destroy()

    def OnPreviousPage(self, e):
        if self.emailPage > 0:
            mainframe = MainFrame(None, self.imapServer, self.smtpServer, self.username, self.emailPage - 10)
            self.Destroy()

    def ReturnEmailSizer(self, imapServer, start):
        emailQuantity = start + 10
        self.emailList = imapServer.listup(emailQuantity)

        number = wx.StaticText(self, label="Number", size=(50, 15))
        fromEmail = wx.StaticText(self, label="From", size=(100, 15))
        subject = wx.StaticText(self, label="Subject", size=(350, 15))
        date = wx.StaticText(self, label="Date", size=(100, 15))
        open = wx.StaticText(self, label="Open", size=(100, 15))

        flexGridEmailSizer = wx.FlexGridSizer(11, 5, 10, 10)
        flexGridEmailSizer.Add(number)
        flexGridEmailSizer.Add(fromEmail)
        flexGridEmailSizer.Add(subject)
        flexGridEmailSizer.Add(date)
        flexGridEmailSizer.Add(open)

        i = start
        while i < start + 10:
            currentEmail = self.emailList[i]

            numberEmail = wx.StaticText(self, label=str(i), size=(50, 15))
            fromEmailEmail = wx.StaticText(self, label=currentEmail.from_addr, size=(100, 15))
            subjectEmail = wx.StaticText(self, label=currentEmail.title, size=(330, 15))
            dateEmail = wx.StaticText(self, label=currentEmail.date, size=(100, 15))
            openEmail = wx.Button(self, label="Open")
            openEmail.Bind(wx.EVT_BUTTON, self.OnOpenEmail(i))

            flexGridEmailSizer.Add(numberEmail)
            flexGridEmailSizer.Add(fromEmailEmail)
            flexGridEmailSizer.Add(subjectEmail)
            flexGridEmailSizer.Add(dateEmail)
            flexGridEmailSizer.Add(openEmail)

            i += 1
        return flexGridEmailSizer



