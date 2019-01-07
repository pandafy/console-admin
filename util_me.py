import json
from shutil import copyfile
from ntpath import basename
from os import remove

NOTICE_JSON = '/home/stark/Desktop/Notices/data.json'
FACULTY_DIR = '/home/stark/Desktop/Faculty_info/' 
NOTICE_DIR = '/home/stark/Desktop/Notices/'
ECE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/ece_faculty.json'
CSE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/cse_faculty.json'
MAE_FACULTY_JSON = '/home/stark/Desktop/Faculty_info/mae_faculty.json'


def appendNotices(date,title,path,category):
	FileName = basename(path)
	FilePath = NOTICE_DIR + FileName
	copyfile(path,FilePath)
	new_notice = {"id" : 99 , "date" : date, "path" : FilePath , "description" : title ,"category" : category}
	Database = NOTICE_JSON
	print("Reading : ",Database)
	with open (Database) as json_file :
		filedata = json.load(json_file)
		new_notice["id"] = filedata[0]["id"] + 1
		filedata = [new_notice] + filedata
		with open (Database,'w') as outfile : 
			json.dump(filedata, outfile,indent=4)

def EditNotices(id,date,title,path,category):
	FilePath = path
	Database = NOTICE_JSON
	with open (Database) as json_file :
		filedata = json.load(json_file)
		if filedata[len(filedata)-id]["id"] == id :
			index = len(filedata)-id
		else:
			for x in range(len(filedata)):
				if filedata[x]["id"] == id :
					index = x
					break
		#Chcek if previous image and profile are to be removed
		if filedata[index]["path"] != path :
			remove(filedata[index]["path"])
			FilePath = FACULTY_DIR + basename(image)
			copyfile(path,FilePath)
		new_notice = {"id" : id, "date" : date, "path" : FilePath , "description" : title ,"category" : category}
		diffkeys = [k for k in new_notice if filedata[index][k] != new_notice[k]]
		for k in diffkeys:
  			print k, ':', filedata[index][k], '->', new_notice[k]

		filedata[index] = new_notice
		with open (Database,'w') as outfile : 
			json.dump(filedata, outfile,indent=4)
			outfile.close()
		json_file.close()

def appendFaculty(dep,image,name,designation,qualification,specialization,email,profile):
	ImagePath = FACULTY_DIR + basename(image)
	ProfilePath = FACULTY_DIR +basename(profile)
	copyfile(image,ImagePath)
	copyfile(profile,ProfilePath)
	new_entry = { "id" : "",
	"image" : ImagePath ,
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

		new_entry["id"] = filedata[len(filedata)-1]["id"]
		filedata = filedata + [new_entry]
		with open (Database,'w') as outfile : 
			json.dump(filedata, outfile,indent=4)
			outfile.close()
		json_file.close()

def EditFaculty(id,dep,image,name,designation,qualification,specialization,email,profile):
	ImagePath = image
	ProfilePath = profile
	


	if dep == 'CSE':
		Database = CSE_FACULTY_JSON
	elif dep == 'MAE':
		Database = MAE_FACULTY_JSON
	elif dep == 'ECE':
		Database = ECE_FACULTY_JSON

	with open(Database) as json_file:
		filedata = json.load(json_file)

		if filedata[id]["id"] == id :
			index = id
		else:
			for x in range(len(filedata)):
				if filedata[x]["id"] == id :
					index = x
					break
		#Chcek if previous image and profile are to be removed
		if filedata[index]["image"] != image :
			remove(filedata[index]["image"])
			ImagePath = FACULTY_DIR + basename(image)
			ProfilePath = FACULTY_DIR +basename(profile)

			copyfile(image,ImagePath)
			copyfile(profile,ProfilePath)
		
			

		new_entry = { "id" : id,
		"image" : ImagePath ,
		 "name" : name , 
	 	  "designation" : designation ,
	  	   "qualification" : qualification ,
	   		"specialization" : specialization ,
	   		 "email" : "<a href='mailto:" + email + "' target='_blank'>'" + email + "'</a>" ,
	    	  "profile" : "<a href='" + profile +"'>See Profile</a>"
	      }

		diffkeys = [k for k in new_entry if filedata[index][k] != new_entry[k]]
		for k in diffkeys:
  			print k, ':', filedata[index][k], '->', new_entry[k]




		filedata[index] = new_entry
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

def DeleteNotice(id):
	filepath = NOTICE_JSON
	

	json_file=	open(Database,'r')
	try:
		filedata = json.load(json_file)
		if filedata[id]["id"] == id :
			index = id
		else:
			for x in range(len(filedata)):
				if filedata[x]["id"] == id :
					index = x
					break
		del filedata[index]
	except ValueError :
		filedata = json_file.read()
		print json_file.read()
	json_file.close()
	json_file=	open(Database,'w')
	json.dump(filedata,json_file,indent=4)


	return filedata

def DeleteFaculty(id,dep):
	if dep == 0:
		Database = CSE_FACULTY_JSON
	elif dep == 2:
		Database = MAE_FACULTY_JSON
	elif dep == 1:
		Database = ECE_FACULTY_JSON

	json_file=	open(Database,'r')
	try:
		filedata = json.load(json_file)
		if filedata[len(filedata)-id-1]["id"] == id :
			index = len(filedata)-id-1
		else:
			for x in range(len(filedata)):
				if filedata[x]["id"] == id :
					index = x
					break
		del filedata[index]
	except ValueError :
		filedata = json_file.read()
		print json_file.read()
	json_file.close()
	json_file=	open(Database,'w')
	json.dump(filedata,json_file,indent=4)


	return filedata
