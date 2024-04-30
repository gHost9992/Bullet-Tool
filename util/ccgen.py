import random
import time as t


import colorama
from colorama import Fore,Back, Style
colorama.init()


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


number = random.randint(1000000000000000, 100000000000000000)
date = random.randint(1, 12)
date1 = random.randint(2025, 2035)
cvv = random.randint(100, 1000)

print(f"{lr}Generating...")
t.sleep(3)

print(Fore.RED)
print("Credit Card Generated.")

print(Fore.LIGHTBLACK_EX)
print(f"Num: {lr}{number}")
print(f"{b}Date: {lr}{date}/{date1} ")
print(f"{b}CVV: {lr}{cvv}")
input(f"{r}Press enter to continue : ")
