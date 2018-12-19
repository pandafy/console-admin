import json
from datetime import date
from shutil import copyfile
from ntpath import basename

NOTICE_JSON = '/home/stark/Desktop/Notices/data.json'
FACULTY_DIR = '/home/stark/Desktop/Faculty_info/' 
NOTICE_DIR = '/home/stark/Desktop/Notices/'
ECE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/ece_faculty.json'
CSE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/cse_faculty.json'
MAE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/mae_faculty.json'


today = str(date.today())
def appendNotices(title,path,category):
	FileName = basename(path)
	FilePath = NOTICE_DIR + FileName
	copyfile(path,FilePath)
	new_notice = {"date" : today , "path" : FilePath , "description" : title ,"category" : category}
	Database = NOTICE_JSON
	print("Reading : ",Database)
	with open (Database) as json_file :
		filedata = json.load(json_file)
		filedata = [new_notice] + filedata
		with open (Database,'w') as outfile : 
			json.dump(filedata, outfile,indent=4)

def appendFaculty(dep,image,name,designation,qualification,specialization,email,profile):
	ImagePath = FACULTY_DIR + basename(image)
	ProfilePath = FACULTY_DIR +basename(profile)
	copyfile(image,ImagePath)
	copyfile(profile,ProfilePath)
	new_entry = {"image" : ImagePath ,
	 "name" : name , 
	 "designation" : designation ,
	  "qualification" : qualification ,
	   "specialization" : specialization ,
	    "email" : "<a href='mailto:" + email + "' target='_blank'>'" + email + "'</a>" ,
	     "profile" : "<a href='" + profile +"'>See Profile</a>"
	      }

	if dep == 'CSE':
		Database = CSE_FACULTY_JSON
	elif dep == 'MAE':
		Database = MAE_FACULTY_JSON
	elif dep == 'ECE':
		Database = ECE_FACULTY_JSON
	
	#print("Reading : ",Database)
	with open (Database) as json_file :
		filedata = json.load(json_file)
		filedata = filedata + [new_entry]
		with open (Database,'w') as outfile : 
			json.dump(filedata, outfile,indent=4)
			outfile.close()
		json_file.close()

def readFile(file_type):
	if file_type == 'notice':
		filepath = NOTICE_JSON
	elif file_type == 'faculty_ece':
		filepath = ECE_FACULTY_JSON
	elif file_type == 'faculty_cse':
		filepath = CSE_FACULTY_JSON
	elif file_type == 'faculty_mae':
		filepath = MAE_FACULTY_JSON
	

	json_file =	open(filepath,'r')
	try:
		filedata = json.load(json_file)
	except ValueError :
		filedata = json_file.read()
		print json_file.read()
	json_file.close()
	return filedata

def emailFromJSON(email):
	email = email[email.find('to:'):]
	email = email[3:]
	email = email[:email.find("' ")]	
	return email

def profileFromJSON(profile):
	profile = profile[profile.find("='"):]
	profile = profile[2:]
	profile = profile[:profile.find("'>")]
	return profile
