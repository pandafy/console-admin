import wx
from util_me import *
from ObjectListView import ObjectListView, ColumnDefn

class addFacultyClass(wx.Dialog):
	def __init__(self,*args,**kwargs):
		super(addFacultyClass,self).__init__(*args,**kwargs)
		self.SetTitle('Add Faculty')
		self.SetSize((750,600))
		self.PhotoMaxSize = 200
		self.panel = wx.Panel(self)

	def basicGUI(self):
		self.sizer = wx.GridBagSizer(5,5)

		SName = wx.StaticText(self.panel,-1,"Name : ")
		self.CName = wx.TextCtrl(self.panel,-1)
		SDesignation = wx.StaticText(self.panel,-1,"Designation : ")
		self.CDesignation = wx.TextCtrl(self.panel,-1)
		SQualification = wx.StaticText(self.panel,-1,"Qualification : ")
		self.CQualification = wx.TextCtrl(self.panel,-1)
		SSpecialization = wx.StaticText(self.panel,-1,"Specialization : ")
		self.CSpecialization = wx.TextCtrl(self.panel,-1)
		SEmail = wx.StaticText(self.panel,-1,"Email : ")
		self.CEmail = wx.TextCtrl(self.panel,-1)
		SImage = wx.StaticText(self.panel,-1,"Select an image :")
		self.CImage = wx.TextCtrl(self.panel,-1)
		SProfile = wx.StaticText(self.panel,-1,'Profile :')
		self.CProfile =wx.TextCtrl(self.panel,-1)
		img = wx.EmptyImage(200,200)
		self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,wx.BitmapFromImage(img))
		lblList = ['CSE', 'ECE', 'MAE']     
		self.rbox = wx.RadioBox(self.panel,label = 'Department', choices = lblList ,majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
		addImgBtn = wx.Button(self.panel,-1,'Image')
		self.Bind(wx.EVT_BUTTON,self.chooseImage,addImgBtn)
		addProfileBtn = wx.Button(self.panel,-1,'Profile')
		self.Bind(wx.EVT_BUTTON,self.chooseProfile,addProfileBtn)
		self.FacultyBtn = wx.Button(self.panel,-1,'ADD')
		



		self.sizer.Add(SName,pos = (1,1),flag = wx.ALL|wx.ALIGN_CENTER,border=5)
		self.sizer.Add(self.CName,pos = (1,3),span = (1,9),flag = wx.ALL|wx.EXPAND,border=5)
		self.sizer.Add(SDesignation,pos = (2,1),flag = wx.ALL|wx.ALIGN_LEFT, border = 5)
		self.sizer.Add(self.CDesignation,pos = (2,3),span = (1,9),flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(SQualification,pos = (3,1),flag = wx.ALL|wx.ALIGN_CENTER, border = 5)
		self.sizer.Add(self.CQualification,pos = (3,3),span = (1,9),flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(SSpecialization,pos = (4,1),flag = wx.ALL|wx.ALIGN_CENTER, border = 5)
		self.sizer.Add(self.CSpecialization,pos = (4,3),span = (1,9),flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(SEmail,pos = (5,1),flag = wx.ALL|wx.ALIGN_CENTER, border = 5)
		self.sizer.Add(self.CEmail,pos = (5,3),span = (1,9),flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(SProfile,pos = (6,1),flag = wx.ALL|wx.ALIGN_RIGHT,border = 5)
		self.sizer.Add(self.CProfile,pos = (6,3),span = (1,8) ,flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(SImage,pos = (1,12),flag = wx.ALL|wx.ALIGN_LEFT, border = 5)
		self.sizer.Add(self.CImage,pos = (7,12),span = (1,4),flag = wx.ALL|wx.EXPAND,border = 5)
		self.sizer.Add(self.imageCtrl,pos = (2,12),span = (5,5),flag = wx.ALL|wx.EXPAND)
		self.sizer.Add(addImgBtn,pos = (1,14),flag = wx.ALIGN_RIGHT)
		self.sizer.Add(addProfileBtn,pos = (6,11),span = (1,1),flag = wx.ALIGN_RIGHT|wx.ALIGN_CENTER,border = 5)
		self.sizer.Add(self.rbox,pos = (7,1), span
		 = (3,10),flag = wx.ALIGN_LEFT|wx.ALL,border = 5)
		self.sizer.Add(self.FacultyBtn,pos = (10,8),span=(1,1), flag = wx.ALIGN_CENTER, border = 5)


		self.panel.SetSizer(self.sizer)

	

	def adFaculty(self,e):
		print "Appending Faculty entry to JSON"
		image = self.CImage.GetValue()
		name = self.CName.GetValue()
		designation = self.CDesignation.GetValue()
		qualification = self.CQualification.GetValue()
		specialization = self.CSpecialization.GetValue()
		email = self.CEmail.GetValue()
		profile = self.CProfile.GetValue()
		department = self.rbox.GetString(self.rbox.GetSelection())

		appendFaculty(department,image,name,designation,qualification,specialization,email,profile)

	def add(self):
		self.Bind(wx.EVT_BUTTON,self.adFaculty,self.FacultyBtn)

	def update(self,row,dep):

		self.FQual = row["qualification"]
		self.FSpec = row["specialization"]
		self.FEmail = emailFromJSON(row["email"])
		self.FProfile = profileFromJSON(row["profile"])
		self.FImage = row["image"]
		self.FName = row["name"]
		self.FDesign = row["designation"]
		self.FDep = dep
		self.id = row["id"]

		self.SetTitle("Edit")
		self.CImage.SetValue(self.FImage)
		self.CName.SetValue(self.FName)
		self.CDesignation.SetValue(self.FDesign)
		self.CQualification.SetValue(self.FQual)
		self.CSpecialization.SetValue(self.FSpec)
		self.CEmail.SetValue(self.FEmail)
		self.CProfile.SetValue(self.FProfile)
		self.rbox.SetSelection(self.FDep)
		self.setImage(self.FImage)

		self.FacultyBtn.SetLabel("EDIT")
		self.Bind(wx.EVT_BUTTON,self.editFaculty,self.FacultyBtn)

		DeleteBtn = wx.Button(self.panel,wx.ID_ANY,'DELETE')
		self.Bind(wx.EVT_BUTTON,self.delFaculty,DeleteBtn)
		self.sizer.Add(DeleteBtn,pos = (10,11),span=(1,1), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)



	def editFaculty(self,e):
		print "Editing faculty information \n Changes are : "

		image = self.CImage.GetValue()
		name = self.CName.GetValue()
		designation = self.CDesignation.GetValue()
		qualification = self.CQualification.GetValue()
		specialization = self.CSpecialization.GetValue()
		email = self.CEmail.GetValue()
		profile = self.CProfile.GetValue()
		department = self.rbox.GetString(self.rbox.GetSelection())
		EditFaculty(self.id,department,image,name,designation,qualification,specialization,email,profile)
		self.Destroy()

	def setImage(self,imgPath):
		img = wx.Image(imgPath, wx.BITMAP_TYPE_ANY)

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

	def chooseImage(self,e):
		print "Browsing files"
		wildcard = "All files (*.*)|*.*|Image Files |*.png;*.jpg;*.jpeg|PDF Files (*.pdf)|*.pdf"
		fileDialog = wx.FileDialog(self, "Open Profile image", wildcard=wildcard,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
 		if fileDialog.ShowModal() == wx.ID_CANCEL:
 			return
		self.CImage.SetValue(fileDialog.GetPath())
		self.setImage(fileDialog.GetPath())

	def chooseProfile(self,e):
		print "Browsing files"
		wildcard = "All files (*.*)|*.*|Image Files |*.png;*.jpg;*.jpeg|PDF Files (*.pdf)|*.pdf"
		fileDialog = wx.FileDialog(self, "Open Profile ", wildcard=wildcard,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
 		if fileDialog.ShowModal() == wx.ID_CANCEL:
 			return
		self.CProfile.SetValue(fileDialog.GetPath())

	def delFaculty(self,e):
		print "Do you want to delete this entry ? : "
		confirmation = wx.MessageDialog(self,'Are you sure to delete this faculty info?','Confirmation',wx.YES_NO|wx.NO_DEFAULT|wx.CENTRE|wx.STAY_ON_TOP)
		answer = confirmation.ShowModal()
		if answer == wx.ID_YES:
			print "\b Yes"
			print self.FDep
			DeleteFaculty(self.id,self.FDep)
			self.Destroy()

#############################################################################################################


class viewFacultyClass(wx.Dialog):
	def __init__(self,*args,**kwargs):
		super(viewFacultyClass,self).__init__(*args,**kwargs)
		#self.SetTitle("Notice Editor")
		self.SetSize((720,720))
		self.panel = wx.Panel(self)
		self.dataOLV1 = ObjectListView(self,-1,style =wx.LC_REPORT)
		self.dataOLV2 = ObjectListView(self,-1,style =wx.LC_REPORT)
		self.dataOLV3 = ObjectListView(self,-1,style =wx.LC_REPORT)

		self.basicGUI()

	def basicGUI(self):
		
		mainSizer = wx.BoxSizer(wx.VERTICAL) 

		CSE_LABEL = wx.Button(self,-1,'CSE Department')       
		self.Bind(wx.EVT_BUTTON,self.editCSE,CSE_LABEL)
 		MAE_LABEL = wx.Button(self,-1,'MAE Department')
 		self.Bind(wx.EVT_BUTTON,self.editMAE,MAE_LABEL)
 		ECE_LABEL = wx.Button(self,-1,'ECE Department')
 		self.Bind(wx.EVT_BUTTON,self.editECE,ECE_LABEL)

		mainSizer.Add(CSE_LABEL,0,wx.ALIGN_CENTER|wx.ALL,10)
		mainSizer.Add(self.dataOLV1, 1, wx.ALL|wx.EXPAND, 10)
		mainSizer.Add(ECE_LABEL,0,wx.ALIGN_CENTER,10)
		mainSizer.Add(self.dataOLV2, 1, wx.ALL|wx.EXPAND, 10)
		mainSizer.Add(MAE_LABEL,0,wx.ALIGN_CENTER,10)
		mainSizer.Add(self.dataOLV3, 1, wx.ALL|wx.EXPAND, 10)


		self.SetSizer(mainSizer)
		
		self.dataOLV1.SetColumns([
			ColumnDefn("Image","left",220,"image"),
			ColumnDefn("Name","left",100,"name"),
			ColumnDefn("Designation","left",100,"designation"),
			ColumnDefn("Qualification","left",50,"qualification"),
			ColumnDefn("Specialization","left",50,"specialization"),
			ColumnDefn("Email","left",50,"email"),
			ColumnDefn("Profile","left",50,"profile")
			])
		self.dataOLV2.SetColumns([
			ColumnDefn("Image","left",220,"image"),
			ColumnDefn("Name","left",100,"name"),
			ColumnDefn("Designation","left",100,"designation"),
			ColumnDefn("Qualification","left",50,"qualification"),
			ColumnDefn("Specialization","left",50,"specialization"),
			ColumnDefn("Email","left",50,"email"),
			ColumnDefn("Profile","left",50,"profile")
			])
		self.dataOLV3.SetColumns([
			ColumnDefn("Image","left",220,"image"),
			ColumnDefn("Name","left",100,"name"),
			ColumnDefn("Designation","left",100,"designation"),
			ColumnDefn("Qualification","left",50,"qualification"),
			ColumnDefn("Specialization","left",50,"specialization"),
			ColumnDefn("Email","left",50,"email"),
			ColumnDefn("Profile","left",50,"profile")
			])
		data = readFile('faculty_cse')
		self.dataOLV1.SetObjects(data)
		data = readFile('faculty_ece')
		self.dataOLV2.SetObjects(data)
		data = readFile('faculty_mae')
		self.dataOLV3.SetObjects(data)

	


	def editCSE(self,e):
		print "Opening edit window"
		row = self.dataOLV1.GetSelectedObject()
		editSel = addFacultyClass(None)
		editSel.basicGUI()
		editSel.update(row,0)
		editSel.ShowModal()
		self.dataOLV1.SetObjects(readFile('faculty_cse'))
		editSel.Destroy()
	
	def editECE(self,e):
		print "Opening edit window"
		row = self.dataOLV2.GetSelectedObject()
		editSel = addFacultyClass(None)
		editSel.basicGUI()
		editSel.update(row,1)
		editSel.ShowModal()
		self.dataOLV2.SetObjects(readFile('faculty_ece'))

	def editMAE(self,e):
		print "Opening edit window"
		row = self.dataOLV3.GetSelectedObject()
		editSel = addFacultyClass(None)
		editSel.basicGUI()
		editSel.update(row,2)
		editSel.ShowModal()
		self.dataOLV3.SetObjects(readFile('faculty_mae'))





	

