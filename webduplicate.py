from bs4 import BeautifulSoup
import requests
import time



print("Web Duplicater""\n")
print("_______________")
print("Code by Mubashir69")
print("_______________")



url = str(input("Enter URL of Site you want to duplicate : "))
file_name = str(input("File name to save :"))

path = "/storage/emulated/0/WebDuplicate/Sites/"+file_name+".html"


op = int(input("[1] Start ""\n""[0] Back""\n"))
s = requests.get(url)
u = s.text
b = BeautifulSoup("parser.html",u)
print(b.prettify())
time.sleep(1)
print("Downloading..")
time.sleep(0.3)
print("Downloading...")
with open(path,"w") as d:
  	d.write(u)
  	d.close()
  	print(f"file saved as : {path}")