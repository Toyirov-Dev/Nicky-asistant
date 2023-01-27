# modules
from click_shell import shell 
import os
import datetime
from time import sleep
from tqdm import tqdm
import socket
from plyer import notification
import time
import random 
import PIL
from PIL import Image
import pyautogui
from turtle import *
import subprocess









# clear and color terminal  
try:
	os.system("cls")
except:
	pass

try:
	os.system("color C")
except:
	pass



# ip
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


# ERROR!
def Error():
	if __name__ == '__main__':
		notification.notify(
			title=" * Nicky Asisant * ", 
			message=" Sorry, something went wrong. \n Try again. ",
			app_icon="Assets/icon/logo.ico",
			timeout=5)


# fake code
fc = """
	import getpass

	USER_NAME = getpass.getuser()

	bat_path = r'nothing nothing

	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		   bat_file.write(r'''@echo off
	Tree pause ''')
		
		# It's True code :)
		"""

fk = """
	a = 1
	age = input("How old are you: ")
	try: 
		age = int(age)

		print(f"You [2023-age] years old")

	except:
		print(" Error, please, check again!")

	python3 -m pip uninstall
			Mya Asisant

	for x in range(9999):
		a += 1
		print("Oh, Shit ", a)

"""

ntr = """
	Welcome to the Nicky Asistant! 
	Enter a command down below.  Enter "Help".
	Version 1, 16.01.2023
	Created by Toyirov Dev (Ziyodullo)

"""

# intro
@shell(prompt=" ==> ", intro=ntr)
def Nicky_shell():
	pass  



# help command
@Nicky_shell.command()
def Help():
	print("""
 █
 	█ © Toyirov-Dev 
 █	

     Write in lower case only!

 -> "help"		See this list.
 -> "msg"		Show Alert.
 -> "newfile"		Create new file.
 -> "notepad"		Open notepad.
 -> "paint"		Open paint.
 -> "whoami"		Displays the current domain and user name.
 -> "sayth"		Say anything.
 -> "time"		Show time and date.
 -> "colors"		Print Nicky terminal colors list.
 -> "llh"		Look like hacker :)
 -> "randpass"		Make strong password.
 -> "imgcompressor"	Compress Images.
 -> "spiner"		Spiner for fun.
 -> "timer"		Cauntdown.
 -> "write"		Write as notepad.
 -> "cmd"		Write command cmd.
 -> "shutdown"		Shutdown pc after 10 second.
 -> "clear"		Clear terminal.

 -> "exit"		Exit the Nicky Asistant. 

	""")

# msg command
@Nicky_shell.command()
def msg():
	msg_input = input(" Enter anything: ")
	try:
		os.system("msg * " + msg_input )
	except:
		print(" Error!")
		Error()

# newfile command
@Nicky_shell.command()
def newfile():
	print("")
	file_name = input("    Enter the file name: ")
	content = input("    Enter the file content: ")
	print("")

	try:
		with open(file_name, "w") as f:
			f.write(content)
	except:
		print(" No such file or directory! Please check and try again.")
		Error()

# notepad command
@Nicky_shell.command()
def Notepad():
	try:
		os.system("notepad")
	except: 
		print(" Notepad not found :(")
		Error()

# paint command
@Nicky_shell.command()
def paint():
	try:
		os.system("mspaint")
	except: 
		print(" paint not found :(")
		Error()

# whoamI command
@Nicky_shell.command()
def whoami():
	try:
		os.system("whoami")
		print("")
	except:
		print(" Sorry, I don't know!")
		Error()

# say anything command 
@Nicky_shell.command()
def sayth():
	print(" Write anything down below.")
	print(" Press 'ctrl + c' for exit.\n")
	subprocess.call(["Assets\\scripts\\speak.exe"])




# show time command
@Nicky_shell.command()
def time():
	dtmnow = datetime.datetime.now()
	print(" ", dtmnow, "\n")

# print colors list
@Nicky_shell.command()
def colors():
	print("""
 blue    =  Blue		blue2    =  Bright blue
 green   =  Green		green2   =  Bright green
 cyan    =  Cyan		cyan2    =  Bright cyan
 red     =  Red			red2     =  Bright red
 violet  =  Violet		violet2  =  Bright violet
 yellow  =  Yellow
 gray    =  Gray

 	Example: red2
	""")

# Blue color command
@Nicky_shell.command()
def blue():
	try:
		os.system("color 1")
	except:
		print(" Error!")
		Error()

# Green color command
@Nicky_shell.command()
def green():
	try:
		os.system("color 2")
	except:
		print(" Error!")
		Error()


# Cyan color command
@Nicky_shell.command()
def cyan():
	try:
		os.system("color 3")
	except:
		print(" Error!")
		Error()

# Red color command
@Nicky_shell.command()
def red():
	try:
		os.system("color 4")
	except:
		print(" Error!")
		Error()

# Violet color command
@Nicky_shell.command()
def violet():
	try:
		os.system("color 5")
	except:
		print(" Error!")
		Error()

# Yellow color command
@Nicky_shell.command()
def yellow():
	try:
		os.system("color 6")
	except:
		print(" Error!")
		Error()

# Gray color command
@Nicky_shell.command()
def gray():
	try:
		os.system("color 8")
	except:
		print(" Error!")
		Error()

# Bright blue color command
@Nicky_shell.command()
def blue2():
	try:
		os.system("color 9")
	except:
		print(" Error!")
		Error()

# Bright green color command
@Nicky_shell.command()
def green2():
	try:
		os.system("color A")
	except:
		print(" Error!")
		Error()

# bright cyan color command
@Nicky_shell.command()
def cyan2():
	try:
		os.system("color B")
	except:
		print(" Error!")
		Error()

# Bright red color command
@Nicky_shell.command()
def red2():
	try:
		os.system("color C")
	except:
		print(" Error!")
		Error()

# Bright violet color command
@Nicky_shell.command()
def violet2():
	try:
		os.system("color D")
	except:
		print(" Error!")
		Error()


# Make directory command
@Nicky_shell.command()
def mkdir():
	md_inp = input(" Enter directory name: ")

	try:
		os.system("mkdir " + md_inp)
		print(" Directory created!\n")
	except:
		print(" Error!")
		Error()


# Look like hacker command
@Nicky_shell.command()
def LLH():
	input(" Enter secret password: ")
	print("  password added! Start code!\n")

	input("    █ ")
	sleep(0.5)
	print(" if __name__ == '__main__':\n")

	input("    █ ")
	sleep(0.5)
	print(fc)

	input("    █ ")
	sleep(0.5)
	print(" Your ip address: ", ip, "\n")
	sleep(0.5)
	print(fk)

	sleep(2)

	for x in tqdm(range(1000)):
		sleep(0.01)

	print(" Hacked :) \n")


# Shutdown command
@Nicky_shell.command()
def shutdown():
	try:
		os.system("Shutdown /s /t 10")
	except:
		print(" Error!")
		Error()

# Clear command
@Nicky_shell.command()
def clear():
	try:
		os.system("cls")
		print(ntr)
	except:
		print(" Error!")
		Error()

# whereami command
@Nicky_shell.command()
def whereami():
	try:
		os.system("chdir")
		print("")
	except:
		print(" Error!")
		Error()

# make password
@Nicky_shell.command()
def randpass():
	small = "qwertyuiopasdfghjklzxcvbnm"
	large = "QWERTYUIOPASDFGHJKLZXCVBNM"
	number = "0123456789"
	symbol = "/<>?][}{=_)(*&%$#@!"

	string = small + large + number + symbol
	try:
		password = "".join(random.sample(string, 8))
		password2 = "".join(random.sample(string, 16))
		print(" Random password is:   ", password)
		print(" Random password 2 is: ", password2)
	except:
		print(" Error!")
		Error()


# cmd command
@Nicky_shell.command()
def cmd():
	while True:
		cmnd = input("-> ")
		os.system(cmnd)

		if cmnd.lower() == "exit":
			break
		if cmnd.lower() == "exit ":
			break
		if cmnd.lower() == " exit":
			break
		if cmnd.lower() == " exit ":
			break

# Image compressor command
@Nicky_shell.command()
def Imgcompressor():
	randmnum = random.randint(1, 100000)
	randmnum = str(randmnum)

	Image_path = input("Add image path: ")
	img = PIL.Image.open(Image_path)
	height, width = img.size

	img = img.resize((height, width),PIL.Image.ANTIALIAS)
	img.save("Files/" + randmnum + ".jpg")

	print("\n Image in Files\n")

# screenshot command
@Nicky_shell.command()
def screenshot():
	print(" Take screenshot after 3 second.")
	randmnum = random.randint(1, 100000)
	randmnum = str(randmnum)

	sleep(2)
	screen = pyautogui.screenshot() 
	screen.save("Files/" + randmnum + ".png")
	print(" Screenshot saved in 'Files'.")


# spiner command 
@Nicky_shell.command()
def spiner():	
	print(" Press space key!")
	subprocess.call(["Assets\\scripts\\spiner.exe"])

# Timer command
@Nicky_shell.command()
def timer():
	minute = int(input(" Enter minute: "))
	second = minute * 60
	
	def cdown(t):
		while t:
			minu, secu = divmod(t, 60)
			cdt = '{:02d}:{:02d}'.format(minu, secu)
			print(cdt, end="\r")
			sleep(1)
			t -= 1

	cdown(second) 
	print(" Times up!")
	os.system("msg * Times up 'brah' ")
	
# write command
@Nicky_shell.command()
def write():
	print(" 'exit'		Exit the write command.\n")
	while True:
		inp = input()

		if inp.lower() == "exit":
			break
		if inp.lower() == "exit ":
			break
		if inp.lower() == " exit":
			break
		if inp.lower() == " exit ":
			break










# run
if __name__ == '__main__':
	Nicky_shell()