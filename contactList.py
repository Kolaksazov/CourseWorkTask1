import easyimap

host = 'imap.gmail.com'
user = 'cartmanusbg233@gmail.com'
password = 'cartmanbg23'
mailbox = 'INBOX'
imapper = easyimap.connect(host, user, password, mailbox, ssl=True, port=993)
messageList = []

email_quantity = 10
emails_from_your_mailbox = imapper.listids(limit=email_quantity)
messageList = imapper.listup(10)

imapper.quit()

self.horizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

# self.fromEmail = wx.StaticText(self, label="From")
# self.subject = wx.StaticText(self, label="Subject")
# self.date = wx.StaticText(self, label="Date")
#
# self.horizontalSizer.Add(self.fromEmail, 0, wx.EXPAND | wx.ALL, 20)
# self.horizontalSizer.Add(self.subject, 100, wx.EXPAND | wx.ALL, 20)
# self.horizontalSizer.Add(self.date, 0, wx.EXPAND | wx.ALL, 30)
#
self.verticalSizer = wx.BoxSizer(wx.VERTICAL)
self.verticalSizer.Add(self.sendMailButton, 0, wx.EXPAND | wx.ALL, 0)
# self.verticalSizer.Add(self.horizontalSizer, 0, wx.EXPAND | wx.ALL, 0)


# for message in contactList.messageList:
#     self.fromEmailListing = wx.StaticText(self, label=message.from_addr)
#     self.subjectEmailListing = wx.StaticText(self, label=message.title)
#     self.dateEmailListing = wx.StaticText(self, label=message.date)
#     self.openEmailButton = wx.Button(self, label=str(message.uid))
#
#     self.messageSizer = wx.BoxSizer(wx.HORIZONTAL)
#     self.messageSizer.Add(self.fromEmailListing, 0, wx.EXPAND | wx.ALL, 20)
#     self.messageSizer.Add(self.subjectEmailListing, 100, wx.EXPAND | wx.ALL, 20)
#     self.messageSizer.Add(self.dateEmailListing, 0, wx.EXPAND | wx.ALL, 20)
#     self.messageSizer.Add(self.openEmailButton, 0, wx.EXPAND | wx.ALL, 20)
#     self.verticalSizer.Add(self.messageSizer, 0, wx.EXPAND | wx.ALL, 0)
#     self.emailContent[self.openEmailButton.GetLabel()] = message.body
#     self.Bind(wx.EVT_BUTTON, self.onOpenEmail(self.openEmailButton.GetLabel()), self.openEmailButton)
