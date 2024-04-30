import random, string
from colorama import init, Fore
import webbrowser


num = input(Fore.RED + 'Number of codes : ')
charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
bigStr = ""

with open("Nitro Codes.txt","w", encoding='utf-8') as file:

    print(f'{Fore.LIGHTRED_EX}Generating codes...')

    for i in range(int(num)):
        bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k = 16))}\n'
        if i % 100_000 == 0:
            file.write(f'{bigStr}\n')
            bigStr = ""


    print(f'{Fore.LIGHTRED_EX}Codes generated. Check the folder and find the text file called {Fore.LIGHTBLACK_EX}Nitro Codes.txt')
    input()