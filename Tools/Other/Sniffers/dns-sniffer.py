#!/usr/bin/env python3

import scapy.all as scapy
import sys
import signal
from termcolor import colored


def def_handler(sig, frame):

    print(colored("\n[!] Exiting...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


def process_dns_packet(packet):

    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()

        exclude_keywords = ["google", "cloud", "bing", "static"]
        important_keywords = ["youtube", "twitch", "facebook"]

        if domain not in seen_doms and not any(keyword in domain for keyword in exclude_keywords):
            seen_doms.add(domain)
            if any(keyword in domain for keyword in important_keywords):
                print(colored(f"  [+] Domain: {domain}", "green"))
            else:
                print(colored(f"  [+] Domain: {domain}", "grey"))



def main():

    global seen_doms
    seen_doms = set()
    interface = "ens33"


    print(f"\n[*] Sniffing DNS...\n")
    scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0)


if __name__ == "__main__":
    main()
