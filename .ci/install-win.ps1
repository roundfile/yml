# ABOUT
# CI install script for Artisan Windows builds
#
# LICENSE
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later versison. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
#
# AUTHOR
# Dave Baxter, Marko Luther 2023


# the current directory on entry to this script must be the folder above src
#
# script comandline option LEGACY used to flag a legacy build
#

# ----------------------------------------------------------------------
# normally these paths are set in appveyor.yml
# when running locally these paths must be set here 
# CAUTION: the paths in this section are not gurantted to be up to date!! 
# ----------------------------------------------------------------------

#$ErrorActionPreference = "Stop"

if ($env:APPVEYOR -ne "True") {
    if ($args[0] -eq "LEGACY") {
        $ARTISAN_SPEC = "win-legacy"
        $PYTHON_PATH = "c:\Python38-64"
        $QT_PATH = "c:\qt\5.15\msvc2019_64"
        $PYINSTALLER_VER = "5.7"
        $LIBUSB_VER = "1.2.6.0"
        $BUILD_PYINSTALLER = $false
        $VC_REDIST = "https://aka.ms/vs/16/release/vc_redist.x64.exe"
    }
    else {
        $ARTISAN_SPEC = "win"
        $PYTHON_PATH = "c:\Python311-64"
        $QT_PATH = "c:\qt\6.4\msvc2022_64"
        $PYINSTALLER_VER = "5.7"
        $LIBUSB_VER = "1.2.6.0"
        $BUILD_PYINSTALLER = $true
        $VC_REDIST = "https://aka.ms/vs/17/release/vc_redist.x64.exe"
    }
    $env:PATH = "$PYTHON_PATH;$PYTHON_PATH\Scripts;$env:PATH"
}
else {
    if ($env:ARTISAN_LEGACY -ne "True") {
        $env:ARTISAN_SPEC = "win"
    }
    else {
        $env:ARTISAN_SPEC = "win-legacy"
    }
}

$osVersion = Get-WmiObject -Class Win32_OperatingSystem | Select-Object -ExpandProperty Version
$versionString = "Microsoft Windows [Version $osVersion]"
Write-Host $versionString

Write-Host "Python Version"
python -V

# Get pip up to date
python -m pip install --upgrade pip
python -m pip install wheel


# Install Artisan required libraries from pip
python -m pip install -r src\requirements.txt
python -m pip install -r src\requirements-$env:ARTISAN_SPEC.txt

# Custom build the pyinstaller bootloader or install a prebuilt
if ($env:BUILD_PYINSTALLER -eq "True") {
    Write-Host "***** Start build pyinstaller v$env:PYINSTALLER_VER"
    # Download pyinstaller source
    Write-Host "***** curl pyinstaller v$env:PYINSTALLER_VER"
    Invoke-WebRequest -Uri "https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v$env:PYINSTALLER_VER.zip" -OutFile "v$env:PYINSTALLER_VER.zip"
    if (-not (Test-Path "v$env:PYINSTALLER_VER.zip")) { exit 100 }
    7z x "v$env:PYINSTALLER_VER.zip"
    Remove-Item "v$env:PYINSTALLER_VER.zip"
    if (-not (Test-Path "pyinstaller-$env:PYINSTALLER_VER/bootloader/")) { exit 101 }
    Set-Location "pyinstaller-$env:PYINSTALLER_VER/bootloader"
    # Build the bootloader and wheel
    Write-Host "***** Running WAF"
    python ./waf all --msvc_targets=x64
    Set-Location ..
    Write-Host "***** Start build pyinstaller v$env:PYINSTALLER_VER wheel"
    # Redirect standard output to lower the noise in the logs
    python -m build --wheel > $null
    if (-not (Test-Path "dist/pyinstaller-$env:PYINSTALLER_VER-py3-none-any.whl")) { exit 102 }
    Write-Host "***** Finished build pyinstaller v$env:PYINSTALLER_VER wheel"
    # Install pyinstaller
    Write-Host "***** Start install pyinstaller v$env:PYINSTALLER_VER"
    python -m pip install -q "dist/pyinstaller-$env:PYINSTALLER_VER-py3-none-any.whl"
    Set-Location ..
}
else {
    python -m pip install -q "pyinstaller==$env:PYINSTALLER_VER"
}
Write-Host "***** Finished install pyinstaller v$env:PYINSTALLER_VER"

# Download and install required libraries not available on pip
Write-Host "curl vc_redist.x64.exe"
Invoke-WebRequest -Uri $env:VC_REDIST -OutFile (Split-Path -Leaf $env:VC_REDIST)
if (-not (Test-Path "vc_redist.x64.exe")) { exit 104 }

# Copy the snap7 binary
Copy-Item "$env:PYTHON_PATH\Lib\site-packages\snap7\lib\snap7.dll" "C:\Windows"
if (-not (Test-Path "C:\Windows\snap7.dll")) { exit 105 }

# Download and copy the libusb-win32 dll
Write-Host "curl libusb-win32"

# download and copy the libusb-win32 dll. NOTE-the version number for libusb is set in the requirements-win*.txt file.
$downloadUrl = "https://netcologne.dl.sourceforge.net/project/libusb-win32/libusb-win32-releases/$LIBUSB_VER/libusb-win32-bin-$LIBUSB_VER.zip"
$zipFilePath = "libusb-win32-bin-$env:LIBUSB_VER.zip"
$extractedFolder = "libusb-win32-bin-$env:LIBUSB_VER"
$targetPath = "C:\Windows\SysWOW64\libusb0.dll"
Invoke-WebRequest -Uri $downloadUrl -OutFile $zipFilePath -UseBasicParsing
if (-not (Test-Path $zipFilePath)) {exit 106}
if ((Test-Path $zipFilePath)) {Write-Host "Exists $zipFilePath"}
Write-Host "Before unzip $zipFilePath"
7z x "$zipFilePath"
Write-Host "After unzip"
Copy-Item ".\$extractedFolder\bin\amd64\libusb0.dll" $targetPath -Force
if (-not (Test-Path $targetPath)) {exit 107}
