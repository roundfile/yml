
# comandline option LEGACY used to flag a legacy build in NSIS
$param1=$args[0]
if ( $param1 -eq "LEGACY") {$ARTISAN_LEGACY="True"} else {$ARTISAN_LEGACY="False"}

$temp_str = Get-Content -Path ".\artisanlib\__init__.py" | ? { $_ -match "__version__\s=\s'([0-9.]*)'" }
$ARTISAN_VERSION = $matches[1]
$temp_str = Get-Content -Path ".\artisanlib\__init__.py" | ? { $_ -match "__build__\s=\s'([0-9.]*)'" }
$ARTISAN_BUILD = $matches[1]
#Write-Host "-------------"
#Write-Host "ARTISAN_VERSION $ARTISAN_VERSION"
#Write-Host "ARTISAN_BUILD $ARTISAN_BUILD"

$v = $ARTISAN_VERSION -split "\."
#Write-Host $v[0]

#$temp_str = (Get-Content -Path ".\file_version_info-win.txt").replace("_ww",$v[0]).replace("_xx",$v[1]).replace("_yy",$v[2]).replace("_zz", $ARTISAN_BUILD) | Set-Content -Path ".\file_version_info-win_MOD.txt"
#$temp_str.replace("_ww",$v[0]).replace("_xx",$v[1]).replace("_yy",$v[2]).replace("_zz", $ARTISAN_BUILD)
#$temp_str = $temp_str.replace("_ver", $ARTISAN_VERSION)

$temp_str = Get-Content -Path ".\version-info-win.txt"
$temp_str = $temp_str.replace("_ww_", $v[0])
$temp_str = $temp_str.replace("_xx_", $v[1])
$temp_str = $temp_str.replace("_yy_", $v[2])
$temp_str = $temp_str.replace("_zz_", $ARTISAN_BUILD)
$temp_str = $temp_str.replace("_ver_", $ARTISAN_VERSION)
Set-Content -Path ".\version-info.txt" -Value $temp_str -Encoding UTF8
#Write-Host $temp_str

& pyinstaller.exe --% --noconfirm Dave-artisan-win.spec

#
# Don't make assumptions as to where the 'makensis.exe' is - look in the obvious places
#

if (Test-Path -Path "C:\Program Files (x86)\NSIS\makensis.exe" -PathType Leaf) {$NSIS_EXE="C:\Program Files (x86)\NSIS\makensis.exe"}
if (Test-Path -Path "C:\Program Files\NSIS\makensis.exe" -PathType Leaf) {$NSIS_EXE="C:\Program Files\NSIS\makensis.exe"}
if (Test-Path -Path "${Env:ProgramFiles}\NSIS\makensis.exe" -PathType Leaf) {$NSIS_EXE="${Env:ProgramFiles}\NSIS\makensis.exe"}
if (Test-Path -Path "${Env:ProgramFiles(x86)}\NSIS\makensis.exe" -PathType Leaf) {$NSIS_EXE="${Env:ProgramFiles(x86)}\NSIS\makensis.exe"}
#Write-Host "-------------"
#Write-Host $NSIS_EXE
#
#
#
Write-Host "$NSIS_EXE /DPRODUCT_VERSION=$ARTISAN_VERSION.$ARTISAN_BUILD /DLEGACY=$ARTISAN_LEGACY setup-install3-pi.nsi"
#& $NSIS_EXE /DPRODUCT_VERSION=$ARTISAN_VERSION.$ARTISAN_BUILD /DLEGACY=$ARTISAN_LEGACY setup-install3-pi.nsi
