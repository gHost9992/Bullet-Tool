import colorama
from colorama import Fore, Back, Style, init
import requests
from time import sleep
import os
import os.path
from requests.api import options
import sys
import webbrowser
colorama.init(autoreset=True)
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Bullet Multi Tool")

def menu():
    print(f"""{Fore.LIGHTRED_EX}

 [1] Lookup Server      [2] Exit

""")
menu()

option = int(input(f"{Fore.RED} [>] {Fore.LIGHTRED_EX}"))


def fetch_data():
        menu()
if option == 1:
        sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Bullet Multi Tool")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{Fore.LIGHTRED_EX}


""")

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n{Fore.LIGHTRED_EX} Enter Your Token. [>] ")
        }

        guildId = input(f"\n{Fore.LIGHTRED_EX} Enter Server ID. [>] ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""{Fore.LIGHTRED_EX}
 Guild/Server | Name > {response['name']} 
 Guild/Server | ID > {response['id']}
 Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
 Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
 Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
 Guild/Server | Owner ID > {response['owner_id']}
 Guild/Server | Region > {response['region']}
""")
        input()
        exit()

elif option == 2:
       exit()