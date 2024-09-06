#!/usr/bin/env python3

import argparse
from termcolor import colored

def generate_usernames(name):
    
    parts = name.split()
    first_name = parts[0]
    last_name = parts[-1]
    
    # List of usernames
    usernames = []

    # Patterns to create variant usernames
    patterns = [
        
        # First name
        first_name.capitalize(),                                        # Rick
        first_name.lower(),                                             # rick
        first_name.upper(),                                             # RICK

        # Last name
        last_name.capitalize(),                                         # Sanchez
        last_name.lower(),                                              # sanchez
        last_name.upper(),                                              # SANCHEZ

        # First and last
        first_name.capitalize() + last_name.capitalize(),               # RickSanchez
        first_name.lower() + last_name.lower(),                         # ricksanchez
        first_name.upper() + last_name.upper(),                         # RICKSANCHEZ

        # Last and first
        last_name.capitalize() + first_name.capitalize(),               # SanchezRick
        last_name.lower() + first_name.lower(),                         # sanchezrick
        last_name.upper() + first_name.upper(),                         # SANCHEZRICK

        # First letters variants
        first_name.capitalize() + last_name.upper()[0],                 # RickS
        first_name.capitalize() + last_name.lower()[0],                 # Ricks
        first_name.lower() + last_name.lower()[0],                      # ricks
        first_name.upper() + last_name.upper()[0],                      # RICKS

        first_name.capitalize()[0] + last_name.capitalize(),            # RSanchez
        first_name.capitalize()[0] + last_name.lower(),                 # Rsanchez
        first_name.lower()[0] + last_name.lower(),                      # rsanchez
        first_name.upper()[0] + last_name.upper(),                      # RSANCHEZ

        # Shorter variants
        first_name.capitalize() + last_name.capitalize()[:1],           # RickS
        first_name.lower() + last_name.lower()[:1],                     # ricks
        first_name.upper() + last_name.upper()[:1],                     # RICKS
        first_name.capitalize() + last_name.capitalize()[:2],           # RickSa
        first_name.lower() + last_name.lower()[:2],                     # ricksan
        first_name.upper() + last_name.upper()[:2],                     # RICKSAN
        first_name.capitalize() + last_name.capitalize()[:3],           # RickSan
        first_name.lower() + last_name.lower()[:3],                     # ricksan
        first_name.upper() + last_name.upper()[:3],                     # RICKSAN
        first_name.capitalize() + last_name.capitalize()[:4],           # RickSanc
        first_name.lower() + last_name.lower()[:4],                     # ricksanc
        first_name.upper() + last_name.upper()[:4],                     # RICKSANC

        last_name.capitalize() + first_name.capitalize()[:1],           # SanchezR
        last_name.lower() + first_name.lower()[:1],                     # sanchezr
        last_name.upper() + first_name.upper()[:1],                     # SANCHEZR
        last_name.capitalize() + first_name.capitalize()[:2],           # SanchezRi
        last_name.lower() + first_name.lower()[:2],                     # sanchezri
        last_name.upper() + first_name.upper()[:2],                     # SANCHEZRI
        last_name.capitalize() + first_name.capitalize()[:3],           # SanchezRic
        last_name.lower() + first_name.lower()[:3],                     # sanchezric
        last_name.upper() + first_name.upper()[:3],                     # SANCHEZRIC
        last_name.capitalize() + first_name.capitalize()[:4],           # SanchezRick
        last_name.lower() + first_name.lower()[:4],                     # sanchezrick
        last_name.upper() + first_name.upper()[:4],                     # SANCHEZRICK

        ## Adding separators
        # First and last
        first_name.capitalize() + "." + last_name.capitalize(),         # Rick.Sanchez
        first_name.lower() + "." + last_name.lower(),                   # rick.sanchez
        first_name.upper() + "." + last_name.upper(),                   # RICK.SANCHEZ

        # Last and first
        last_name.capitalize() + "." + first_name.capitalize(),         # Sanchez.Rick
        last_name.lower() + "." + first_name.lower(),                   # sanchez.rick
        last_name.upper() + "." + first_name.upper(),                   # SANCHEZ.RICK

        # First letters variants
        first_name.capitalize() + "." + last_name.upper()[0],           # Rick.S
        first_name.capitalize() + "." + last_name.lower()[0],           # Rick.s
        first_name.lower() + "." + last_name.lower()[0],                # rick.s
        first_name.upper() + "." + last_name.upper()[0],                # RICK.S

        first_name.capitalize()[0] + "." + last_name.capitalize(),      # R.Sanchez
        first_name.capitalize()[0] + "." + last_name.lower(),           # R.sanchez
        first_name.lower()[0] + "." + last_name.lower(),                # r.sanchez
        first_name.upper()[0] + "." + last_name.upper(),                # R.SANCHEZ

        # Shorter variants
        first_name.capitalize() + "." + last_name.capitalize()[:1],     # Rick.S
        first_name.lower() + "." + last_name.lower()[:1],               # rick.s
        first_name.upper() + "." + last_name.upper()[:1],               # RICK.S
        first_name.capitalize() + "." + last_name.capitalize()[:2],     # Rick.Sa
        first_name.lower() + "." + last_name.lower()[:2],               # rick.san
        first_name.upper() + "." + last_name.upper()[:2],               # RICK.SAN
        first_name.capitalize() + "." + last_name.capitalize()[:3],     # Rick.San
        first_name.lower() + "." + last_name.lower()[:3],               # rick.san
        first_name.upper() + "." + last_name.upper()[:3],               # RICK.SAN
        first_name.capitalize() + "." + last_name.capitalize()[:4],     # Rick.Sanc
        first_name.lower() + "." + last_name.lower()[:4],               # rick.sanc
        first_name.upper() + "." + last_name.upper()[:4],               # RICK.SANC

        last_name.capitalize() + "." + first_name.capitalize()[:1],      # Sanchez.R
        last_name.lower() + "." + first_name.lower()[:1],               # sanchez.r
        last_name.upper() + "." + first_name.upper()[:1],               # SANCHEZ.R
        last_name.capitalize() + "." + first_name.capitalize()[:2],     # Sanchez.Ri
        last_name.lower() + "." + first_name.lower()[:2],               # sanchez.ri
        last_name.upper() + "." + first_name.upper()[:2],               # SANCHEZ.RI
        last_name.capitalize() + "." + first_name.capitalize()[:3],     # Sanchez.Ric
        last_name.lower() + "." + first_name.lower()[:3],               # sanchez.ric
        last_name.upper() + "." + first_name.upper()[:3],               # SANCHEZ.RIC
        last_name.capitalize() + "." + first_name.capitalize()[:4],     # Sanchez.Rick
        last_name.lower() + "." + first_name.lower()[:4],               # sanchez.rick
        last_name.upper() + "." + first_name.upper()[:4],               # SANCHEZ.RICK

        # First and last
        first_name.capitalize() + "-" + last_name.capitalize(),         # Rick-Sanchez
        first_name.lower() + "-" + last_name.lower(),                   # rick-sanchez
        first_name.upper() + "-" + last_name.upper(),                   # RICK-SANCHEZ

        # Last and first
        last_name.capitalize() + "-" + first_name.capitalize(),         # Sanchez-Rick
        last_name.lower() + "-" + first_name.lower(),                   # sanchez-rick
        last_name.upper() + "-" + first_name.upper(),                   # SANCHEZ-RICK

        # First letters variants
        first_name.capitalize() + "-" + last_name.upper()[0],           # Rick-S
        first_name.capitalize() + "-" + last_name.lower()[0],           # Rick-s
        first_name.lower() + "-" + last_name.lower()[0],                # rick-s
        first_name.upper() + "-" + last_name.upper()[0],                # RICK-S

        first_name.capitalize()[0] + "-" + last_name.capitalize(),      # R-Sanchez
        first_name.capitalize()[0] + "-" + last_name.lower(),           # R-sanchez
        first_name.lower()[0] + "-" + last_name.lower(),                # r-sanchez
        first_name.upper()[0] + "-" + last_name.upper(),                # R-SANCHEZ

        # Shorter variants
        first_name.capitalize() + "-" + last_name.capitalize()[:1],     # Rick-S
        first_name.lower() + "-" + last_name.lower()[:1],               # rick-s
        first_name.upper() + "-" + last_name.upper()[:1],               # RICK-S
        first_name.capitalize() + "-" + last_name.capitalize()[:2],     # Rick-Sa
        first_name.lower() + "-" + last_name.lower()[:2],               # rick-san
        first_name.upper() + "-" + last_name.upper()[:2],               # RICK-SAN
        first_name.capitalize() + "-" + last_name.capitalize()[:3],     # Rick-San
        first_name.lower() + "-" + last_name.lower()[:3],               # rick-san
        first_name.upper() + "-" + last_name.upper()[:3],               # RICK-SAN
        first_name.capitalize() + "-" + last_name.capitalize()[:4],     # Rick-Sanc
        first_name.lower() + "-" + last_name.lower()[:4],               # rick-sanc
        first_name.upper() + "-" + last_name.upper()[:4],               # RICK-SANC

        last_name.capitalize() + "-" + first_name.capitalize()[:1],     # Sanchez-R
        last_name.lower() + "-" + first_name.lower()[:1],               # sanchez-r
        last_name.upper() + "-" + first_name.upper()[:1],               # SANCHEZ-R
        last_name.capitalize() + "-" + first_name.capitalize()[:2],     # Sanchez-Ri
        last_name.lower() + "-" + first_name.lower()[:2],               # sanchez-ri
        last_name.upper() + "-" + first_name.upper()[:2],               # SANCHEZ-RI
        last_name.capitalize() + "-" + first_name.capitalize()[:3],     # Sanchez-Ric
        last_name.lower() + "-" + first_name.lower()[:3],               # sanchez-ric
        last_name.upper() + "-" + first_name.upper()[:3],               # SANCHEZ-RIC
        last_name.capitalize() + "-" + first_name.capitalize()[:4],     # Sanchez-Rick
        last_name.lower() + "-" + first_name.lower()[:4],               # sanchez-rick
        last_name.upper() + "-" + first_name.upper()[:4],               # SANCHEZ-RICK

        # First and last
        first_name.capitalize() + "_" + last_name.capitalize(),         # Rick_Sanchez
        first_name.lower() + "_" + last_name.lower(),                   # rick_sanchez
        first_name.upper() + "_" + last_name.upper(),                   # RICK_SANCHEZ

        # Last and first
        last_name.capitalize() + "_" + first_name.capitalize(),         # Sanchez_Rick
        last_name.lower() + "_" + first_name.lower(),                   # sanchez_rick
        last_name.upper() + "_" + first_name.upper(),                   # SANCHEZ_RICK

        # First letters variants
        first_name.capitalize() + "_" + last_name.upper()[0],           # Rick_S
        first_name.capitalize() + "_" + last_name.lower()[0],           # Rick_s
        first_name.lower() + "_" + last_name.lower()[0],                # rick_s
        first_name.upper() + "_" + last_name.upper()[0],                # RICK_S

        first_name.capitalize()[0] + "_" + last_name.capitalize(),      # R_Sanchez
        first_name.capitalize()[0] + "_" + last_name.lower(),           # R_sanchez
        first_name.lower()[0] + "_" + last_name.lower(),                # r_sanchez
        first_name.upper()[0] + "_" + last_name.upper(),                # R_SANCHEZ

        # Shorter variants
        first_name.capitalize() + "_" + last_name.capitalize()[:1],     # Rick_S
        first_name.lower() + "_" + last_name.lower()[:1],               # rick_s
        first_name.upper() + "_" + last_name.upper()[:1],               # RICK_S
        first_name.capitalize() + "_" + last_name.capitalize()[:2],     # Rick_Sa
        first_name.lower() + "_" + last_name.lower()[:2],               # rick_san
        first_name.upper() + "_" + last_name.upper()[:2],               # RICK_SAN
        first_name.capitalize() + "_" + last_name.capitalize()[:3],     # Rick_San
        first_name.lower() + "_" + last_name.lower()[:3],               # rick_san
        first_name.upper() + "_" + last_name.upper()[:3],               # RICK_SAN
        first_name.capitalize() + "_" + last_name.capitalize()[:4],     # Rick_Sanc
        first_name.lower() + "_" + last_name.lower()[:4],               # rick_sanc
        first_name.upper() + "_" + last_name.upper()[:4],               # RICK_SANC

        last_name.capitalize() + "_" + first_name.capitalize()[:1],     # Sanchez_R
        last_name.lower() + "_" + first_name.lower()[:1],               # sanchez_r
        last_name.upper() + "_" + first_name.upper()[:1],               # SANCHEZ_R
        last_name.capitalize() + "_" + first_name.capitalize()[:2],     # Sanchez_Ri
        last_name.lower() + "_" + first_name.lower()[:2],               # sanchez_ri
        last_name.upper() + "_" + first_name.upper()[:2],               # SANCHEZ_RI
        last_name.capitalize() + "_" + first_name.capitalize()[:3],     # Sanchez_Ric
        last_name.lower() + "_" + first_name.lower()[:3],               # sanchez_ric
        last_name.upper() + "_" + first_name.upper()[:3],               # SANCHEZ_RIC
        last_name.capitalize() + "_" + first_name.capitalize()[:4],     # Sanchez_Rick
        last_name.lower() + "_" + first_name.lower()[:4],               # sanchez_rick
        last_name.upper() + "_" + first_name.upper()[:4],               # SANCHEZ_RICK

    ]

    # Add username to the list
    for pattern in patterns:
        usernames.append(pattern)

    return usernames


if __name__ == "__main__":

    # Arguments
    parser = argparse.ArgumentParser(description='Username Generator')
    parser.add_argument('-n', '--names', type=str, help='Names separeted with commas ","')
    parser.add_argument('-f', '--file', type=str, help='File with names')
    parser.add_argument('-o', '--output', type=str, help='Output file')
    args = parser.parse_args()

    # Empty output file if exists
    if args.output:
        open(args.output, 'w').close()

    # If any input argument set, start generating
    if args.names or args.file:
        try:
            if args.names:
                names = args.names.split(",")
                names = [name.strip() for name in names]
                
                print(colored("\n[*] generating usernames...\n", "green"))

                for name in names:
                    usernames = generate_usernames(name)
                    for username in usernames:
                        if args.output is None:
                            print(username)
                        else:
                            with open(args.output, 'a') as output_file:
                                output_file.write(f"{username}\n")
                
            else:
                with open(args.file, 'r') as file:
                    names = file.readlines()
                    names = [name.strip() for name in names]
                    
                    print(colored("\n[*] generating usernames...\n", "green"))
                    
                    for name in names:
                        usernames = generate_usernames(name)
                        for username in usernames:
                            if args.output is None:
                                print(username)
                            else:
                                with open(args.output, 'a') as output_file:
                                    output_file.write(f"{username}\n")

            if args.output:
                print(colored(f"[+] output file generated: {args.output}", "green"))
            else:
                print(colored(f"\n[+] finished!", "green"))
            
        except FileNotFoundError:
            print(colored(f"\n[!] file not found: {args.file}", "red"))
        
    else:
        parser.print_help()
