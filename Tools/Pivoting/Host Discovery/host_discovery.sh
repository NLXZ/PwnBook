#!/bin/env bash

network=$1
regex='^([0-9]{1,3}\.){3}[0-9]{1,3}$'


function helpMessage () {
  echo -e "Usage: host_discovery.sh [options] [network]\n"
  echo -e "Network has to be an IPv4 address and /24 network mask\n"
  echo -e "Options:\n"
  echo -e "--help or -h\t\tDisplay this help message.\n"
  echo -e "Example: host_discovery.sh 192.168.1.0"
}

function ctrl_c () {
	echo -e "\n\n[!] Exiting..."
	tput cnorm; exit 1
}


if [ $# -eq 0 ]; then
  helpMessage
elif [ $1 == "--help" ]; then
  helpMessage
elif [ $1 == "-h" ]; then
  helpMessage
else

  if ! [[ $1 =~ $regex ]]; then
    helpMessage
    echo -e "\n[!] Please specify a valid IPv4 network address."
    tput cnorm; exit 1
  else
    trap ctrl_c SIGINT
    tput civis

    echo -e "\n[*] Discovering hosts on $network/24...\n"

    ip=$(echo $1 | awk -F'.' '{ print $1"."$2"."$3 }')

    for i in $(seq 1 254); do
	    timeout 1 bash -c "ping -c 1 $ip.$i" &>/dev/null && echo -e "  $ip.$i" &
    done; wait
    echo -e "\n[*] Finished!"
  fi
fi

tput cnorm
