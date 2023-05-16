import bs4
import time
import pandas as pd
import requests
from requests import RequestException
import os
import sys
import colorama
import pyfiglet
import random
from colorama import Fore
from googlesearch import search
########################################

# Timers


def two_secs():
    time.sleep(2)


def four_secs():
    time.sleep(4)


def eight_secs():
    time.sleep(8)


# Tricks
def Quit():
    sys.exit(1)


def Restart_The_Tool():
    os.system("python Skrappz.py")

# A Set Of Options


def options():
    opts = {1: 'Rerun The Tool',
            2: 'Quit',
            }
    for keys in opts.keys():
        print(keys, opts[keys])
    choice = (int(input("KINDLY SELECT AN OPTION!\n:::  ")))

    # A Little Magic
    if choice == 1:
        two_secs()
        print("Hold ON PLEASE!...")
        Restart_The_Tool()

    elif choice == 2:
        four_secs()
        print(" PLEASE WAIT ...")
        Quit()

    else:
        print("Keyboard EError!")
        quit()


# COLORS
B = Fore.BLUE
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
CY = Fore.CYAN
RS = Fore.RESET
MG = Fore.MAGENTA
MD = Fore.__module__

RAINBOW = (B, R, G, Y, CY, MG, MD, )

# Banner


def BANNER():
    f = pyfiglet.figlet_format("O-Query",font="banner3-D")
    print(random.choice(RAINBOW)+f)
    print(MG+"Author: Orlando The Maker"+RS)
    print(random.choice(RAINBOW)+"https://github.com/OrlandoTheMaker")


# Clear Screen
def cls():
    os.system('cls')

# Introduction


def INTRO1():
    msg = "This Script Was Written By Orlando The Maker.\n"\
          "Please Use At Free Will.\n" \
          "NOTE: The Tool Scrapes 100 Links Per Search!.\n" \
          "ADIOS!\n"
    for i in msg:
        time.sleep(0.2)
        print(i, end='')

# Data Frames

# The Magic


def work():
    query = input(CY+"Please Enter Your Search: "+RS)
    print(CY+"="*60+RS)
    for i in search(query, tld="co.in", num=100, stop=100, pause=2):
        two_secs()
        print(i)


INTRO1()
two_secs()
cls()
BANNER()
print('\n'*3)
work()
print('\n'*3)
options()

