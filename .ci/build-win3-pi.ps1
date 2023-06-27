# ABOUT
# Windows build file for Artisan
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
# on entry to this script the current path must be the src folder
#
# script comandline option LEGACY used to flag a legacy build
#

# ----------------------------------------------------------------------
# normally these paths are set in appveyor.yml
# when running locally these paths must be set here 
# CAUTION: the paths in this section are not guranteed to be up to date!! 
# ----------------------------------------------------------------------

$ErrorActionPreference = "Stop"
#Set-Location $PSScriptRoot

Set-Variable -Name "APPVEYOR" -Value $env:APPVEYOR -Scope Local -Option Constant
Set-Variable -Name "ARTISAN_SPEC" -Scope Local -Option Constant
Set-Variable -Name "PYTHON_PATH" -Scope Local -Option Constant
Set-Variable -Name "ARTISAN_LEGACY" -Scope Local -Option Constant
Set-Variable -Name "PYUIC" -Scope Local -Option Constant
Set-Variable -Name "QT_PATH" -Scope Local -Option Constant

if ($env:APPVEYOR -neq "True") {
    if ($env:~1 -eq "LEGACY") {
        Set-Variable -Name "ARTISAN_SPEC" -Value "win-legacy" -Scope Local -Option Constant
        Set-Variable -Name "PYTHON_PATH" -Value "c:\Python38-64" -Scope Local -Option Constant
        Set-Variable -Name "ARTISAN_LEGACY" -Value "True" -Scope Local -Option Constant
        Set-Variable -Name "PYUIC" -Value "pyuic5.exe" -Scope Local -Option Constant
        Set-Variable -Name "QT_PATH" -Value "c:\qt\5.15\msvc2019_64" -Scope Local -Option Constant
    } else {
        Set-Variable -Name "ARTISAN_SPEC" -Value "win" -Scope Local -Option Constant
        Set-Variable -Name "PYTHON_PATH" -Value "c:\Python311-64" -Scope Local -Option Constant
        Set-Variable -Name "ARTISAN_LEGACY" -Value "False" -Scope Local -Option Constant
        Set-Variable -Name "PYUIC" -Value "pyuic6.exe" -Scope Local -Option Constant
        Set-Variable -Name "QT_PATH" -Value "c:\qt\6.4\msvc2022_64" -Scope Local -Option Constant
    }
    $env:PATH = "$PYTHON_PATH;$PYTHON_PATH\Scripts;$env:PATH"
} else {
    if ($env:ARTISAN_LEGACY -neq "True") {
        Set-Variable -Name "ARTISAN_SPEC" -Value "win" -Scope Local -Option Constant
    } else {
        Set-Variable -Name "ARTISAN_SPEC" -Value "win-legacy" -Scope Local -Option Constant
    }
}

Set-Variable -Name "APPVEYOR" -Scope Local -Option Constant
Set-Variable -Name "ARTISAN_SPEC" -Scope Local -Option Constant
Set-Variable -Name "PYTHON_PATH" -Scope Local -Option Constant
Set-Variable -Name "ARTISAN_LEGACY" -Scope Local -Option Constant
Set-Variable -Name "PYUIC" -Scope Local -Option Constant
Set-Variable -Name "QT_PATH" -Scope Local -Option Constant

python -V

#alternate
$pythonVersion = & python -V
Write-Host $pythonVersion

Write-Host "************* build derived files **************"
& build-derived-win.bat
if ($LASTEXITCODE -ne 0) {
    Write-Host "** Failed in build-derived-win.bat"
    exit 1
}
else {
    Write-Host "** Finished build-dependant-win.bat"
}


# Set environment variables for version and build
$ARTISAN_VERSION = python -c "import artisanlib; print(artisanlib.__version__)"
$ARTISAN_BUILD = python -c "import artisanlib; print(artisanlib.__build__)"

# Create a version file for pyinstaller
create-version-file version-metadata.yml --outfile version_info-win.txt --version "$ARTISAN_VERSION.$ARTISAN_BUILD"

# Run pyinstaller
Write-Output "**** Running pyinstaller"
pyinstaller --noconfirm --log-level=WARN artisan-win.spec
if ($LASTEXITCODE -eq 1) {
    Write-Output "** Failed in pyinstaller"
    exit 1
} else {
    Write-Output "** Success"
}

# Don't make assumptions as to where the 'makensis.exe' is - look in the obvious places
if (Test-Path "C:\Program Files (x86)\NSIS\makensis.exe") {
    $NSIS_EXE = "C:\Program Files (x86)\NSIS\makensis.exe"
}
elseif (Test-Path "C:\Program Files\NSIS\makensis.exe") {
    $NSIS_EXE = "C:\Program Files\NSIS\makensis.exe"
}
elseif (Test-Path "$env:ProgramFiles\NSIS\makensis.exe") {
    $NSIS_EXE = "$env:ProgramFiles\NSIS\makensis.exe"
}
elseif (Test-Path "$env:ProgramFiles(x86)\NSIS\makensis.exe") {
    $NSIS_EXE = "$env:ProgramFiles(x86)\NSIS\makensis.exe"
}

# Echo the file date since makensis does not have a version command
$NSIS_DATE = (Get-ChildItem $NSIS_EXE).LastWriteTime
Write-Host "**** Running NSIS makensis.exe file date $NSIS_DATE"

# Run NSIS to build the install .exe file
& $NSIS_EXE "/DPRODUCT_VERSION=$env:ARTISAN_VERSION.$env:ARTISAN_BUILD" "/DLEGACY=$env:ARTISAN_LEGACY" setup-install3-pi.nsi
if ($LASTEXITCODE -ne 0) {
    Write-Host "** Failed in NSIS"
    exit 1
}
else {
    Write-Host "** Success"
}

# Package the installation zip file
if ($env:APPVEYOR -eq "True") {
    Copy-Item "..\LICENSE" "LICENSE.txt"
    & 7z.exe a "artisan-$env:ARTISAN_SPEC-$env:ARTISAN_VERSION.zip" Setup*.exe LICENSE.txt README.txt
}
# ALTERNATE
## Package the installation zip file
#if ($AppVeyor -eq "True") {
#    Copy-Item "..\LICENSE" "LICENSE.txt"
#    $zipFileName = "artisan-$($ARTISAN_SPEC)-$($ARTISAN_VERSION).zip"
#    Compress-Archive -Path "Setup*.exe","LICENSE.txt","README.txt" -DestinationPath $zipFileName
#    Write-Host "Packaged files in $zipFileName"
#}


# Check that the packaged files are above an expected size

$file = "artisan-$env:ARTISAN_SPEC-$env:ARTISAN_VERSION.zip"
$min_size = 170000000
$size = (Get-Item $file).Length

if ($size -lt $min_size) {
    Write-Host "*** Zip file is smaller than expected"
    exit 1
}
else {
    Write-Host "**** Success: $file is larger than minimum $min_size bytes"
}





_____________________________________________________

$pythonVersion = & python -V
Write-Host $pythonVersion

Write-Host "************* build derived files **************"
& build-derived-win.bat
if ($LASTEXITCODE -ne 0) {
    Write-Host "** Failed in build-derived-win.bat"
    exit 1
}
else {
    Write-Host "** Finished build-dependant-win.bat"
}

$ARTISAN_VERSION = & python -c "import artisanlib; print(artisanlib.__version__)"
$ARTISAN_BUILD = & python -c "import artisanlib; print(artisanlib.__build__)"
$versionInfo = "version_info-win.txt"
$ARTISAN_VERSION_INFO = "version-metadata.yml"
$pyInstallerCommand = "pyinstaller --noconfirm --log-level=WARN artisan-win.spec"
$NSIS_EXE = ""
$NSIS_DATE = ""

# Create version file for pyinstaller
& python -c "create-version-file $ARTISAN_VERSION_INFO --outfile $versionInfo --version $ARTISAN_VERSION.$ARTISAN_BUILD"

# Run pyinstaller
echo "**** Running pyinstaller"
& $pyInstallerCommand
if ($LASTEXITCODE -ne 0) {
    Write-Host "** Failed in pyinstaller"
    exit 1
}
else {
    Write-Host "** Success"
}

# Run NSIS to build the install .exe file
$NSIS_EXE = if (Test-Path "/Program Files (x86)/NSIS/makensis.exe") {"/Program Files (x86)/NSIS/makensis.exe"} `
            elseif (Test-Path "/Program Files/NSIS/makensis.exe") {"/Program Files/NSIS/makensis.exe"} `
            elseif (Test-Path "%ProgramFiles%/NSIS/makensis.exe") {"%ProgramFiles%/NSIS/makensis.exe"} `
            elseif (Test-Path "%ProgramFiles(x86)%/NSIS/makensis.exe") {"%ProgramFiles(x86)%/NSIS/makensis.exe"} `
            else {""}
$NSIS_DATE = ""
foreach ($exe in $NSIS_EXE) {
    $NSIS_DATE = (Get-Item $exe).LastWriteTime.ToString()
    break
}

# Package the installation zip file
if ($AppVeyor -eq "True") {
    Copy-Item "..\LICENSE" "LICENSE.txt"
    $zipFileName = "artisan-$($ARTISAN_SPEC)-$($ARTISAN_VERSION).zip"
    Compress-Archive -Path "Setup*.exe","LICENSE.txt","README.txt" -DestinationPath $zipFileName
    Write-Host "Packaged files in $zipFileName"
}

# Check that the packaged files are above an expected size
$file = "artisan-$($ARTISAN_SPEC)-$($ARTISAN_VERSION).zip"
$expectedSize = 170000000
$actualSize = (Get-Item $file).Length
if ($actualSize -lt $expectedSize) {
    Write-Host "*** Zip file is smaller than expected"
    exit 1
}
else {
    Write-Host "**** Success: $file is larger than minimum $expectedSize bytes"
}

# Run NSIS to build the install .exe file
$NSIS_EXE = if (Test-Path "/Program Files (x86)/NSIS/makensis.exe") {"/Program Files (x86)/NSIS/makensis.exe"} `
            elseif (Test-Path "/Program Files/NSIS/makensis.exe") {"/Program Files/NSIS/makensis.exe
