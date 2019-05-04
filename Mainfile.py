import wx
import random
import MySQLdb
import sys
from twilio.rest import Client




# Open database connection
db = MySQLdb.connect("localhost","shravan","shravan","supermarket" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

'''def send_sms(msg, to):
		
	sid = "ACb78f700e33a4fd49b88732b4ae9ff98d"
	auth_token = "6d18566e439f4849ab824e0594871f51"
	twilio_number = "+19186094397"
	#client = TwilioRestClient(sid, auth_token)
	tClient= Client(sid, auth_token)
	message = tClient.messages.create(body=msg,
									from_='+19186094397',
									to='+919121931106',
									)'''


class LoginDialog3(wx.Dialog):
	   
	def __init__(self):
		
		wx.Dialog.__init__(self, None, title="customer Login")
		self.logged_in = False
		# user info
		user_sizer = wx.BoxSizer(wx.HORIZONTAL)

		user_lbl = wx.StaticText(self, label="Username:")
		user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.user = wx.TextCtrl(self)
		user_sizer.Add(self.user, 0, wx.ALL, 5)

		# pass info
		p_sizer = wx.BoxSizer(wx.HORIZONTAL)

		p_lbl = wx.StaticText(self, label="Password:")
		p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.password = wx.TextCtrl(
			self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
		self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
		p_sizer.Add(self.password, 0, wx.ALL, 5)

		self.x_sizer = wx.BoxSizer(wx.HORIZONTAL)
		#self.x_lbl = wx.StaticText(self, label="username or password is incorrect")
		# self.x_lbl.Hide()
		self.main_sizer = wx.BoxSizer(wx.VERTICAL)
		self.main_sizer.Add(user_sizer, 0, wx.ALL, 5)
		self.main_sizer.Add(p_sizer, 0, wx.ALL, 5)

		btn = wx.Button(self, label="Login")
		btn.Bind(wx.EVT_BUTTON, self.onLogin)
		self.main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)
		#self.x_sizer.Add(self.x_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.main_sizer.Add(self.x_sizer, 0, wx.ALL, 5)
		
		self.SetSizer(self.main_sizer)

	# ----------------------------------------------------------------------
	def onLogin(self, event):
		"""
		Check credentials and login
		"""
		self.user_name=self.user.GetValue()
		sql=("select * from clogin where lid='"+self.user_name+"';")
		cursor=self.query(sql)
		x=cursor.fetchone()
		
		k1=""
		k2=""
		k1=str(x[0])
		k2=str(x[1])
		user_password = self.password.GetValue()
		if user_password == k2:
			print("You are now logged in!")
			d=Customer1(None)
			d.Show()
			self.logged_in = True
			self.Close()
			

		elif self.user_name=="" or user_password!=k2 :
			 wx.MessageBox('Username or password is incorrect!',
						  'Enter Again', wx.OK | wx.ICON_INFORMATION)
	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor


class Customer1(wx.Frame):
			
	def __init__(self,*args, **kwargs):
		super(Customer1,self).__init__(*args, **kwargs)
		self.Maximize()
		self.details()

	def details(self):
		sql="select * from customers where lid='%s'" %(s.user_name)
		cursor=self.query(sql)
		m=cursor.fetchone()
		print m
		panel=wx.Panel(self)
		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(20)
		sizer=wx.GridBagSizer(10,10)
		st1=wx.StaticText(panel,label="ID:")
		st4=wx.StaticText(panel,label=str(m[0]))
		st2=wx.StaticText(panel,label="Name:")
		st5=wx.StaticText(panel,label=str(m[1]))
		st3=wx.StaticText(panel,label="PhNo:")
		st6=wx.StaticText(panel,label=str(m[2]))
		st1.SetFont(font)
		st2.SetFont(font)
		st3.SetFont(font)
		st4.SetFont(font)
		st5.SetFont(font)
		st6.SetFont(font)
		sizer.Add(st1,pos=(10,25),flag=wx.ALIGN_CENTER)
		sizer.Add(st2,pos=(12,25),flag=wx.ALIGN_CENTER)
		sizer.Add(st3,pos=(14,25),flag=wx.ALIGN_CENTER)
		sizer.Add(st4,pos=(10,28),flag=wx.ALIGN_CENTER)
		sizer.Add(st5,pos=(12,28),flag=wx.ALIGN_CENTER)
		sizer.Add(st6,pos=(14,28),flag=wx.ALIGN_CENTER)


		btn1=wx.Button(panel,label="Edit",size=(100,50))
		btn2=wx.Button(panel,label="view payments",size=(200,50))
		btn3=wx.Button(panel,label="Log OUt",size=(150,50))
		sizer.Add(btn1,pos=(25,25))
		sizer.Add(btn2,pos=(25,28))
		sizer.Add(btn3,pos=(25,31))
		panel.Bind(wx.EVT_BUTTON,self.OnClicked1,id = btn1.GetId())
		panel.Bind(wx.EVT_BUTTON,self.OnClicked2,btn2)
		panel.Bind(wx.EVT_BUTTON,self.OnClicked3,btn3)

		panel.SetSizerAndFit(sizer)

		#self.SetSize((500, 500))
		self.SetTitle('Customer')
		self.Center()
		
		panel.Layout()

	def OnClicked1(self,e):
			
		Update4(None)

	def OnClicked2(self,e):
		
		View(None)
		

	def OnClicked3(self,e):
		self.Destroy()

	

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
			self.connect()
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		return cursor


class View(wx.Frame):
	def __init__(self, parent):
			
		super(View,self).__init__(parent)
		self.Maximize()
		sql="select * from customers where lid='%s'" %(s.user_name)
		cursor = self.query(sql)
		tuples = cursor.fetchall()
		gbs=wx.GridBagSizer(5,5)
		width,height=wx.GetDisplaySize()
		self.list = wx.ListCtrl(self, -1, size=(-1,200),style = wx.LC_REPORT)
		self.list.InsertColumn(0, 'c_ID',wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(1, 'c_Name', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(2, 'phNo', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(3, 'Bill', wx.LIST_FORMAT_CENTER, width/4-20)
		for i in tuples:
		   k1=str(i[0])
		   k2=str(i[1])
		   k3=str(i[2])
		   k4=str(i[6])
		   index = self.list.InsertStringItem(sys.maxint,k1)
		   self.list.SetStringItem(index, 1, k2)
		   self.list.SetStringItem(index, 2, k3)
		   self.list.SetStringItem(index, 3, k4)
		gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)
		q="NULL"
		sql="select * from bill"+str(k4)
		# sql="select * from bill"+k4+" where lid='"+s.user_name+"'" 
		cursor = self.query(sql)
		bills = cursor.fetchall()
		self.list = wx.ListCtrl(self, -1, size=(-1,300),style = wx.LC_REPORT)
		self.list.InsertColumn(0, 'Pname',wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(1, 'Price', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(2, 'NoItems', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(3, 'Amount', wx.LIST_FORMAT_CENTER, width/4-20) 

		for i in bills:
			f1=str(i[1])
			f2=str(i[2])
			f3=str(i[3])
			f4=str(i[4])
			index = self.list.InsertStringItem(sys.maxint,f1)
			self.list.SetStringItem(index, 1, f2)
			self.list.SetStringItem(index, 2, f3)
			self.list.SetStringItem(index, 3, f4)
			
		gbs.Add(self.list, pos = (11,0),span=(7,14),flag = wx.ALL, border = 5)

		btn2=wx.Button(self,label="back",size=(80,40))
		gbs.Add(btn2, pos = (18, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

		self.SetSizerAndFit(gbs)
		self.Centre()
		self.Show()

	def connect(self):
			self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
			self.connect()
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		return cursor

	
class Update4(wx.Frame):
	def __init__(self, parent):
		super(Update4,self).__init__(parent)

		self.Maximize()

	
		self.gbs=wx.GridBagSizer(5,5)
	
		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(17)
		
		sql="select * from customers where lid='%s'" %(s.user_name)
		cursor = self.query(sql)
		x=cursor.fetchone()
		print x
		st1=wx.StaticText(self,label="c_Name:")
		st1.SetFont(font)
		self.tc1=wx.TextCtrl(self,-1,str(x[1]),size=(15,100))
		st2=wx.StaticText(self,label="phNo:")
		st2.SetFont(font)
		self.tc2=wx.TextCtrl(self,-1,str(x[2]),size=(15,100))
		st3=wx.StaticText(self,label="address:")
		st3.SetFont(font)
		self.tc3=wx.TextCtrl(self,-1,str(x[4]),size=(15,100))
		st4=wx.StaticText(self,label="email:")
		st4.SetFont(font)
		self.tc4=wx.TextCtrl(self,-1,str(x[3]),size=(15,100))
		
		update=wx.Button(self,label="update")
		self.gbs.Add(st1, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
		self.gbs.Add(self.tc1, pos = (9, 29),span=(1,15), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
		self.gbs.Add(st2, pos = (12, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
		self.gbs.Add(self.tc2, pos = (12,29), span=(1,15), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
		self.gbs.Add(st3, pos = (14,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
		self.gbs.Add(self.tc3, pos = (14, 29),span=(1,15), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
		self.gbs.Add(st4, pos = (16,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
		self.gbs.Add(self.tc4, pos = (16, 29),span=(1,15), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
		
		self.gbs.Add(update, pos = (18,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

		self.Bind(wx.EVT_BUTTON, self.update, update)
		self.SetSizerAndFit(self.gbs)
		self.Centre()
		self.Show()

	def update(self,e):
		
		sql="update customers set cname='%s',mnumber=%s,email='%s',address='%s' where lid='%s'" %(self.tc1.GetValue(),self.tc2.GetValue(),self.tc4.GetValue(),self.tc3.GetValue(),s.user_name)
		cursor = self.query(sql)
		

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
			self.connect()
			cursor = self.conn.cursor()
			cursor.execute(sql)
			self.conn.commit()
		return cursor



 

class LoginDialog2(wx.Dialog):
   
	def __init__(self):
		
		wx.Dialog.__init__(self, None, title="Admin Login")
		self.logged_in = False
		# user info
		user_sizer = wx.BoxSizer(wx.HORIZONTAL)

		user_lbl = wx.StaticText(self, label="Username:")
		user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.user = wx.TextCtrl(self)
		user_sizer.Add(self.user, 0, wx.ALL, 5)

		# pass info
		p_sizer = wx.BoxSizer(wx.HORIZONTAL)

		p_lbl = wx.StaticText(self, label="Password:")
		p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.password = wx.TextCtrl(
			self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
		self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
		p_sizer.Add(self.password, 0, wx.ALL, 5)

		self.x_sizer = wx.BoxSizer(wx.HORIZONTAL)
		#self.x_lbl = wx.StaticText(self, label="username or password is incorrect")
		# self.x_lbl.Hide()
		self.main_sizer = wx.BoxSizer(wx.VERTICAL)
		self.main_sizer.Add(user_sizer, 0, wx.ALL, 5)
		self.main_sizer.Add(p_sizer, 0, wx.ALL, 5)

		btn = wx.Button(self, label="Login")
		btn.Bind(wx.EVT_BUTTON, self.onLogin)
		self.main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)
		#self.x_sizer.Add(self.x_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.main_sizer.Add(self.x_sizer, 0, wx.ALL, 5)
		
		self.SetSizer(self.main_sizer)

	# ----------------------------------------------------------------------
	def onLogin(self, event):
		"""
		Check credentials and login
		"""
		user_name=self.user.GetValue()
		sql=("select * from admin where admin='"+user_name+"';")
		cursor=self.query(sql)
		x=cursor.fetchall()
		print (x)
		k1=""
		k2=""
		for i in x:
			k1=str(i[0])
			k2=str(i[1])
		
		user_password = self.password.GetValue()
		if user_password == k2:
			print("You are now logged in!")
			self.logged_in = True
			self.Close()
		elif user_name=="" or user_password!=k2 :
			 wx.MessageBox('Username or password is incorrect!',
						  'Enter Again', wx.OK | wx.ICON_INFORMATION)
	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor
			

			# self.x_lbl.Show()
			
			# self.SetSizer(self.main_sizer)
			# print("Username or password is incorrect!")
			

class Mainwindow(wx.Frame):
		
	def __init__(self,*args, **kwargs):
		super(Mainwindow,self).__init__(*args, **kwargs)
		self.Maximize()
		self.Login()

	def Login(self):
		panel=wx.Panel(self)
		sizer=wx.GridBagSizer(10,10)
		btn1=wx.Button(panel,label="customer")
		btn2=wx.Button(panel,label="admin")
		
		sizer.Add(btn1,pos=(5,5))
		sizer.Add(btn2,pos=(7,5))
		panel.Bind(wx.EVT_BUTTON,self.OnClicked1,btn1)
		panel.Bind(wx.EVT_BUTTON,self.OnClicked2,btn2)
		

		panel.SetSizerAndFit(sizer)

		#self.SetSize((500, 500))
		self.SetTitle('Main Window')
		self.Center()
		
		self.Layout()
		
	def OnClicked1(self,e):
		s.Show()
		dlg = LoginDialog3()
		dlg.ShowModal()
		authenticated = dlg.logged_in
		# if authenticated:
			# c=Customer1(None)
			# c.Show()
		

	def OnClicked2(self,e):
		dlg = LoginDialog2()
		dlg.ShowModal()
		authenticated = dlg.logged_in
		
		if authenticated:
			p1 = SuperMarket(None)
			p1.Show()

class SuperMarket2(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(SuperMarket2,self).__init__(*args, **kwargs)
		self.Maximize()

		self.Vbar()

	def Vbar(self):
		panel = wx.Panel(self)

		self.notebook = wx.Notebook(panel)
		tabOne = TabPanel(self.notebook)
		self.notebook.AddPage(tabOne, "products")

		tabTwo = TabPanel2(self.notebook)
		self.notebook.AddPage(tabTwo, "customers")

		tabThree = TabPanel3(self.notebook)
		self.notebook.AddPage(tabThree, "payments")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)
		panel.SetSizer(sizer)
		self.Layout()
		self.Show()


class SuperMarket(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(SuperMarket,self).__init__(*args, **kwargs)
		self.Maximize()
		self.count=100
		self.count1=0
		self.Mbar()

	def Mbar(self):
		menubar=wx.MenuBar()
		self.font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(15)

		#File Menu
		fileMenu=wx.Menu()
		fileMenu.Append(wx.ID_NEW,'&New')
		fileMenu.Append(wx.ID_OPEN,'&Open')
		fileMenu.Append(wx.ID_SAVE,'&Save')
		fileMenu.AppendSeparator()

		imp=wx.Menu()
		imp.Append(wx.ID_ANY,'Import files')
		imp.Append(wx.ID_ANY,'Import images')
		imp.Append(wx.ID_ANY,'Import audio or video')

		fileMenu.AppendMenu(wx.ID_ANY,'I&mport',imp)
		fileItem=fileMenu.Append(wx.ID_EXIT,'&Quit')


		self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)

		#Edit Menu
		editMenu = wx.Menu()
		editMenu.Append(wx.ID_COPY,'&Copy')
		editMenu.Append(wx.ID_CUT,'&Cut')
		editMenu.Append(wx.ID_PASTE,'&Paste')
		editMenu.AppendSeparator()
		editMenu.Append(wx.ID_SELECTALL,'Select All')
		editMenu.Append(wx.ID_PREFERENCES,'Preferences')

		#view menu
		viewMenu=wx.Menu()
		self.shtl=viewMenu.Append(wx.ID_ANY,'Show ToolBar',kind=wx.ITEM_CHECK)
		self.shst=viewMenu.Append(wx.ID_ANY,'Show StatusBar',kind=wx.ITEM_CHECK)

		viewMenu.Check(self.shtl.GetId(),True)
		viewMenu.Check(self.shst.GetId(),True)

		self.Bind(wx.EVT_MENU,self.ToggleToolBar,self.shtl)
		self.Bind(wx.EVT_MENU,self.ToggleStatusBar,self.shst)

		self.toolbar=self.CreateToolBar()
		self.toolbar.Realize()

		self.statusbar=self.CreateStatusBar()
		self.statusbar.SetStatusText('Ready')

		menubar.Append(fileMenu,'&File')
		menubar.Append(editMenu, '&Edit')
		menubar.Append(viewMenu,'&View')
		self.SetMenuBar(menubar)

		self.SetSize((500,500))
		self.SetTitle('Super Market')
		self.Center()

		# HomePage
		self.width, self.height = wx.GetDisplaySize()
		self.two = wx.Panel(self, size=(self.width, self.height))
		# self.two.SetBackgroundColour('grey')
		main1 = wx.GridBagSizer(10, 10)
		bill = wx.Button(self.two, label="Billing")
		# info = wx.Button(self.two, label="Info")
		tables=wx.Button(self.two,label="Tables")
		main1.Add(bill, pos=(30, 60), flag=wx.ALL, border=5)
		# main1.Add(info, pos=(30, 40), flag=wx.ALL, border=5)
		main1.Add(tables,pos=(30,20),flag=wx.ALL, border=5)
		self.two.SetSizer(main1)
		self.Bind(wx.EVT_BUTTON, self.billingfun, id=bill.GetId())
		#self.Bind(wx.EVT_BUTTON, self., id=info.GetId())
		self.Bind(wx.EVT_BUTTON,self.OnClicked3,tables)
		# hp = "hp.png"
		# bmp1 = wx.Image(hp,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		# bitmap1=wx.StaticBitmap(self.two,-1,bmp1,(0,0),size=(self.width,self.height))
		# str1 = "%s %d%d" % (hp,bmp1.GetWidth()/8,bmp1.GetHeight()/8)

	def OnClicked3(self,e):
		# self.two.Hide()
		self.p1=SuperMarket2(None)
		self.p1.Show()
# Functions

	def billingfun(self, e):
		sql="create table bill"+str(self.count)+"(pid int not null,pname varchar(20),price float,items int,amount float );"
		cursor=self.query(sql)
		
		print("hello")
		self.two.Hide()
		self.splitter = wx.SplitterWindow(
			self, -1, size=(self.width, self.height))
		# cart panel
		self.cart = wx.Panel(self.splitter, -1)
		self.cart.Hide()
		# hp2 = "hp2.jpg"
		# bmp2 = wx.Image(hp,wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
		# bitmap2=wx.StaticBitmap(self.two,-1,bmp2,(0,0),size=(self.width,self.height))
		# str2 = "%s %d%d" % (hp2,bmp2.GetWidth(),bmp2.GetHeight())
		self.cart.SetBackgroundColour('orange')
		# hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.cart1 = wx.StaticText(
			self.cart, label="Your Cart is Empty", pos=(370, 500), size=(20, 20))
		self.cart1.SetFont(self.font)
		self.bill9 = wx.Button(self.cart, label="Pay", pos=(700, 900))
		self.bill9.SetFont(self.font)
		self.bill9.Hide()
		# hbox1.Add(self.bill9, 2)
		# languages=[]
		# lst = wx.ListBox(self.cart, size = (100,300), choices = languages, style = wx.LB_SINGLE)
		# hbox1.Add(lst,1)
		# self.cart.SetSizer(hbox1)
		self.makebill()


# Billing

	def makebill(self):
		# billing panel
		# self.main2 = wx.GridBagSizer(10, 10)
		# width,height=wx.GetDefaultSize()
		self.billing = wx.Panel(
			self.splitter, -1, size=(self.width/2, self.height))
		self.billing.SetBackgroundColour('grey')
		# bill_id = wx.StaticText(self.billing, label=""+str(id))
		# self.main2.Add(bill_id, pos=(2, 10), flag=wx.ALL, border=5)
		self.bill1 = wx.StaticText(self.billing, label="Enter Product Id", pos=(20, 200), size=(20, 20))
		self.bill1.SetFont(self.font)
		self.bill2 = wx.TextCtrl(self.billing, -1, "",# Bil# Billing# Billingling
								 pos=(220, 200), size=(150, 40))
		self.bill2.SetFont(self.font)
		# self.main2.Add(self.bill1, pos=(8, 1), flag=wx.ALL, border=5)
		# self.main2.Add(self.bill2, pos=(8, 2), flag=wx.ALL, border=5)
		# self.forfs = wx.StaticText(self.billing, label=".")
		# self.main2.Add(self.forfs, pos=(self.width/2, self.height/2), flag=wx.ALL, border=5)
		self.bill8 = wx.Button(
			self.billing, label="Get Details", pos=(220, 250), size=(150, 35))
		self.bill8.SetFont(self.font)
		# self.main2.Add(self.bill8, pos=(9, 2), flag=wx.ALL, border=5)
		self.Bind(wx.EVT_BUTTON, self.okay2, id=self.bill8.GetId())
		# self.billing.SetSizer(self.main2)
		self.cart.Show()
		self.splitter.SplitVertically(self.billing, self.cart)

# when GetDetails is clicked
	def okay2(self, e):
		if self.bill2.GetValue() == "":
			wx.MessageBox("Enter a Product Id")
		else:
			sql="select * from products where pid=%s" %(self.bill2.GetValue())
			cursor = self.query(sql)
			self.x=cursor.fetchone()

			
			self.k=str(self.x[1])
			self.k1=str(self.x[2])
			self.bill8.Destroy()
			self.st4 = wx.StaticText(
				self.billing, label=self.bill2.GetValue(), pos=(250, 200), size=(150, 40))
			self.st4.SetFont(self.font)
			self.bill2.Destroy()
			# self.main2.Add(self.st4, pos=(8, 2), flag=wx.ALL, border=5)
			self.st5 = wx.StaticText(
				self.billing, label="Name", pos=(370, 150), size=(150, 40))
			self.st5.SetFont(self.font)
			self.tc5=wx.StaticText(self.billing,-1,label=self.k,pos=(370, 200), size=(150, 40))
			self.st6 = wx.StaticText(
				self.billing, label="Price", pos=(530, 150), size=(150, 40))
			self.st6.SetFont(self.font)
			self.tc6=wx.StaticText(self.billing,-1,label=self.k1,pos=(530, 200), size=(150, 40))
			self.bill3 = wx.StaticText(
				self.billing, label="No.of Items", pos=(20, 250), size=(150, 40))
			self.bill3.SetFont(self.font)
			self.bill4 = wx.TextCtrl(
				self.billing, -1, "", pos=(200, 250), size=(80, 40))
			self.bill4.SetFont(self.font)

			# update=wx.Button(self,label="update")
			# self.gbs.Add(update, pos = (8, 10), flag = wx.ALL, border = 1)
			# self.main2.Add(self.st5, pos=(7, 4), flag=wx.ALL, border=5)
			self.bill7 = wx.Button(
				self.billing, label="Add to Cart", pos=(200, 300), size=(150, 35))
			self.bill7.SetFont(self.font)
			self.bill6 = wx.Button(
				self.billing, label="Change Id", pos=(390, 300), size=(140, 35))
			self.bill6.SetFont(self.font)
			# self.main2.Add(self.st6, pos=(7, 6), flag=wx.ALL, border=5)
			# self.main2.Add(self.bill3, pos=(9, 1), flag=wx.ALL, border=5)
			# self.main2.Add(self.bill4, pos=(9, 2), flag=wx.ALL, border=5)
			# self.main2.Add(self.bill7, pos=(10, 2), flag=wx.ALL, border=5)
			# self.main2.Add(self.bill6, pos=(10, 3), flag=wx.ALL, border=5)
			self.Bind(wx.EVT_BUTTON, self.Changeid, id=self.bill6.GetId())
			self.Bind(wx.EVT_BUTTON, self.Addcart, id=self.bill7.GetId())
			# self.billing.SetSizer(self.main2)
	def connect(self):
			self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

	def Changeid(self, e):
		self.billing.Destroy()
		self.makebill()

	def Addcart(self, e):
		if self.bill4.GetValue() != '1' and self.bill4.GetValue() != '2' and self.bill4.GetValue() != '3' and self.bill4.GetValue() != '4' and self.bill4.GetValue() != '5' and self.bill4.GetValue() != '6' and self.bill4.GetValue() != '7' and self.bill4.GetValue() != '8' and self.bill4.GetValue() != '9':
			wx.MessageBox("Enter an Integer !")
			self.bill4.Value = ""
		else:
			z=self.x[2]*int(self.bill4.GetValue())
			sql="insert into bill"+str(self.count)+" values("+str(self.st4.GetLabel())+",'"+self.k+"','"+self.k1+"',"+str(self.bill4.GetValue())+",'"+str(z)+"')"
			cursor=self.query(sql)
			sql="update products set stock=stock-"+str(self.bill4.GetValue())+" where pid="+str(self.st4.GetLabel())
			cursor=self.query(sql)
			self.billing.Destroy()
			self.makebill()
	
			
			if self.count1>0:
				self.heading2.Destroy()
			if self.count1==0:
				self.cart1.Destroy()
			
				self.heading=wx.StaticText(self.cart,label="\t\tpname\t\t\t\tprice\t\titems\t\tamount")
				self.heading.SetFont(self.font)
			sql="select * from bill"+str(self.count)+";"
			x=cursor=self.query(sql)
			
			
			count2=1
			for i in x:
				z0=str(i[0])
				z1=str(i[1])
				z2=str(i[2])
				z3=str(i[3])
				z4=str(i[4])
				self.heading2=wx.StaticText(self.cart,label="\n\t\t"+z1+"\t\t\t"+z2+"\t\t"+z3+"\t\t\t"+z4,pos=(0,50*count2))
				count2=count2+1

				self.heading2.SetFont(self.font)

			sql="select sum(amount) from bill"+str(self.count)
			cursor=self.query(sql)
			x=cursor.fetchone()
			if self.count1>0:
				self.total.Destroy()
			self.total=wx.StaticText(self.cart,label=str(x[0]),pos=(700,70*count2))
			self.total.SetFont(self.font)
			self.count1=self.count1+1

			self.bill9.Show()
			self.Bind(wx.EVT_BUTTON, self.payment, id=self.bill9.GetId())

	def payment(self, e):
		self.billing.Destroy()
		self.cart.Destroy()
		self.pay = wx.Panel(self, size=(self.width, self.height))
		self.pay.SetBackgroundColour('yellow')
		self.pay1 = wx.StaticText(self.pay, label="Enter Cust Num", pos=(20, 200), size=(20, 20))
		self.pay1.SetFont(self.font)
		self.pay2 = wx.TextCtrl(self.pay, -1, "",pos=(220, 200), size=(180, 40))
		self.pay2.SetFont(self.font)
		self.pay3 = wx.Button(self.pay, label="Get Details", pos=(200, 250), size=(130, 35))
		self.pay3.SetFont(self.font)
		self.Bind(wx.EVT_BUTTON, self.customer, id=self.pay3.GetId())
		
	def customer(self,e):
		self.pay3.Destroy()
		sql="select * from customers where mnumber="+str(self.pay2.GetValue())
		cursor=self.query(sql)
		self.y=cursor.fetchone()
		print (self.y)
		
		sql="select * from customers"
		cursor=self.query(sql)
		self.a=cursor.fetchall()
		
		self.j=0
		for i in self.a:
			if str(self.pay2.GetValue())==str(i[2]):
				self.j=i
				
				break
			else:
				self.j=0
				
				
		length=len(str(self.pay2.GetValue()))
		self.id=self.pay2.GetValue()

		if self.pay2.GetValue() == "" or length!=10:
			self.pay4 = wx.StaticText(self.pay, label="Customer Not present", pos=(50, 250), size=(40, 20))
			self.pay4.SetFont(self.font)
			self.pay5 = wx.Button(self.pay, label="Sign Up", pos=(200, 290), size=(130, 35))
			self.pay5.SetFont(self.font)
		elif self.j==0:
			self.pay4 = wx.StaticText(self.pay, label="Customer Not present", pos=(50, 250), size=(40, 20))
			self.pay4.SetFont(self.font)
			self.pay5 = wx.Button(self.pay, label="Sign Up", pos=(200, 290), size=(130, 35))
			self.pay5.SetFont(self.font)
			self.Bind(wx.EVT_BUTTON,self.sign,id=self.pay5.GetId())
			
		else:
			self.k2=str(self.y[1])
			self.cus1 = wx.StaticText(self.pay, label=self.pay2.GetValue(), pos=(200, 200), size=(150, 40))
			self.cus1.SetFont(self.font)
			self.pay2.Destroy()
			self.cus2 = wx.StaticText(self.pay, label="Name", pos=(420, 150), size=(150, 40))
			self.cus2.SetFont(self.font)
			self.cus4 = wx.StaticText(self.pay, label=self.k2, pos=(420, 200), size=(150, 40))
			self.cus4.SetFont(self.font)
			self.cus3 = wx.Button(self.pay, label="Pay Now", pos=(200, 300), size=(120, 35))
			self.cus3.SetFont(self.font)
			self.Bind(wx.EVT_BUTTON,self.final,id=self.cus3.GetId())
	def sign(self,e):
		self.pay1.Destroy()
		self.pay2.Destroy()
		self.pay4.Destroy()
		self.pay5.Destroy()
		self.signup = wx.Panel(self, size=(self.width, self.height))
		self.sign1 = wx.StaticText(self.signup, label="Enter Cust Num", pos=(200, 200), size=(20, 20))
		self.sign1.SetFont(self.font)
		self.sign2 = wx.TextCtrl(self.signup, -1, "",pos=(380, 200), size=(180, 40))
		self.sign2.SetFont(self.font)
		self.sign3 = wx.StaticText(self.signup, label="Enter EmailId", pos=(200, 300), size=(20, 20))
		self.sign3.SetFont(self.font)
		self.sign4 = wx.TextCtrl(self.signup, -1, "",pos=(380, 300), size=(180, 40))
		self.sign4.SetFont(self.font)
		self.sign5 = wx.StaticText(self.signup, label="Enter Address", pos=(200, 400), size=(20, 20))
		self.sign5.SetFont(self.font)
		self.sign6 = wx.TextCtrl(self.signup, -1, "",pos=(380, 400), size=(180, 40))
		self.sign6.SetFont(self.font)
		self.sign7 = wx.Button(self.signup, label="Add and Generate", pos=(250, 500),size=(220,35))
		self.Bind(wx.EVT_BUTTON,self.final2,id=self.sign7.GetId())

	def final2(self,e):
		
		
		sql="insert into clogin values('"+str(self.sign2.GetValue())+"','"+str(self.id)+"')"
		cursor=self.query(sql)
		sql="insert into customers(mnumber,cname,email,address,lid) values("+str(self.id)+",'"+str(self.sign2.GetValue())+"','"+str(self.sign4.GetValue())+"','"+str(self.sign6.GetValue())+"','"+str(self.sign2.GetValue())+"')"
		cursor=self.query(sql)
		
		sql="update customers set bill="+str(self.count)+" where mnumber="+str(self.id)+";"
		cursor=self.query(sql)
		self.count=self.count+1;
		self.signup.Destroy()
		self.thank = wx.StaticText(self.pay, label="Payment is Done", pos=(700, 200), size=(200, 200))
		self.thank.SetFont(self.font)
		self.pay4 = wx.Button(self.pay, label="Back to Homepage", pos=(1500, 900),size=(220,35))
		self.Bind(wx.EVT_BUTTON,self.back,id=self.pay4.GetId())
		self.pay4.SetFont(self.font)
		
	def final(self,e):
		sql="update customers set bill="+str(self.count)+" where mnumber="+str(self.id)+";"
		cursor=self.query(sql)
		self.count=self.count+1;
		self.pay1.Destroy()
		self.cus1.Destroy()
		self.cus2.Destroy()
		self.cus3.Destroy()
		self.cus4.Destroy()
		self.thank = wx.StaticText(self.pay, label="Payment is Done", pos=(700, 200), size=(200, 200))
		self.thank.SetFont(self.font)
		self.pay4 = wx.Button(self.pay, label="Back to Homepage", pos=(1500, 900),size=(220,35))
		self.Bind(wx.EVT_BUTTON,self.back,id=self.pay4.GetId())
		self.pay4.SetFont(self.font)
		# msg = "Hello Bro!"
		# to = "+919121931106"
		# send_sms(msg, to)
			
	def back(self,e):
		self.pay.Destroy()
		self.count1=0
		self.two.Show()

	def Onclicked(self, e):
		self.two.Hide()
		if self.table.IsShown():
			self.two.Show()
			self.table.Hide()
		else:
			self.table.Show()
			self.billing.Hide()
			self.cart.Hide()


		

	def OnQuit(self,e):
		self.Close()

	def ToggleToolBar(self,e):
		if self.shtl.IsChecked():
			self.toolbar.Show()
		else:
			self.toolbar.Hide()

	def ToggleStatusBar(self,e):
		if self.shst.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()



class TabPanel(wx.Panel):
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		#self.SetBackgroundColour("yellow")
		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(13)
		self.gbs=wx.GridBagSizer(5,5)

		attributes = ['pid', 'pname', 'MRP','stock','Did']
		st=wx.StaticText(self,label="search by")
		self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
		self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
		btn1=wx.Button(self,label="search")
		st.SetFont(font)
		self.gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
		self.gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
		self.gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
		self.gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
		self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

		# execute SQL query using execute() method.
		sql="select * from products"
		cursor = self.query(sql)
		records = cursor.fetchall()
		width,height=wx.GetDisplaySize()
		self.list = wx.ListCtrl(self, -1, size=(-1,300),style = wx.LC_REPORT)
		self.list.InsertColumn(0, 'p_ID',wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(1, 'p_Name', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(2, 'MRP', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(3, 'stock', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(4, 'd_ID', wx.LIST_FORMAT_CENTER, width/5-27)
		for i in records:
		   k1=str(i[0])
		   k2=str(i[1])
		   k3=str(i[2])
		   k4=str(i[3])
		   k5=str(i[4])
		   index = self.list.InsertStringItem(sys.maxint,k1)
		   self.list.SetStringItem(index, 1, k2)
		   self.list.SetStringItem(index, 2, k3)
		   self.list.SetStringItem(index, 3, k4)
		   self.list.SetStringItem(index, 4, k5)
		self.gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

		btn2=wx.Button(self,label="back",size=(80,40))
		self.gbs.Add(btn2, pos = (24, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)
		# self.Bind(wx.EVT_BUTTON,self.OnClicked4, id = btn2.GetId())

		btn3=wx.Button(self,label="update",size=(80,40))
		self.gbs.Add(btn3, pos = (24, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
		self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

		self.SetSizerAndFit(self.gbs)

	# def OnClicked4(self,e):
	# 	self.notebook.Destroy()
	# 	self.p2=SuperMarket(None)
	# 	self.p2.Show()
	def search(self,e):
    		searchby=self.combo.GetValue()
		value=self.searchControl.GetValue()
		sql="select * from products where %s='%s'" %(searchby,value)
		cursor = self.query(sql)
		x=cursor.fetchall()
		if not x:
			print "nulll"
		else:
			print x[0]
			width,height=wx.GetDisplaySize()
			self.list = wx.ListCtrl(self, -1, size=(-1,100),style = wx.LC_REPORT)
			self.list.InsertColumn(0, 'pid',wx.LIST_FORMAT_CENTER, width/5-27)
			self.list.InsertColumn(1, 'pname', wx.LIST_FORMAT_CENTER, width/5-27)
			self.list.InsertColumn(2, 'MRP', wx.LIST_FORMAT_CENTER, width/5-27)
			self.list.InsertColumn(1, 'stock', wx.LIST_FORMAT_CENTER, width/5-27)
			self.list.InsertColumn(2, 'Did', wx.LIST_FORMAT_CENTER, width/5-27)
			for i in x:
				l1=str(i[0])
				l2=str(i[1])
				l3=str(i[2])
				l4=str(i[3])
				l5=str(i[4])
				index = self.list.InsertStringItem(sys.maxint,l1)
				self.list.SetStringItem(index, 1, l2)
				self.list.SetStringItem(index, 2, l3)
				self.list.SetStringItem(index, 3, l4)
				self.list.SetStringItem(index, 4, l5)
			self.gbs.Add(self.list, pos = (18,0),span=(5,14),flag = wx.ALL, border = 5)

			self.SetSizerAndFit(self.gbs)



	def update(self,e):
		Update(self,"update")

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

class Update(wx.Frame):
	def __init__(self, parent,title):
		super(Update,self).__init__(parent,title=title)

		self.Maximize()

		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(17)
		self.gbs=wx.GridBagSizer(5,5)

		self.st1= wx.StaticText(self,label = "PRODUCTS" ,style = wx.ALIGN_CENTRE)
		self.st1.SetFont(font)
		self.st2= wx.StaticText(self,label = "p_ID:" )
		self.st2.SetFont(font)
		self.tc2=wx.TextCtrl(self,-1,"")
		self.btn1=wx.Button(self,label="OK")
		self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

		self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
		self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
		self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
		self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

		self.SetSizerAndFit(self.gbs)
		self.Centre()
		self.Show()


	def okay(self,e):
		if self.tc2.GetValue() == "" :
			wx.MessageBox("p_ID field is Empty!")
		else:
			font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
			font.SetPointSize(17)
			sql="select * from products where pid=%s" %(self.tc2.GetValue())
			cursor = self.query(sql)
			x=cursor.fetchone()
			st3=wx.StaticText(self,label="p_Name:")
			st3.SetFont(font)
			self.tc3=wx.TextCtrl(self,-1,str(x[1]))
			st4=wx.StaticText(self,label="MRP:")
			st4.SetFont(font)
			self.tc4=wx.TextCtrl(self,-1,str(x[2]))
			st5=wx.StaticText(self,label="stock:")
			st5.SetFont(font)
			self.tc5=wx.TextCtrl(self,-1,str(x[3]))
			st6=wx.StaticText(self,label="d_ID:")
			st6.SetFont(font)
			self.tc6=wx.TextCtrl(self,-1,str(x[4]))
			update=wx.Button(self,label="update")
			self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
			self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st5, pos = (11,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc5, pos = (11, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st6, pos = (12,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc6, pos = (12, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(update, pos = (14,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

			self.SetSizerAndFit(self.gbs)
			self.Bind(wx.EVT_BUTTON, self.update, update)

	def update(self,e):
		sql="update products set pname='%s',MRP=%s, stock=%s, Did=%s where pid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc5.GetValue(),self.tc6.GetValue(),self.tc2.GetValue())
		cur = self.query(sql)
		SuperMarket(None)

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

	
class TabPanel2(wx.Panel):
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		#self.SetBackgroundColour("yellow")
		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(13)
		gbs=wx.GridBagSizer(5,5)

		attributes = ['c_ID', 'c_Name', 'phNo','Bill']
		st=wx.StaticText(self,label="search by")
		self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
		self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
		btn1=wx.Button(self,label="search")
		st.SetFont(font)
		gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
		gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
		gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
		gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
		self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

		# execute SQL query using execute() method.
		sql="select * from customers"
		cursor = self.query(sql)
		records = cursor.fetchall()
		width,height=wx.GetDisplaySize()
		self.list = wx.ListCtrl(self, -1, size=(-1,400),style = wx.LC_REPORT)
		self.list.InsertColumn(0, 'c_ID',wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(1, 'c_Name', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(2, 'phNo', wx.LIST_FORMAT_CENTER, width/4-20)
		self.list.InsertColumn(3, 'Bill', wx.LIST_FORMAT_CENTER, width/4-20)
		for i in records:
		   k1=str(i[0])
		   k2=str(i[1])
		   k3=str(i[2])
		   k4=str(i[6])
		   index = self.list.InsertStringItem(sys.maxint,k1)
		   self.list.SetStringItem(index, 1, k2)
		   self.list.SetStringItem(index, 2, k3)
		   self.list.SetStringItem(index, 3, k4)
		   
		  
		gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

		btn2=wx.Button(self,label="back",size=(80,40))
		gbs.Add(btn2, pos = (11, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

		btn3=wx.Button(self,label="update",size=(80,40))
		gbs.Add(btn3, pos = (11, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5) 
		self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

		self.SetSizerAndFit(gbs)

	def search(self,e):
		searchby=self.combo.GetValue()
		value=self.searchControl.GetValue()
		sql="select * from customers where %s='%s'" %(searchby,value)
		cursor = self.query(sql)
		x=cursor.fetchone()
		print (x)

	def update(self,e):
		Update2(self,"update")

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

class Update2(wx.Frame):
	def __init__(self, parent,title):
		super(Update2,self).__init__(parent,title=title)

		self.Maximize()

		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(17)
		self.gbs=wx.GridBagSizer(5,5)

		self.st1= wx.StaticText(self,label = "CUSTOMERS" ,style = wx.ALIGN_CENTRE)
		self.st1.SetFont(font)
		self.st2= wx.StaticText(self,label = "c_ID:" )
		self.st2.SetFont(font)
		self.tc2=wx.TextCtrl(self,-1,"")
		self.btn1=wx.Button(self,label="OK")
		self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

		self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
		self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
		self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
		self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

		self.SetSizerAndFit(self.gbs)
		self.Centre()
		self.Show()


	def okay(self,e):
		if self.tc2.GetValue() == "" :
			wx.MessageBox("c_ID field is Empty!")
		else:
			font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
			font.SetPointSize(17)
			sql="select * from customers where cid=%s" %(self.tc2.GetValue())
			cursor = self.query(sql)
			x=cursor.fetchone()
			st3=wx.StaticText(self,label="c_Name:")
			st3.SetFont(font)
			self.tc3=wx.TextCtrl(self,-1,str(x[1]))
			st4=wx.StaticText(self,label="phNo:")
			st4.SetFont(font)
			self.tc4=wx.TextCtrl(self,-1,str(x[2]))
			
			update=wx.Button(self,label="update")
			self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
			self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			
			self.gbs.Add(update, pos = (12,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

			self.SetSizerAndFit(self.gbs)
			self.Bind(wx.EVT_BUTTON, self.update, update)

	def update(self,e):
		sql="update customers set cname='%s',mnumber=%s where cid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc2.GetValue())
		cur = self.query(sql)
		SuperMarket(None)

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

class TabPanel3(wx.Panel):
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		#self.SetBackgroundColour("yellow")
		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(13)
		gbs=wx.GridBagSizer(5,5)

		attributes = ['b_ID', 'm_number', 'c_ID','p_date','amount']
		st=wx.StaticText(self,label="search by")
		self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
		self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
		btn1=wx.Button(self,label="search")
		st.SetFont(font)
		gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
		gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
		gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
		gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
		self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

		# execute SQL query using execute() method.
		sql="select * from payment"
		cursor = self.query(sql)
		records = cursor.fetchall()
		width,height=wx.GetDisplaySize()
		self.list = wx.ListCtrl(self, -1, size=(-1,400),style = wx.LC_REPORT)
		self.list.InsertColumn(0, 'b_ID',wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(1, 'm_number', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(2, 'c_ID', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(3, 'p_date', wx.LIST_FORMAT_CENTER, width/5-27)
		self.list.InsertColumn(4, 'amount', wx.LIST_FORMAT_CENTER, width/5-27)
		for i in records:
		   k1=str(i[0])
		   k2=str(i[1])
		   k3=str(i[2])
		   k4=str(i[3])
		   k5=str(i[4])
		   index = self.list.InsertStringItem(sys.maxint,k1)
		   self.list.SetStringItem(index, 1, k2)
		   self.list.SetStringItem(index, 2, k3)
		   self.list.SetStringItem(index, 3, k4)
		   self.list.SetStringItem(index, 4, k5)
		gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

		btn2=wx.Button(self,label="back",size=(80,40))
		gbs.Add(btn2, pos = (11, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

		btn3=wx.Button(self,label="update",size=(80,40))
		gbs.Add(btn3, pos = (11, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
		self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

		self.SetSizerAndFit(gbs)

	def search(self,e):
		searchby=self.combo.GetValue()
		value=self.searchControl.GetValue()
		sql="select * from payment where %s='%s'" %(searchby,value)
		cursor = self.query(sql)
		x=cursor.fetchone()
		print (x)

	def update(self,e):
		Update3(self,"update")

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor

class Update3(wx.Frame):
	def __init__(self, parent,title):
		super(Update3,self).__init__(parent,title=title)

		self.Maximize()

		font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(17)
		self.gbs=wx.GridBagSizer(5,5)

		self.st1= wx.StaticText(self,label = "PAYMENTS" ,style = wx.ALIGN_CENTRE)
		self.st1.SetFont(font)
		self.st2= wx.StaticText(self,label = "b_ID:" )
		self.st2.SetFont(font)
		self.tc2=wx.TextCtrl(self,-1,"")
		self.btn1=wx.Button(self,label="OK")
		self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

		self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
		self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
		self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
		self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

		self.SetSizerAndFit(self.gbs)
		self.Centre()
		self.Show()


	def okay(self,e):
		if self.tc2.GetValue() == "" :
			wx.MessageBox("b_ID field is Empty!")
		else:
			font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
			font.SetPointSize(17)
			sql="select * from payment where bid=%s" %(self.tc2.GetValue())
			cursor = self.query(sql)
			x=cursor.fetchone()
			st3=wx.StaticText(self,label="m_number:")
			st3.SetFont(font)
			self.tc3=wx.TextCtrl(self,-1,str(x[1]))
			st4=wx.StaticText(self,label="c_ID:")
			st4.SetFont(font)
			self.tc4=wx.TextCtrl(self,-1,str(x[2]))
			st5=wx.StaticText(self,label="p_date:")
			st5.SetFont(font)
			self.tc5=wx.TextCtrl(self,-1,str(x[3]))
			st6=wx.StaticText(self,label="amount:")
			st6.SetFont(font)
			self.tc6=wx.TextCtrl(self,-1,str(x[4]))
			update=wx.Button(self,label="update")
			self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
			self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st5, pos = (11,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc5, pos = (11, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(st6, pos = (12,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
			self.gbs.Add(self.tc6, pos = (12, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
			self.gbs.Add(update, pos = (14,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

			self.SetSizerAndFit(self.gbs)
			self.Bind(wx.EVT_BUTTON, self.update, update)

	def update(self,e):
		sql="update payment set mnumber=%s,cid=%s,pdate=%s,amount=%s where bid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc5.GetValue(),self.tc2.GetValue())
		cur = self.query(sql)
		SuperMarket(None)

	def connect(self):
		self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

	def query(self, sql):
		try:
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		except (AttributeError, MySQLdb.OperationalError):
		  self.connect()
		  cursor = self.conn.cursor()
		  cursor.execute(sql)
		  self.conn.commit()
		return cursor


db.close()



app=wx.App()

p=Mainwindow(None)
p.Show()
s=LoginDialog3()
s.Show()
#frame = DemoFrame()
app.MainLoop()


# def main():


# if __name__ == '__main__':
	# main()


#from twilio.rest import TwilioRestClient


#----------------------------------------------------------------------


# if __name__ == "__main__":
#     msg = "Hello pine..!!"
#     to = "+919121931106"
#     send_sms(msg, to)