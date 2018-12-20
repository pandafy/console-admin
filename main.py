
from util_me import *
from ObjectListView import ObjectListView, ColumnDefn
from faculty_manager import *
from datetime import date

	   	



class windowClass(wx.Frame):
	def __init__(self,*args,**kwargs):
		super(windowClass,self).__init__(*args,**kwargs)
		self.SetTitle('Administrator Console')
		self.Show(True)
		self.SetSize((400,400))
		self.basicGUI()

	def basicGUI(self):
		


		

		menuBar = wx.MenuBar()
		
		fileButton = wx.Menu()
		editButton = wx.Menu()
		addButon = wx.Menu()
		toolsButton = wx.Menu()

		#File menu dropdown
		exitItem = fileButton.Append(wx.ID_EXIT,'Exit','Select to exit program')


		#Add menu dropdown
		addNotice = addButon.Append(wx.ID_ADD,'Notice','Select to add notice.')
		addFaculty = addButon.Append(wx.ID_ADD,'Faculty','Add a new faculty member')

		#Tools menu dropdown
		stageItem = toolsButton.Append(81,'Stage','Click to stage changes')
		self.Bind(wx.EVT_MENU,self.stage,stageItem)


		menuBar.Append(fileButton,'File')
		menuBar.Append(editButton,'Edit')
		menuBar.Append(addButon,'Add')
		menuBar.Append(toolsButton,'Tools')


		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU,self.Quit,exitItem)
		self.Bind(wx.EVT_MENU,self.addNotices,addNotice)

		panel = wx.Panel(self)

		#Notice Management Buttons
		noticeButtonAdd = wx.Button(panel,-1,'Add Notice')
		self.Bind(wx.EVT_BUTTON,self.addNotices,noticeButtonAdd)
		noticeButtonEdit = wx.Button(panel,-1,'Edit Notices')
		self.Bind(wx.EVT_BUTTON,self.viewNotice,noticeButtonEdit)

		#Faculty Management Buttons
		facultyAddBtn = wx.Button(panel,-1,'Add Faculty')
		self.Bind(wx.EVT_BUTTON,self.addFaculty,facultyAddBtn)
		facultyEditBtn = wx.Button(panel,-1,'Edit Info')
		self.Bind(wx.EVT_BUTTON,self.viewFaculty,facultyEditBtn)


		#Utility tool Buttons
		stageButton = wx.Button(panel,-1,'Stage')
		self.Bind(wx.EVT_BUTTON,self.stage,stageButton)








		vbox = wx.BoxSizer(wx.VERTICAL)
		Notice = wx.StaticBox(panel, -1, 'Manage Notices:') 
		NoticeSizer = wx.StaticBoxSizer(Notice, wx.VERTICAL)
		NoticeBox = wx.BoxSizer(wx.HORIZONTAL)

		Faculty = wx.StaticBox(panel,-1, 'Manage Faculty Information')
		FacultySizer = wx.StaticBoxSizer(Faculty,wx.HORIZONTAL)
		FacultyBox = wx.BoxSizer(wx.HORIZONTAL)

		panel.SetSizer(vbox)

		vbox.Add(NoticeSizer,0,wx.ALL|wx.CENTER|wx.EXPAND,20)
		vbox.Add(FacultySizer,0,wx.ALL|wx.CENTER|wx.EXPAND,20)

		NoticeSizer.Add(NoticeBox,0,wx.ALL,5)
		NoticeBox.Add(noticeButtonAdd, 2, wx.ALL,border = 5)
		NoticeBox.Add(noticeButtonEdit, 2, wx.ALL,border = 5)
		
		FacultySizer.Add(FacultyBox,0,wx.CENTER|wx.ALL,5)
		FacultyBox.Add(facultyAddBtn,2,wx.ALL,border=5)
		FacultyBox.Add(facultyEditBtn,2,wx.ALL,border=5)
		



		
		
		#hbox.AddSpacer(5,0,0)

		vbox.Add(stageButton, 0, wx.ALL,border = 5)


	

	def addNotices(self,e):
		print "Inside ADD NOTICE"
		notice = NoticeClass(None,title = 'Notice Manager')
		notice.basicGUI()
		notice.ShowModal()
		notice.add()
		notice.Destroy()	

	def viewNotice(self,e) :
		print "View existing notices."	
		Notice = viewNoticeClass(None,title = 'Notice Editor')
		Notice.ShowModal()
		Notice.Destroy()


	def addFaculty(self,e):
		print 'Adding new faculty'
		Faculty = addFacultyClass(None)
		Faculty.basicGUI()
		Faculty.add()
		Faculty.ShowModal()
		Faculty.Destroy()
	def viewFaculty(self,e):
		print 'View existing faculty'
		Faculty = viewFacultyClass(None,title="Edit Faculty")
		Faculty.ShowModal()
		Faculty.Destroy()


	def stage(slef,e):
		print "Yo"

	def Quit(self, e):
		self.Close()



class NoticeClass(wx.Dialog):
	def __init__(self,*args,**kwargs):
		super(NoticeClass,self).__init__(*args,**kwargs)
		self.SetTitle('Notice Manager')
		self.SetSize((720,720))
		self.PhotoMaxSize = 640
		self.panel = wx.Panel(self)

	def basicGUI(self):
		
		

		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)


		img = wx.EmptyImage(640,480)
		self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,wx.BitmapFromImage(img))
		self.photoTxt = wx.TextCtrl(self.panel, size=(400,-1))
		noticeBrowseButton = wx.Button(self.panel,-1,'File...')
		self.Bind(wx.EVT_BUTTON,self.browseFile,noticeBrowseButton)
		lblList = ['Examination', 'Scholarship', 'Sports']     
		self.rbox = wx.RadioBox(self.panel,label = 'Category', choices = lblList ,majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
		self.TitleTxt = wx.TextCtrl(self.panel, size=(640,-1),value = "Enter notice description here.")
		self.NoticeBtn = wx.Button(self.panel,-1,'Add')
		self.Bind(wx.EVT_BUTTON,self.adNotice,self.NoticeBtn)
		self.DateTxt = wx.TextCtrl(self.panel,-1,size = (150,-1))
		self.DateLbl = wx.StaticText(self.panel,-1,'Date : ') 


		vbox.Add(hbox,0,wx.ALL|wx.ALIGN_CENTER)
		vbox.AddSpacer(5)
		vbox.Add(self.imageCtrl,0,wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL,5)
		vbox.AddSpacer(5)
		vbox.Add(hbox1,0,wx.ALIGN_CENTER,5)
		vbox.AddSpacer(5)
		vbox.Add(self.TitleTxt,0,wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL,5)
		vbox.AddSpacer(5)
		vbox.Add(self.NoticeBtn,0,wx.ALIGN_CENTER,5)

		hbox.AddSpacer(5)
		hbox.Add(wx.StaticText(self.panel,-1,"Select notice file : ",style=wx.ALIGN_CENTER), 0)
		hbox.Add(self.photoTxt, 5, wx.ALL, 5)	
		hbox.Add(noticeBrowseButton, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER,5)
		hbox.AddSpacer(5,0,0)

		hbox1.Add(self.DateLbl,0,wx.ALIGN_CENTER|wx.ALL,5)
		hbox1.Add(self.DateTxt,7,wx.ALIGN_CENTER | wx.ALL,5)
		hbox1.AddSpacer(30)
		hbox1.Add(self.rbox,0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER,5)

		self.panel.SetSizer(vbox)


	def browseFile(self,e):
		print "Browsing files"
		wildcard = "All files (*.*)|*.*|Image Files |*.png;*.jpg;*.jpeg|PDF Files (*.pdf)|*.pdf"
		fileDialog = wx.FileDialog(self, "Open XYZ file", wildcard=wildcard,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
 		if fileDialog.ShowModal() == wx.ID_CANCEL:
 			return
 		self.photoTxt.SetValue(fileDialog.GetPath())
 		self.onView(fileDialog.GetPath())


	def onView(self,path):
		print "reached here"
		img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		W = img.GetWidth()
		H = img.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = img.Scale(NewW,NewH)
		self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))

	def add(self):
		self.Bind(wx.EVT_BUTTON,self.adNotice,self.NoticeBtn)
		self.Date = str(date.today)
		self.DateTxt.SetValue(self.Date)

	def update(self,data):
		self.SetTitle("Edit Notice")
		self.NoticeBtn.SetLabel("EDIT")
		self.Bind(wx.EVT_BUTTON,self.editNotice,self.NoticeBtn)
		self.NPath = data["path"]
		self.NDate = data["date"]
		self.NDesc = data["description"]
		self.NCatg = ['Examination', 'Scholarship', 'Sports'].index(data["category"])
		self.id    = data["id"]

		self.onView(self.NPath)

		self.photoTxt.SetValue(self.NPath)
		self.TitleTxt.SetValue(self.NDesc)
		self.rbox.SetSelection(self.NCatg)
		self.DateTxt.SetValue(self.NDate)


	def adNotice(self,e):
		title = self.TitleTxt.GetValue()
		path = self.photoTxt.GetValue()
		category = self.rbox.GetString(self.rbox.GetSelection())
		date = self.DateTxt.GetValue()

		appendNotices(date,title,path,category)
		self.Destroy()

	def editNotice(self,e):
		title = self.TitleTxt.GetValue()
		path = self.photoTxt.GetValue()
		category = self.rbox.GetString(self.rbox.GetSelection())
		date = self.DateTxt.GetValue()
		EditNotices(self.id,date,title,path,category)
		self.Destroy()

class viewNoticeClass(wx.Dialog):
	def __init__(self,*args,**kwargs):
		super(viewNoticeClass,self).__init__(*args,**kwargs)
		#self.SetTitle("Notice Editor")
		self.SetSize((720,720))
		self.panel = wx.Panel(self)
		self.dataOLV = ObjectListView(self,-1,style =wx.LC_REPORT)
		self.basicGUI()

	def basicGUI(self):
		mainSizer = wx.BoxSizer(wx.VERTICAL)     

		editNoticeBtn = wx.Button(self,-1,"EDIT")
		self.Bind(wx.EVT_BUTTON,self.edit,editNoticeBtn)

 		mainSizer.Add(editNoticeBtn,0,wx.ALL|wx.ALIGN_CENTER,20)
		mainSizer.Add(self.dataOLV, 1, wx.ALL|wx.EXPAND, 20)
		
		self.SetSizer(mainSizer)
		data = readFile('notice')
		self.dataOLV.SetColumns([ColumnDefn("date", "left", 100, "date"),ColumnDefn("path","left",220,"path"),ColumnDefn("Title","left",100,"description"),ColumnDefn("Category","left",100,"category"),ColumnDefn("Remove","left",50,"")])
		
		self.dataOLV.SetObjects(data)

	def edit(self,e):
		print "Openig Notice Edit Window"
		row = self.dataOLV.GetSelectedObject()
		Notice = NoticeClass(None)
		Notice.basicGUI()
		Notice.update(row)
		Notice.ShowModal()
		Notice.Destroy()
		self.dataOLV.SetObjects(readFile('notice'))






def main():
	app = wx.App()
	windowClass(None)
	app.MainLoop()

main()







