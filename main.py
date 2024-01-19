import sys
import os
from pystyle import Center
import webbrowser
from src.apiflood import apiflood, checkapi
from src.dnschecker import dns
from src.flood import conflood
from src.ports import sockscan, reqscan 
from src.spoofcon import spoof

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

logo = f"""{RED}                     
    ███        ▄████████ ▀████    ▐████▀ ███▄▄▄▄      ▄████████     ███     
▀█████████▄   ███    ███   ███▌   ████▀  ███▀▀▀██▄   ███    ███ ▀█████████▄ 
   ▀███▀▀██   ███    ███    ███  ▐███    ███   ███   ███    █▀     ▀███▀▀██ 
    ███   ▀   ███    ███    ▀███▄███▀    ███   ███  ▄███▄▄▄         ███   ▀ 
    ███     ▀███████████    ████▀██▄     ███   ███ ▀▀███▀▀▀         ███     
    ███       ███    ███   ▐███  ▀███    ███   ███   ███    █▄      ███     
    ███       ███    ███  ▄███     ███▄  ███   ███   ███    ███     ███     
   ▄████▀     ███    █▀  ████       ███▄  ▀█   █▀    ██████████    ▄████▀  
{WHITE}
Private Web/Api Stresser/Spoofer.

{RED}[1]{WHITE} API Stresser\t\t\t{RED}[2]{WHITE} Check API Response
{RED}[3]{WHITE} DNS Lookup\t\t\t\t{RED}[4]{WHITE} IP Stresser
{RED}[5]{WHITE} Portscanner\t\t\t{RED}[6]{WHITE} Connection Spoofer
{RED}[00]{WHITE} Exit\t\t\t\t{RED}[99]{WHITE} Tool Info
"""

# logo = Center.XYCenter(logo)
logo =  Center.XCenter(logo)
logo = Center.YCenter(logo)


file = open(f"src\\fromthedev.txt","w")
file.write("This tool is coded by Sido!")
file.close()

os.system("cls || clear")
os.system("title TaxNet")
print(logo, end="\n")
option = int(input("enter choice: "))

def clear():
    os.system("cls || clear")

def a():
    print(f"{RED}RELAUNCH THE CLIENT TO CLOSE THE PROCESS{WHITE}")

# main
while True:

  if option == 1:
      a()
      url = input(f"{RED}[URL]{WHITE} enter url: ")
      apiflood(url)

  elif option == 2:
      a()
      url = input(f"{RED}[URL]{WHITE} enter url: ")
      checkapi(url)

  elif option == 3:
      a()
      url = input(f"{RED}[URL]{WHITE} enter url: ")
      dns(url)

  elif option == 4:
      a()
      ip = str(input(f"{RED}[IP]{WHITE} enter ip: "))
      port = int(input(f"{RED}[INT: PORT]{WHITE} port: "))
      sleep = float(input(f"{RED}[FLOAT: SLEEP]{WHITE} sleep: "))
      conflood(ip, port, sleep)

  elif option == 5:
      a()
      ip = input(f"{RED}[IP]{WHITE} IP: ")
      s = int(input(f"{RED}[START]{WHITE} STARTPORT: "))
      e = int(input(f"{RED}[END]{WHITE} ENDPORT: "))
      while True:
          nd = input(f"{RED}[PORTSCAN: HOME]{WHITE} requests: 'r' or socket: 's': ")
          help = nd.lower()
          if help == "r":
              open_ports = reqscan(ip, s, e)
              print(f"{PURPLE}[+]{WHITE} Open ports:", open_ports)
          elif help == "s":
              open_ports = sockscan(ip, s, e)
              print(f"{PURPLE}[+]{WHITE} Open ports:", open_ports)
          else:
              print(f"{RED}[ERROR]{WHITE} Invalid choice '{nd}', its either 'r' or 's'.")

  elif option == 6:
      a()
      ip = input(f"{RED}[HOST]{WHITE} Host IP: ")
      port = int(input(f"{RED}[ACCESS]{WHITE} Access Port: "))
      print(f"{RED}[HIJACK]{WHITE} Connecting to host...")
      spoof(ip, port)

  elif option == 99:
      print(f"""Hello this is Sido, Thank you so much for using my tool.  

""")
      x = input(f"{GREEN}[LINK]{WHITE} Roblox/Discord: ")
      imlonely = x.lower()
      if imlonely == "roblox":
          webbrowser.open_new_tab("https://www.roblox.com/users/3574157026/profile")
          print(f"Opened roblox link in your browser :)")
          input()
      elif imlonely == "discord":
          webbrowser.open_new_tab("https://discord.gg/ducking")
          print(f"Opened discord link in your browser :)")
          input()
      else:
          print(f"{RED}[!]{WHITE} Invalid link '{x}', try 'roblox' or 'discord'")
          input()
  elif option == 00:
      clear()
      os.system("title Exitting...")
      print(f"press any key to exit")
      input()
      sys.exit()