@echo off
:: ABOUT
:: Install script for Artisan Windows CI builds
::
:: LICENSE
:: This program or module is free software: you can redistribute it and/or
:: modify it under the terms of the GNU General Public License as published
:: by the Free Software Foundation, either version 2 of the License, or
:: version 3 of the License, or (at your option) any later versison. It is
:: provided for educational purposes and is distributed in the hope that
:: it will be useful, but WITHOUT ANY WARRANTY; without even the implied
:: warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
:: the GNU General Public License for more details.
::
:: AUTHOR
:: Dave Baxter, Marko Luther 2023


:: the current directory on entry to this script must be the folder above src

setlocal enabledelayedexpansion
if /i "%APPVEYOR%" NEQ "True" (
    echo This file is for use on Appveyor CI only.
    exit /b 1
)
if /i "%ARTISAN_LEGACY%" NEQ "True" (
    set ARTISAN_SPEC=win
) else (
    set ARTISAN_SPEC=win-legacy
)
:: ----------------------------------------------------------------------

ver
echo Python Version
python -V

::
:: get pip up to date
::
python -m pip install --upgrade pip
python -m pip install wheel

::
:: install Artisan required libraries from pip
::
python -m pip install -r src\requirements.txt | findstr /v /b "Ignoring"

::
:: custom build the pyinstaller bootloader or install a prebuilt
::
if /i "%BUILD_PYINSTALLER%"=="True" (
    echo ***** Start build pyinstaller v%PYINSTALLER_VER%
    rem
    rem download pyinstaller source
    echo ***** curl pyinstaller v%PYINSTALLER_VER%
    curl -L -O https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%PYINSTALLER_VER%.zip
    if not exist v%PYINSTALLER_VER%.zip (exit /b 100)
    7z x v%PYINSTALLER_VER%.zip
    del v%PYINSTALLER_VER%.zip
    if ERRORLEVEL 1 (exit /b 110)
    if not exist pyinstaller-%PYINSTALLER_VER%/bootloader/ (exit /b 120)
    cd pyinstaller-%PYINSTALLER_VER%/bootloader
    rem
    rem build the bootloader and wheel
    echo ***** Running WAF
    python ./waf all --msvc_targets=x64
    cd ..
    echo ***** Start build pyinstaller v%PYINSTALLER_VER% wheel
)
echo %VIRTUAL_ENV%
rem     rem redirect standard output to lower the noise in the logs
rem     python -m build --wheel > NUL
rem     if not exist dist/pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl (exit /b 130)
rem     echo ***** Finished build pyinstaller v%PYINSTALLER_VER% wheel
rem     rem
rem     rem install pyinstaller
rem     echo ***** Start install pyinstaller v%PYINSTALLER_VER%
rem     python -m pip install -q dist/pyinstaller-%PYINSTALLER_VER%-py3-none-any.whl
rem     cd ..
rem ) else (
rem      python -m pip install -q pyinstaller==%PYINSTALLER_VER%
rem )
rem echo ***** Finished install pyinstaller v%PYINSTALLER_VER%
rem 
rem ::
rem :: download and install required libraries not available on pip
rem ::
rem echo curl vc_redist.x64.exe
rem curl -L -O %VC_REDIST%
rem if not exist vc_redist.x64.exe (exit /b 140)
rem 
rem ::
rem :: copy the snap7 binary
rem ::
rem copy "%PYTHON_PATH%\Lib\site-packages\snap7\lib\snap7.dll" "C:\Windows"
rem if not exist "C:\Windows\snap7.dll" (exit /b 150)
rem 
rem ::
rem :: show set of libraries are installed
rem ::
rem echo **** pip freeze ****
rem python -m pip freeze
