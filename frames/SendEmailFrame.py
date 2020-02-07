import wx

from frames.MainMenuBar import MainMenuBar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


class SendEmailFrame(wx.Frame):
    def __init__(self, parent, smtpServer):
        wx.Frame.__init__(self, parent, title="Send Email", size=(400, 650), style=wx.SYSTEM_MENU | wx.CAPTION
                                                                              | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.parent = parent
        self.smtpServer = smtpServer
        self.attachmentPath = ""
        self.attachmentName = ""

        self.menuBar = MainMenuBar(self)
        self.CreateStatusBar()

        self.SetMenuBar(self.menuBar)

        self.emailTo = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.subject = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.emailText = wx.TextCtrl(self, size=(-1, 400), style=wx.TE_PROCESS_ENTER | wx.TE_MULTILINE)

        self.emailTo.SetHint("Receiver of the Email")
        self.subject.SetHint("Subject")

        self.sendEmailButton = wx.Button(self, label="Send Email")
        self.Bind(wx.EVT_BUTTON, self.OnSendEmail, self.sendEmailButton)

        self.attachFileButton = wx.Button(self, label="Attach File")
        self.Bind(wx.EVT_BUTTON, self.OnAttachFile, self.attachFileButton)

        self.attachmentText = wx.StaticText(self, label="Attachment: None")

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.emailTo, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.subject, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.emailText, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.attachFileButton, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.attachmentText, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.sendEmailButton, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)

        self.Show(True)

    def OnSendEmail(self, e):
        emailTo = self.emailTo.GetValue()
        subject = self.subject.GetValue()
        emailText = self.emailText.GetValue()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['To'] = emailTo

        body = MIMEText(emailText, "html")

        if self.attachmentPath != "":
            attachment = open(self.attachmentPath, "rb")
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {self.attachmentName}",
            )

            msg.attach(part)

        msg.attach(body)

        self.smtpServer.sendmail(self.parent.username, emailTo, msg.as_string())
        self.Close()

    def OnAttachFile(self, e):
        with wx.FileDialog(self, "Select File to be attached", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.attachmentPath = fileDialog.GetPath()
            self.attachmentName = fileDialog.GetFilename()

            self.attachmentText.SetLabelText("Attachment: " + self.attachmentName)


