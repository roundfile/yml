@ECHO OFF

rem with admin
rem PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"

rem without admin
rem PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "if ($true) {& '%~dpn0.ps1'}"
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "if ($env:stopRdp -eq $true) {Write-Host \"hello\"; $blockRdp = $true; Write-Host $blockRdp; & %~dpn0.ps1 }" &
rem PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command \"if ($env:stopRdp -eq $true) {   '$blockRdp = $true; echo `\"$blockRdp`\"; '}\"

rem iex ((new-object net.webclient).DownloadString(`\"https://raw.githubusercontent.com/roundfile/yml/master/check_ping.ps1`\"))
echo ready to pause
rem timeout /t 2 /nobreak >nul
PAUSE