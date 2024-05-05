param(
    [string]$network
)

$regex = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

function helpMessage {
    Write-Host "Usage: host_discovery.ps1 [network]"
    Write-Host "`nNetwork has to be an IPv4 address and /24 network mask`n"
    Write-Host "Example: host_discovery.ps1 192.168.1.0"
}

function ctrl_c {
    Write-Host "`n`n[!] Exiting..."
    exit 1
}

if ($network -eq "") {
    helpMessage
}
elseif ($network -eq "--help" -or $network -eq "-help" -or $network -eq "-h") {
    helpMessage
}
else {
    if ($network -notmatch $regex) {
        helpMessage
        Write-Host "`n[!] Please specify a valid IPv4 network address."
        exit 1
    }
    else {
        $ip = ($network -split '\.') | Select-Object -First 3
        $ip = $ip[0] + "." + $ip[1] + "." + $ip[2]

        Write-Host "`n[*] Discovering hosts on $network/24..."
        Write-Host ""

        if (Test-Path .\hosts) {
            Remove-Item .\hosts.txt -Force
        }

        1..254 | ForEach-Object {
            $currentIP = "$ip.$_"
            $ping = "if (Test-Connection -ComputerName $currentIP -Count 1 -Quiet -TimeToLive 1) {echo $currentIP | Out-File -FilePath .\hosts.txt -Append}"
            $null = & Start-Process -FilePath powershell -WindowStyle Hidden -PassThru -ArgumentList("-c", "$ping")
        }

        Get-Content .\hosts.txt | Select-Object -Unique
        Remove-Item .\hosts.txt -Force

        Write-Host "`n[*] Finished!"
    }
}
