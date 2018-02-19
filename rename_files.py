import os


def rename_files():
	
	# pull all files in given directoy and rename
	files = os.listdir("/Users/Sajib/Music/iTunes/iTunes Music/Yanni/In My Time")
	print(files)
	
	# Get current directory
	saved_path= os.getcwd()
	print("Current Working directory -" + saved_path)
	
	
	# change current directory to our specific directory
	os.chdir("/Users/Sajib/Music/iTunes/iTunes Music/Yanni/In My Time")
	
	for file in files:
		print("Old Name -" + file)
		print("New Name - " + file.translate(None,"1234567890"))
		# renaming all files
		os.rename(file, file.translate(None,"1234567890"))
	# Return to directory which is current directory
	os.chdir(saved_path)
	
rename_files()