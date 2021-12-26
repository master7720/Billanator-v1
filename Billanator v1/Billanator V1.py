import sys,os,re,socket,binascii,time,json,random,threading,queue,pprint,urllib.parse,smtplib,telnetlib,os.path,hashlib,string,urllib.request,urllib.error,urllib.parse,glob,sqlite3,urllib.request,urllib.parse,urllib.error,argparse,marshal,base64,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from queue import Queue
from time import strftime
from urllib.parse import urlparse
from urllib.request import urlopen
init()

la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'

def update_pip():
	if system() == "Linux":
		os.system('/usr/bin/python3 -m pip install --upgrade pip')
	elif system() == "Windows":
		os.system('py -m pip install --upgrade pip')

def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37 ]

	x = """ 

	██████╗ ██╗██╗     ██╗      █████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
	██╔══██╗██║██║     ██║     ██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
	██████╔╝██║██║     ██║     ███████║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
	██╔══██╗██║██║     ██║     ██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
	██████╔╝██║███████╗███████╗██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
	╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═
		
		A DavidBilla Tool 
			
			[ CLEANED BY https://t.me/f4c3r100 ]

	official channel https://t.me/tutorials_zone 
	
	1) Billanator laravel smtp cracker	11) Duplicate ips remover
	2) Crack mass smtps from combos 	12) Mass Laravel Shell Checker 
	3) Advanced shell cracker 		13) Mass AWS limit,panel checker 
	4) Advanced method for fresh ips 	14) Mass Laravel Dork Maker
	5) Private IP Reverse tool 		15) Advanced zone-h Grabber
	6) Good ip Checker 			16) Amazon Valid Email Checker 
	7) Mass IP Range Grabber 		17) CMS Filter
	8) Mass site Grabber 			18) CMS Checker +site scanner+ wp installer
	9) .env grabber 			19) Creator and update
	10) Privates cPanel Cracker 
				   
				   """
	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
try:
	update_pip()
except:
	pass

logo()


choice=input('Choose Number => ')
if choice=='1':
	print("""\n\033[91m Go to Files/Tool1 and put ur list of sites there
		and your results will be saved in results folder 

	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool1 && python3 lara.py")
		if system() == 'Windows':
			os.system('cd Files/Tool1 && py lara.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='2':
	print("""\n\033[91m Put Your combo List. Result Will Be Get Files/Tool2 with name .

	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool2 && python3 smtp.py")
		if system() == 'Windows':
			os.system('cd Files/Tool2 && py smtp.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='3':
	print("""\n\033[91m Put Ur List. Then Result Will Be Saved In Files\Tool3\Results With The Name
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool3 && python3 sc.py")
		if system() == 'Windows':
			os.system('cd Files/Tool3 && py sc.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='4':
	print("""\n\033[91m 
	Go to Files\Tool4\davidbilla.py -- change api key in line 8 
	Your Results will be saved in Files\Tool4\Results
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool4 && python3 davidbilla.py")
		if system() == 'Windows':
			os.system('cd Files/Tool4 && py davidbilla.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='5':
	print("""\n\033[91m Go to Files/Tool5 Put your iplists there
	your reversed ip lists will be saved in Files/Tool5/ip-reverse.txt
Note Domain Without Http://
Exemple : google.com 
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool5 && python3 ip.py")
		if system() == 'Windows':
			os.system('cd Files/Tool5 && py ip.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='6':
	print("""\n\033[91m Go to Files/Tool6 Put Your Email List .
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool6 && python3 gip.py")
		if system() == 'Windows':
			os.system('cd Files/Tool6 && py gip.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='7':
	print("""\n\033[91m 
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool7 && python3 ipr.py 50 ")
		if system() == 'Windows':
			os.system('cd Files/Tool7 && python3 ipr.py 50 ')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='8':
	print("""\n\033[91m 
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool8 && python3 grabsite.py")
		if system() == 'Windows':
			os.system('cd Files/Tool8 && py grabsite.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice=='9':
	print("""\n\033[91m
	y = yes 
	n = no\033[0m""")
	t=input('~>')
	if t=='y':
		if system() == 'Linux':
			os.system("cd Files/Tool9 && python3 env.py")
		if system() == 'Windows':
			os.system('cd Files/Tool9 && py env.py')
		else:
			print('unknown error :| ')
	elif t=='n':
		main()
	else :
		print('unknown error :| ')
elif choice == '10':
	print("""\n\033[91m 
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool10 && python3 masscp.py ")
		if system() == 'Windows':
			os.system('cd Files/Tool10 && py masscp.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ')
elif choice == '11':
	print("""\n\033[91m Go to Files/Tool11 Put Your URLS list of Sites in list.txt . Result Will Be Save On Files/Tool11/Result
Then Run it
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool11 && python3 d.py ")
		if system() == 'Windows':
			os.system('cd Files/Tool11 && py d.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ')
elif choice == '12':
	print("""\n\033[91m Go to Files/Tool12 Put Your Shell on list.txt
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool12 && python3 shellchecker.py ")
		if system() == 'Windows':
			os.system('cd Files/Tool12 && py shellchecker.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ')
elif choice == '13':
	print("""\n\033[91m Go to Files/Tool13
		 Put Your WSO Shell List There
Then Run it
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool13 && python3 aws.py ")
		if system() == 'Windows':
			os.system('cd Files/Tool13 && py aws.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ')
elif choice == '14':
	print("""\n\033[91m Go to Files/Tool14 
		Put Your WSO Shell List There
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool14 && python3 dorkmaker.py ")
		if system() == 'Windows':
			os.system('cd Files/Tool14 && py dorkmaker.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ')
	
elif choice == '15':
	print("""\n\033[91m 
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool15 && python3 zone.py")
		if system() == 'Windows':
			os.system('cd Files/Tool15 && py zone.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ') 
elif choice == '16':
	print("""\n\033[91m 
	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool16 && python3 amaz.py")
		if system() == 'Windows':
			os.system('cd Files/Tool16 && py amaz.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ') 
elif choice == '17':
	print("""\n\033[91m Go to Files/Tool17 Put Your URL List 

	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool17 && python3 cms.py")
		if system() == 'Windows':
			os.system('cd Files/Tool17 && py cms.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ') 
	
elif choice == '18':
	print("""\n\033[91m Go to Files/Tool18 
		Put Url Lst

	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		if system() == 'Linux':
			os.system("cd Files/Tool18 && python3 all.py")
		if system() == 'Windows':
			os.system('cd Files/Tool18 && py all.py')
		else:
			print('unknown error :| ')
	elif t == 'n':
		main()
	else:
		print('unknown error :| ') 
elif choice == '19':
	print("""\n\033[91m 

	y = yes 
	n = no\033[0m""")
	t = input('~>')
	if t == 'y':
		print("--- \t\033[31;1;3mDECODED BY @F4C3R100\t\033[0m ---\n\n\033[34m- - -\033[33m Found 2 Backdoors Embedded By \033[34m- - -\n\n\t\033[35mTG Name : \033[36;4m⏤͟͟͞͞★DA͙V͙I͙D͙ BI͙L͙L͙A͙ꗄ➺\033[0m\n\t\033[35mTG Chat : \033[36;4m@david_3illa\033[0m\n\t\033[35mTG Id   : \033[36;4m895505121\033[0m")
	elif t == 'n':
		main()
	else:
		print('unknown error :| ') 
elif choice == '20':
	print("""\n\033[91m 

	y = yes 
	n = no\033[0m""")