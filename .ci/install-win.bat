 @echo off
:: on entry to this script the current path must be the folder above src
echo ****** CD
cd


::
:: comandline option LEGACY is used to flag a legacy build in NSIS
::

::
:: Set the Python path, update the local path and pyinstaller version here
::
if "%APPVEYOR%" == "True" (
    echo True
    set PYTHON_PATH=%PYTHON%
) else (
    if "%~1" NEQ "LEGACY" (
        set PYTHON_PATH=c:\Python310-64
        set PYINSTALLER_VER=4.7
    ) else (
        set PYTHON_PATH=c:\Python38-64
        set PYINSTALLER_VER=4.3
    )
)

::
:: Set some env variables based on if ths is a regular or LEGACY build
::
if "%~1" NEQ "LEGACY"  (
    echo "Windows Install"
    set PYUIC=%PYTHON_PATH%\scripts\pyuic6.exe
    set ARTISAN_LEGACY="False"
    set ARTISAN_SPEC=win
    set QT_PATH=c:\qt\6.2\msvc2019_64
    set PYLUPDATE=pylupdate6pro
    set VC_REDIST=https://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe

) else (
    echo "Windows Legacy Install"
    set PYUIC=%PYTHON_PATH%\scripts\pyuic5.exe
    set ARTISAN_LEGACY="True"
    set ARTISAN_SPEC=win-legacy
    set QT_PATH=c:\qt\5.15\msvc2019_64
    set PYLUPDATE=pylupdate5pro
    set VC_REDIST=https://aka.ms/vs/17/release/vc_redist.x64.exe
)
 
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\\Scripts;%PATH%"

echo Python Version
python -V

%PYTHON_PATH%\python.exe -m pip install --upgrade pip
%PYTHON_PATH%\python.exe -m pip install wheel

::%PYTHON_PATH%\\python.exe -m pip install .ci\\pyinstaller-4.3-py3-none-any.whl
:: build the pyinstaller bootloader and install
curl -L -O https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%PYINSTALLER_VER%.zip
7z x v%PYINSTALLER_VER%.zip
del v%PYINSTALLER_VER%.zip
cd pyinstaller-%PYINSTALLER_VER%\bootloader
%PYTHON_PATH%\\python.exe ./waf all --target-arch=64bit
cd ..
%PYTHON_PATH%\\python.exe setup.py -q install
cd ..
# end: build the pyinstaller bootloader and install

%PYTHON%\python.exe -m pip install -r src\\requirements.txt
%PYTHON%\\python.exe -m pip install -r src\\requirements-win-legacy.txt
curl -L -O %VC_REDIST%
#curl -L -O https://aka.ms/vs/17/release/vc_redist.x64.exe
# curl -L -O https://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe
curl -k -L -O https://netcologne.dl.sourceforge.net/project/snap7/1.4.2/snap7-full-1.4.2.7z
7z x snap7-full-1.4.2.7z
copy snap7-full-1.4.2\build\bin\win64\snap7.dll c:\windows
curl -k -L -O https://netcologne.dl.sourceforge.net/project/libusb-win32/libusb-win32-releases/1.2.6.0/libusb-win32-bin-1.2.6.0.zip
7z x libusb-win32-bin-1.2.6.0.zip
copy libusb-win32-bin-1.2.6.0\bin\amd64\libusb0.dll C:\Windows\SysWOW64

 