import wx
import os
import ftplib
import geet

host = '10.0.0.4'
port = '2121'

class commit():
	def __init__(self,*args,**kwargs):
		self.login_cred();

	def login_cred(self):
		print "Commiting staged changes"
		username = wx.TextEntryDialog(None,message = "Enter username for FTP server : ",caption = "FTP",style =wx.OK|wx.CANCEL|wx.CENTER)
		if(username.ShowModal() == wx.ID_OK):
			password = wx.PasswordEntryDialog(None,message = "Enter password for FTP server : ",caption = "FTP",style =wx.CENTER|wx.OK|wx.CANCEL)
			if(password.ShowModal()==wx.ID_OK):
				self.username = username.GetValue()
				self.password = password.GetValue()
				self.establish_connec()
			else:
				print 'Commit terminated : password'
				return
		else:
			print 'Commit cancelled : username'
			return

	def establish_connec(self):
		ftp = ftplib.FTP()
		ftp.connect(host,port,100)
		ftp.login(user = self.username,passwd = self.password)
		ftp.set_debuglevel(1)
		added_files = geet.readfile("added")
		moded_files = geet.readfile("modified")
		deleted_files = geet.readfile("deleted")
		
		if geet.isnotempty_util(added_files):
			for i in range(len(added_files)):
				if added_files[i]['DIR'] == 'true':
					try:
						ftp.voidcmd('mkd ' + os.path.join(ftp.pwd(),added_files[i]['path']))
					except ftplib.error_perm,e:
						if int(e.args[0][:3]) == 550:
							continue
						else:
							print str(e)

				else:
					try:
						ftp.storbinary('STOR ' + added_files[i]['path'],open(added_files[i]['abspath'],'rb'))
					except e:
						print str(e)

		if(geet.isnotempty_util(moded_files)):
			for i in range(len(moded_files)):
				if moded_files[i]['DIR'] == 'true':
					try:
						ftp.voidcmd('mkd ' + os.path.join(ftp.pwd(),moded_files[i]['path']))
					except ftplib.error_perm,e:
						if int(e.args[0][:3]) == 550:
							continue
						else:
							print str(e)
				else:
					try:
						ftp.delete(moded_files[i]['path'])
					except e:
						print str(e)
					try:
						ftp.storbinary('STOR '+ added_files[i][path],open(added_files[i]['abspath'],'rb'))
					except e:
						print str(e)

		if(geet.isnotempty_util(deleted_files)):
			for i in range(len(deleted_files)):
				if deleted_files[i]['DIR'] == 'false':
					try:
						ftp.delete(deleted_files[i]['path'])
					except e:
						print str(e)
				else:
					try:
						ftp.rmd(deleted_files[i]['path'])
					except e:
						print str(e)


		print ftp.pwd()
		ftp.quit()
		geet.clean_temp2()





