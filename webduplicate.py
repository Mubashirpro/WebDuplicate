from bs4 import BeautifulSoup
import requests
import time
from colorama import  Fore
import os

print(Fore.CYAN,"@@@@ @@@@  @@@@""\n""@@@ @@@ @@@ @@@ @@@")


print(Fore.GREEN+"Web Duplicater""\n")
print("_______________")
print("Code by Mubashir69")
print("_______________")



url = str(input(Fore.LIGHTYELLOW_EX+"Enter URL of Site you want to duplicate : "))
file_name = str(input("File name to save :"))

os.chdir("/storage/emulated/0/WebDuplicate/Sites/")

path = "/storage/emulated/0/WebDuplicate/Sites/"+file_name+".html"


op = int(input("[1] Start ""\n""[0] Back""\n"))
if op == 0:
	url = str(input("Enter URL of Site you want to duplicate : "))
else:
	
 s = requests.get(url)
 u = s.text

time.sleep(1)
print(Fore.CYAN+"Downloading..")
time.sleep(0.3)
print(Fore.CYAN+"Downloading...")
with open(path,"w") as d:
  	d.write(u)
  	d.close()
  	print(f"file saved as : {path}")
