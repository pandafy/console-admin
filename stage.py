import wx
from ObjectListView import ObjectListView, ColumnDefn
from geet import readfile,create_temp_files


class stageViewClass(wx.Dialog):
	def __init__(self,*args,**kwargs):
		super(stageViewClass,self).__init__(*args,**kwargs)

		self.SetSize((720,720))
		self.SetTitle("Staged Files")
		self.panel = wx.Panel(self)
		self.added = ObjectListView(self,-1,style =wx.LC_REPORT)
		self.moded = ObjectListView(self,-1,style =wx.LC_REPORT)
		self.deleted = ObjectListView(self,-1,style =wx.LC_REPORT)

		self.basicGUI()

	def basicGUI(self):
		create_temp_files()

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		addedLabel = wx.StaticText(self,-1, 'Added Files')
		modedLabel = wx.StaticText(self,-1, 'Modified Files')
		deletedLabel = wx.StaticText(self,-1, 'Deleted Files')

		mainSizer.Add(addedLabel,0,wx.ALIGN_CENTER|wx.ALL,10)
		mainSizer.Add(self.added, 1, wx.ALL|wx.EXPAND, 10)
		mainSizer.Add(modedLabel,0,wx.ALIGN_CENTER,10)
		mainSizer.Add(self.moded, 1, wx.ALL|wx.EXPAND, 10)
		mainSizer.Add(deletedLabel,0,wx.ALIGN_CENTER,10)
		mainSizer.Add(self.deleted, 1, wx.ALL|wx.EXPAND, 10)

		self.SetSizer(mainSizer)

		self.added.SetColumns([
			ColumnDefn("FileName","left",100,"name"),
			ColumnDefn("FilePath","left",100,"path"),
			ColumnDefn("Absolute FilePath","left",250,"abspath"),
			ColumnDefn("Date","left",200,"date"),
			ColumnDefn("DIR","left",40,"DIR")
			])

		self.moded.SetColumns([
			ColumnDefn("FileName","left",100,"name"),
			ColumnDefn("FilePath","left",100,"path"),
			ColumnDefn("Absolute FilePath","left",250,"abspath"),
			ColumnDefn("Date","left",200,"date"),
			ColumnDefn("DIR","left",70,"DIR")
			])

		self.deleted.SetColumns([
			ColumnDefn("FileName","left",100,"name"),
			ColumnDefn("FilePath","left",100,"path"),
			ColumnDefn("Absolute FilePath","left",250,"abspath"),
			ColumnDefn("Date","left",200,"date"),
			ColumnDefn("DIR","left",40,"DIR")
			])

		try:
			data = readfile("added")
		except e:
			data = []
		self.added.SetObjects(data)
		try:
			data = readfile("modified")
		except e:
			data = []
		self.moded.SetObjects(data)
		try:
			data = readfile("deleted")
		except e:
			data = []
		self.deleted.SetObjects(data)