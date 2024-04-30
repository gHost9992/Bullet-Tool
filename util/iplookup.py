import random
import requests

from colorama import Fore

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



ip_input = input(f"{r}IP : {b}")


def lookup():
    
    headers = {
        'authority': 'ipinfo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'referer': 'https://ipinfo.io/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
    r = requests.get(f'https://ipinfo.io/widget/demo/{ip_input}', headers=headers)
    ip = r.json()['data']['ip']
    city = r.json()['data']['city']
    region = r.json()['data']['region']
    country = r.json()['data']['country']
    timezone = r.json()['data']['timezone']
    address = r.json()['data']['abuse']['address']
    country = r.json()['data']['abuse']['country']
    print(f'{Fore.LIGHTRED_EX}IP: {Fore.LIGHTBLACK_EX}{ip}')
    print(f'{Fore.LIGHTRED_EX}City: {Fore.LIGHTBLACK_EX}{city}')
    print(f'{Fore.LIGHTRED_EX}Region: {Fore.LIGHTBLACK_EX}{region}')
    print(f'{Fore.LIGHTRED_EX}Country: {Fore.LIGHTBLACK_EX}{country}')
    print(f'{Fore.LIGHTRED_EX}Timezone: {Fore.LIGHTBLACK_EX}{timezone}')
    print(f'{Fore.LIGHTRED_EX}Address: {Fore.LIGHTBLACK_EX}{address}')


lookup()
input(f"Press enter to continue : ")
