# CODED : AkasakaID
# Time : 13/03/2020
# LIHAT? BOLEH , REKOD? JANGAN 
# KONTOL KONTOL KONTOL
# https://trakteer.id/fowawaz
import requests,os
r = requests.Session()
from bs4 import BeautifulSoup as bs
if os.name == 'nt':os.system('cls')
else:os.system('clear')
url = 'https://www.name-generator.org.uk/quick/'
def ban():
	if os.name == 'nt':os.system('cls')
	else:os.system('clear')
	print("""
╔╗╔┌─┐┌┬┐┌─┐  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║║║├─┤│││├┤   ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╝╚╝┴ ┴┴ ┴└─┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
[-] powered by https://www.name-generator.org.uk
[-] buy me es teh? https://trakteer.id/fowawaz
		""")
ban()
try:
	count = input("Jumlah: ")
	sex = input("1.Female\n2.Male\nPilihan: ")
	if sex == "1":
		sex = "f"
	elif sex == "2":
		sex = "m"
	else:
		print("Masukkan data yang benar!!")
		exit()
	data = {"type": "12","spam_check": "","count": count,"gender": sex}
	a = r.post(url,data=data).text
	ban()
	print("Result!!\n")
	b = bs(a,"html.parser")
	for name in b.findAll("div",attrs={"class":"name_heading"}):
		print(name.text)
except Exception as e:
	print("[Error]:",str(e))
	exit()
except KeyboardInterrupt:
	print("\nKeluar..!!")
	exit()
