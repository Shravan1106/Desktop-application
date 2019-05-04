import wx
import random
import MySQLdb
#import ol_3
count=100
db=MySQLdb.connect("localhost","shravan","shravan","supermarket")
cursor=db.cursor()


class LoginDialog1(wx.Dialog):
   
	def __init__(self):
		
		wx.Dialog.__init__(self, None, title="User Login",size=(100,100))
		self.logged_in = False
		wx.Maximize()
		user_sizer = wx.BoxSizer(wx.VERTICAL)

		user_lbl = wx.StaticText(self, label="Username:")
		user_sizer.Add(user_lbl, 0,flag= wx.ALL | wx.ALIGN_CENTER,border= 5)
		self.user = wx.TextCtrl(self)
		user_sizer.Add(self.user, 0,flag= wx.ALL |wx.ALIGN_CENTER, border=5)

	   
		p_sizer = wx.BoxSizer(wx.HORIZONTAL)

		p_lbl = wx.StaticText(self, label="Password:")
		p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
		self.password = wx.TextCtrl(
			self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
		self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
		p_sizer.Add(self.password, 0, wx.ALL, 5)

		main_sizer = wx.BoxSizer(wx.VERTICAL)
		main_sizer.Add(user_sizer, 0, wx.ALL, 5)
		main_sizer.Add(p_sizer, 0, wx.ALL, 5)

		btn = wx.Button(self, label="Login")
		btn.Bind(wx.EVT_BUTTON, self.onLogin)
		main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

		self.SetSizer(main_sizer)

	# ----------------------------------------------------------------------
	def onLogin(self, event):
		"""
		Check credentials and login
		"""
		user_name=self.user.GetValue()
		sql=("select password from user where user='"+user_name+"';")
		cursor.execute(sql)
		x=cursor.fetchone()
		print x;
		user_password = self.password.GetValue()
		if user_password == x :
			print("You are now logged in!")
			self.logged_in = True
			self.Close()
		else:
			wx.MessageBox('Username or password is incorrect!',
						  'Enter Again', wx.OK | wx.ICON_INFORMATION)
			print("Username or password is incorrect!")
 

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
		cursor.execute(sql)
		x=cursor.fetchall()
		print x
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
		dlg = LoginDialog1()
		dlg.ShowModal()
		authenticated = dlg.logged_in
		if not authenticated:
			self.Close()

	def OnClicked2(self,e):
		dlg = LoginDialog2()
		dlg.ShowModal()
		authenticated = dlg.logged_in
		
		if authenticated:
			p = SuperMarket(None)
			p.Show()

		
		



class SuperMarket(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(SuperMarket, self).__init__(*args, **kwargs)
		self.Mbar()

	def Mbar(self):

		self.width, self.height = wx.GetDisplaySize()
		menubar = wx.MenuBar()

		# File Menu
		fileMenu = wx.Menu()
		fileMenu.Append(wx.ID_NEW, '&New')
		fileMenu.Append(wx.ID_OPEN, '&Open')
		fileMenu.Append(wx.ID_SAVE, '&Save')
		fileMenu.AppendSeparator()

		imp = wx.Menu()
		imp.Append(wx.ID_ANY, 'Import files')
		imp.Append(wx.ID_ANY, 'Import images')
		imp.Append(wx.ID_ANY, 'Import audio or video')

		fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
		fileItem = fileMenu.Append(wx.ID_EXIT, '&Quit')

		self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

		# Edit Menu
		editMenu = wx.Menu()
		editMenu.Append(wx.ID_COPY, '&Copy')
		editMenu.Append(wx.ID_CUT, '&Cut')
		editMenu.Append(wx.ID_PASTE, '&Paste')
		editMenu.AppendSeparator()
		editMenu.Append(wx.ID_SELECTALL, 'Select All')
		editMenu.Append(wx.ID_PREFERENCES, 'Preferences')

		# view menu
		viewMenu = wx.Menu()
		self.shtl = viewMenu.Append(
			wx.ID_ANY, 'Show ToolBar', kind=wx.ITEM_CHECK)
		self.shst = viewMenu.Append(
			wx.ID_ANY, 'Show StatusBar', kind=wx.ITEM_CHECK)

		viewMenu.Check(self.shtl.GetId(), True)
		viewMenu.Check(self.shst.GetId(), True)

		self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)
		self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)

		self.toolbar = self.CreateToolBar()
		self.toolbar.Realize()

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('Ready')

		# table Menu
		tableMenu = wx.Menu()
		tableItem = tableMenu.Append(wx.ID_ANY, '&show')

		self.Bind(wx.EVT_MENU, self.Onclicked, id=tableItem.GetId())

		menubar.Append(fileMenu, '&File')
		menubar.Append(editMenu, '&Edit')
		menubar.Append(viewMenu, '&View')
		menubar.Append(tableMenu, '&Tables')

		self.SetMenuBar(menubar)

		self.SetSize((500, 500))
		self.SetTitle('Super Market')
		self.Center()
		self.Maximize()

		# HomePage
		self.two = wx.Panel(self, size=(self.width, self.height))
		self.two.SetBackgroundColour('grey')
		main1 = wx.GridBagSizer(10, 10)
		bill = wx.Button(self.two, label="Billing")
		info = wx.Button(self.two, label="Info")
		main1.Add(bill, pos=(30, 80), flag=wx.ALL, border=5)
		main1.Add(info, pos=(30, 40), flag=wx.ALL, border=5)
		self.two.SetSizer(main1)
		self.Bind(wx.EVT_BUTTON, self.billingfun, id=bill.GetId())
		#self.Bind(wx.EVT_BUTTON, self., id=info.GetId())

		# Tables
		# width, height = wx.GetDisplaySize()
		self.table = wx.Panel(self, size=(self.width, self.height))
		self.table.Hide()
		notebook = wx.Notebook(self.table)
		tabOne = TabPanel(notebook)
		notebook.AddPage(tabOne, "Table 1")
		tabTwo = TabPanel2(notebook)
		notebook.AddPage(tabTwo, "Table 2")
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
		self.table.SetSizer(sizer)

		# Font
		self.font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(15)

		self.two.Show()
		self.Layout()

# Functions

	def billingfun(self, e):
		sql="create table bill"+str(count)+"(pid int not null,pname varchar(20),price float,items int,amount float );"
		cursor=self.query(sql)
		
		print("hello")
		self.two.Hide()
		self.splitter = wx.SplitterWindow(
			self, -1, size=(self.width, self.height))
		# cart panel
		self.cart = wx.Panel(self.splitter, -1)
		self.cart.Hide()
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
			sql="insert into bill"+str(count)+" values("+str(self.st4.GetLabel())+",'"+self.k+"','"+self.k1+"',"+str(self.bill4.GetValue())+",'"+str(z)+"')"
			cursor=self.query(sql)
			self.billing.Destroy()
			self.makebill()
			self.cart1.Destroy()
			self.bill9.Show()
			self.Bind(wx.EVT_BUTTON, self.payment, id=self.bill9.GetId())

	def payment(self, e):
		self.billing.Destroy()
		self.cart.Destroy()
		self.pay = wx.Panel(self, size=(self.width, self.height))
		self.pay.SetBackgroundColour('yellow')
		self.pay1 = wx.StaticText(self.pay, label="Enter Cust Num", pos=(20, 200), size=(20, 20))
		self.pay1.SetFont(self.font)
		self.pay2 = wx.TextCtrl(self.pay, -1, "",pos=(200, 200), size=(150, 40))
		self.pay2.SetFont(self.font)
		self.pay3 = wx.Button(self.pay, label="Get Details", pos=(200, 250), size=(130, 35))
		self.pay3.SetFont(self.font)
		self.Bind(wx.EVT_BUTTON, self.customer, id=self.pay3.GetId())
		
	def customer(self,e):
		self.pay3.Destroy()
		sql="select * from customers where mnumber="+str(self.pay2.GetValue())
		cursor=self.query(sql)
		self.y=cursor.fetchone()
		print self.y
		
		sql="select mnumber from customers"
		cursor=self.query(sql)
		self.a=cursor.fetchall()
		for i in self.a:
			if(i==self.a):
				self.j=i
				break
			else:
				self.j=0
		length=len(str(self.pay2.GetValue()))
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
		else:
			self.k2=str(self.y[1])
			self.cus1 = wx.StaticText(self.pay, label=self.pay2.GetValue(), pos=(200, 200), size=(150, 40))
			self.cus1.SetFont(self.font)
			self.pay2.Destroy()
			self.cus2 = wx.StaticText(self.pay, label="Name", pos=(320, 150), size=(150, 40))
			self.cus2.SetFont(self.font)
			self.cus4 = wx.StaticText(self.pay, label=self.k2, pos=(320, 200), size=(150, 40))
			self.cus4.SetFont(self.font)
			self.cus3 = wx.Button(self.pay, label="Pay Now", pos=(200, 300), size=(120, 35))
			self.cus3.SetFont(self.font)
			self.Bind(wx.EVT_BUTTON,self.final,id=self.cus3.GetId())

	def final(self,e):
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
		
	def back(self,e):
		self.pay.Destroy()
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

	def OnQuit(self, e):
		self.Close()

	def ToggleToolBar(self, e):
		if self.shtl.IsChecked():
			self.toolbar.Show()
		else:
			self.toolbar.Hide()

	def ToggleStatusBar(self, e):
		if self.shst.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()


class TabPanel(wx.Panel):
	# ----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		self.SetBackgroundColour(random.choice(colors))

		btn = wx.Button(self, label="insert")
		btn2 = wx.Button(self, label="delete")
		btn3 = wx.Button(self, label="update")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(btn, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		sizer.Add(btn2, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		sizer.Add(btn3, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		self.SetSizer(sizer)


class TabPanel2(wx.Panel):
	# ----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		self.SetBackgroundColour(random.choice(colors))

		btn = wx.Button(self, label="insert")
		btn2 = wx.Button(self, label="delete")
		btn3 = wx.Button(self, label="update")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(btn, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		sizer.Add(btn2, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		sizer.Add(btn3, 0, wx.ALIGN_LEFT | wx.ALL, 10)
		self.SetSizer(sizer)





def main():
	app = wx.App()
	x=Mainwindow(None)
	x.Show()
	
	# frame = DemoFrame()
	app.MainLoop()


if __name__ == '__main__':
	main()
